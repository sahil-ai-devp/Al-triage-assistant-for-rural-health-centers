import json
from flask import Flask, render_template, request, redirect, jsonify, url_for
import database as store
from triage_engine import assess
import i18n

app = Flask(__name__)

# Ensure DB initialized
store.init_db()

@app.route("/")
def home():
    lang = request.args.get("lang", "en")
    if lang not in i18n.LANGS:
        lang = "en"
    
    view = request.args.get("view", "triage")
    rows = store.get_queue()
    counts = {p: sum(r["priority"] == p for r in rows) for p in ("Emergency", "Urgent", "Routine")}
    pending = sum(not r.get("synced") for r in rows)
    
    pid = request.args.get("id", type=int)
    last = store.get_patient(pid) if pid else None

    # Pick localized strings for last patient if present
    last_localized = None
    if last:
        last_localized = dict(last)
        if lang == "hi":
            last_localized["display_reasons"] = last.get("reasons_hi") or last.get("reasons")
            last_localized["display_actions"] = last.get("actions_hi") or last.get("actions")
            last_localized["display_teacher_notes"] = last.get("teacher_notes_hi") or last.get("teacher_notes")
        elif lang == "pa":
            last_localized["display_reasons"] = last.get("reasons_pa") or last.get("reasons")
            last_localized["display_actions"] = last.get("actions_pa") or last.get("actions")
            last_localized["display_teacher_notes"] = last.get("teacher_notes_pa") or last.get("teacher_notes")
        else:
            last_localized["display_reasons"] = last.get("reasons")
            last_localized["display_actions"] = last.get("actions")
            last_localized["display_teacher_notes"] = last.get("teacher_notes")

    # Localize queue display reasons
    localized_rows = []
    for r in rows:
        row_copy = dict(r)
        if lang == "hi" and r.get("reasons_hi"):
            row_copy["display_reasons"] = r.get("reasons_hi")
        elif lang == "pa" and r.get("reasons_pa"):
            row_copy["display_reasons"] = r.get("reasons_pa")
        else:
            row_copy["display_reasons"] = r.get("reasons")
        localized_rows.append(row_copy)

    t = i18n.UI.get(lang, i18n.UI["en"])

    return render_template(
        "index.html",
        rows=localized_rows,
        counts=counts,
        pending=pending,
        symptoms=i18n.SYMPTOMS,
        last=last_localized,
        raw_last=last,
        lang=lang,
        langs=i18n.LANGS,
        t=t,
        view=view,
        training_cases=i18n.TRAINING_CASES,
        protocols=i18n.PROTOCOLS,
        i18n_json=json.dumps(i18n.UI),
        symptoms_json=json.dumps(i18n.SYMPTOMS)
    )

@app.route("/assess", methods=["POST"])
def do_assess():
    f = request.form
    lang = f.get("lang", "en")
    if lang not in i18n.LANGS:
        lang = "en"

    if f.get("consent") != "yes":
        return "Patient consent is required before recording assessment.", 400

    name = f.get("name", "").strip()
    if not name:
        return "Patient name is required.", 400

    gender = f.get("gender", "Other")

    try:
        v = {
            "age": int(f.get("age", 30)),
            "sbp": int(f.get("sbp", 120)),
            "dbp": int(f.get("dbp", 80)),
            "spo2": int(f.get("spo2", 98)),
            "temp": float(f.get("temp", 37.0)),
            "pulse": int(f.get("pulse", 75))
        }
    except (ValueError, KeyError):
        return "Please enter valid numeric patient measurements.", 400

    if not (0 <= v["age"] <= 125 and
            30 <= v["sbp"] <= 300 and
            20 <= v["dbp"] <= 200 and
            0 <= v["spo2"] <= 100 and
            25 <= v["temp"] <= 45 and
            0 <= v["pulse"] <= 300):
        return "Measurements are outside physiologically accepted input ranges.", 400

    sym = f.getlist("sym")
    result = assess(sym, gender=gender, **v)

    pid = store.add_patient({
        "name": name,
        "gender": gender,
        "symptoms": ", ".join(sym) if sym else "None reported",
        "priority": result["priority"],
        "reasons": result["reasons"],
        "reasons_hi": result["reasons_hi"],
        "reasons_pa": result["reasons_pa"],
        "actions": result["actions"],
        "actions_hi": result["actions_hi"],
        "actions_pa": result["actions_pa"],
        "teacher_notes": result["teacher_notes"],
        "teacher_notes_hi": result["teacher_notes_hi"],
        "teacher_notes_pa": result["teacher_notes_pa"],
        "consent": 1,
        **v
    })

    return redirect(f"/?id={pid}&lang={lang}")

@app.route("/api/assess", methods=["POST"])
def api_assess():
    data = request.get_json(silent=True) or request.form
    try:
        age = int(data.get("age", 30))
        sbp = int(data.get("sbp", 120))
        dbp = int(data.get("dbp", 80))
        spo2 = int(data.get("spo2", 98))
        temp = float(data.get("temp", 37.0))
        pulse = int(data.get("pulse", 75))
        gender = data.get("gender", "Other")
        sym = data.get("sym", [])
        if isinstance(sym, str):
            sym = [s.strip() for s in sym.split(",") if s.strip()]
        result = assess(sym, age=age, sbp=sbp, dbp=dbp, spo2=spo2, temp=temp, pulse=pulse, gender=gender)
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/referral/<int:pid>")
def view_referral(pid):
    patient = store.get_patient(pid)
    if not patient:
        return "Patient record not found", 404
    lang = request.args.get("lang", "en")
    t = i18n.UI.get(lang, i18n.UI["en"])
    return render_template("referral.html", p=patient, lang=lang, t=t)

@app.route("/sync", methods=["POST"])
def sync():
    lang = request.form.get("lang", request.args.get("lang", "en"))
    store.mark_synced()
    if request.headers.get("X-Requested-With") == "XMLHttpRequest" or request.is_json:
        return jsonify({"status": "success", "message": "Synchronized successfully"})
    return redirect(f"/?lang={lang}&synced=1")

@app.route("/delete/<int:pid>", methods=["POST"])
def delete_item(pid):
    lang = request.form.get("lang", request.args.get("lang", "en"))
    store.delete_patient(pid)
    return redirect(f"/?lang={lang}")

@app.route("/reset-demo", methods=["POST"])
def reset_demo():
    lang = request.form.get("lang", request.args.get("lang", "en"))
    store.reset_db_with_samples()
    return redirect(f"/?lang={lang}&demo_reset=1")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
