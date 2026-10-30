import sqlite3
import datetime
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "triage.db")
_RANK = {"Emergency": 0, "Urgent": 1, "Routine": 2}

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT DEFAULT 'Other',
                temp REAL NOT NULL,
                sbp INTEGER NOT NULL,
                dbp INTEGER DEFAULT 80,
                spo2 INTEGER NOT NULL,
                pulse INTEGER NOT NULL,
                symptoms TEXT NOT NULL,
                priority TEXT NOT NULL,
                reasons TEXT NOT NULL,
                reasons_hi TEXT,
                reasons_pa TEXT,
                actions TEXT,
                actions_hi TEXT,
                actions_pa TEXT,
                teacher_notes TEXT,
                teacher_notes_hi TEXT,
                teacher_notes_pa TEXT,
                consent INTEGER DEFAULT 1,
                synced INTEGER DEFAULT 0,
                created TEXT NOT NULL
            )
        """)
    conn.close()
    seed_sample_data_if_empty()

def seed_sample_data_if_empty():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM patients")
    count = cur.fetchone()[0]
    if count == 0:
        sample_patients = [
            {
                "name": "Gurpreet Singh",
                "age": 58,
                "gender": "Male",
                "temp": 37.1,
                "sbp": 175,
                "dbp": 105,
                "spo2": 88,
                "pulse": 118,
                "symptoms": "Chest pain, Breathlessness",
                "priority": "Emergency",
                "reasons": "SpO2 88% indicates severe hypoxemia; Chest pain red flag; Hypertensive crisis",
                "reasons_hi": "SpO2 88% गंभीर हाइपोक्सिमिया (ऑक्सीजन की कमी) दर्शाता है; सीने में दर्द आपातकालीन संकेत है",
                "reasons_pa": "SpO2 88% ਗੰਭੀਰ ਆਕਸੀਜਨ ਦੀ ਘਾਟ ਦਰਸਾਉਂਦਾ ਹੈ; ਛਾਤੀ ਵਿੱਚ ਦਰਦ ਐਮਰਜੈਂਸੀ ਚੇਤਾਵਨੀ ਹੈ",
                "actions": "Keep patient seated at 45°; Administer 4-6 L/min O2; Call 108 Emergency Ambulance immediately; Keep chewable Aspirin 300mg ready if confirmed by doctor.",
                "actions_hi": "मरीज़ को 45° पर बैठाएं; तुरंत 4-6 L/मि. ऑक्सीजन शुरू करें; 108 एम्बुलेंस को तत्काल कॉल करें।",
                "actions_pa": "ਮਰੀਜ਼ ਨੂੰ 45° 'ਤੇ ਬਿਠਾਓ; ਤੁਰੰਤ 4-6 L/ਮਿੰਟ ਆਕਸੀਜਨ ਦਿਓ; 108 ਐਂਬੂਲੈਂਸ ਨੂੰ ਤੁਰੰਤ ਕਾਲ ਕਰੋ।",
                "teacher_notes": "Clinical Teaching: In patients >50 with chest pain and SpO2 < 92%, suspect acute coronary syndrome with pulmonary congestion. Time is muscle.",
                "teacher_notes_hi": "नैदानिक सीख: 50+ आयु के मरीज़ में सीने में दर्द और कम ऑक्सीजन दिल के दौरे का गंभीर संकेत हो सकता है। समय अमूल्य है।",
                "teacher_notes_pa": "ਕਲੀਨਿਕਲ ਸਿੱਖਿਆ: 50 ਸਾਲ ਤੋਂ ਵੱਧ ਉਮਰ ਵਿੱਚ ਛਾਤੀ ਵਿੱਚ ਦਰਦ ਅਤੇ ਘੱਟ ਆਕਸੀਜਨ ਦਿਲ ਦੇ ਦੌਰੇ ਦਾ ਸੰਕੇਤ ਹੋ ਸਕਦੀ ਹੈ। ਸਮਾਂ ਬਹੁਤ ਮਹੱਤਵਪੂਰਨ ਹੈ।",
                "consent": 1,
                "synced": 0,
                "created": (datetime.datetime.now() - datetime.timedelta(minutes=42)).isoformat(timespec="seconds")
            },
            {
                "name": "Simran Kaur",
                "age": 28,
                "gender": "Female",
                "temp": 39.4,
                "sbp": 125,
                "dbp": 82,
                "spo2": 95,
                "pulse": 112,
                "symptoms": "Fever, Vomiting, Headache",
                "priority": "Urgent",
                "reasons": "High grade fever (39.4°C); Tachycardia (Pulse 112 bpm); Risk of acute dehydration",
                "reasons_hi": "तेज़ बुखार (39.4°C); तेज़ नाड़ी (112 bpm); निर्जलीकरण (डिहाइड्रेशन) का जोखिम",
                "reasons_pa": "ਤੇਜ਼ ਬੁਖ਼ਾਰ (39.4°C); ਤੇਜ਼ ਨਬਜ਼ (112 bpm); ਪਾਣੀ ਦੀ ਘਾਟ ਦਾ ਖ਼ਤਰਾ",
                "actions": "Oral rehydration therapy (ORS); Cold sponging; Paracetamol under nurse protocol; Monitor vitals every 30 mins.",
                "actions_hi": "ओआरएस (ORS) घोल दें; ठंडे पानी की पट्टी रखें; 30 मिनट में दोबारा तापमान जाँचें।",
                "actions_pa": "ਓ.ਆਰ.ਐੱਸ. (ORS) ਘੋਲ ਦਿਓ; ਮੱਥੇ 'ਤੇ ਠੰਢੀਆਂ ਪੱਟੀਆਂ ਰੱਖੋ; ਹਰ 30 ਮਿੰਟ ਬਾਅਦ ਤਾਪਮਾਨ ਚੈੱਕ ਕਰੋ।",
                "teacher_notes": "Clinical Teaching: High fever with persistent vomiting accelerates dehydration rapidly. Check capillary refill and skin turgor.",
                "teacher_notes_hi": "नैदानिक सीख: उल्टी के साथ तेज़ बुखार से शरीर में पानी तेजी से घटता है। निर्जलीकरण के लक्षणों पर नज़र रखें।",
                "teacher_notes_pa": "ਕਲੀਨਿਕਲ ਸਿੱਖਿਆ: ਉਲਟੀ ਦੇ ਨਾਲ ਤੇਜ਼ ਬੁਖ਼ਾਰ ਸਰੀਰ ਵਿੱਚ ਪਾਣੀ ਦੀ ਤੇਜ਼ੀ ਨਾਲ ਘਾਟ ਕਰਦਾ ਹੈ। ਨਿਰਜਲੀਕਰਨ ਦੇ ਲੱਛਣਾਂ ਦੀ ਜਾਂਚ ਕਰੋ।",
                "consent": 1,
                "synced": 1,
                "created": (datetime.datetime.now() - datetime.timedelta(minutes=85)).isoformat(timespec="seconds")
            },
            {
                "name": "Ram Lal",
                "age": 42,
                "gender": "Male",
                "temp": 36.8,
                "sbp": 122,
                "dbp": 78,
                "spo2": 98,
                "pulse": 76,
                "symptoms": "Cough",
                "priority": "Routine",
                "reasons": "Normal vitals; Stable parameters; Mild seasonal cough without respiratory distress",
                "reasons_hi": "सामान्य जीवन संकेत; स्थिर स्थिति; बिना किसी सांस की तकलीफ के हल्की खांसी",
                "reasons_pa": "ਆਮ ਜੀਵਨ ਸੰਕੇਤ; ਸਥਿਰ ਹਾਲਤ; ਬਿਨਾਂ ਸਾਹ ਦੀ ਤਕਲੀਫ ਦੇ ਆਮ ਖੰਘ",
                "actions": "Steam inhalation; Warm fluids; Routine OPD consultation; Advise return if breathlessness or fever develops.",
                "actions_hi": "भाप लें; गुनगुना पानी पिएं; नियमित ओपीडी परामर्श लें।",
                "actions_pa": "ਭਾਫ਼ ਲਵੋ; ਗਰਮ ਪਾਣੀ ਪੀਓ; ਆਮ ਓ.ਪੀ.ਡੀ. ਵਿੱਚ ਡਾਕਟਰ ਨੂੰ ਦਿਖਾਓ।",
                "teacher_notes": "Clinical Teaching: For chronic cough without fever or weight loss, rule out seasonal allergy and advise sputum testing if persisting >2 weeks (TB screening).",
                "teacher_notes_hi": "नैदानिक सीख: यदि 2 सप्ताह से अधिक खांसी रहे तो टीबी (क्षयरोग) स्क्रीनिंग आवश्यक है।",
                "teacher_notes_pa": "ਕਲੀਨਿਕਲ ਸਿੱਖਿਆ: ਜੇਕਰ ਖੰਘ 2 ਹਫ਼ਤਿਆਂ ਤੋਂ ਵੱਧ ਰਹੇ ਤਾਂ ਟੀ.ਬੀ. ਟੈਸਟ ਜ਼ਰੂਰੀ ਹੈ।",
                "consent": 1,
                "synced": 1,
                "created": (datetime.datetime.now() - datetime.timedelta(minutes=150)).isoformat(timespec="seconds")
            }
        ]
        with conn:
            for p in sample_patients:
                conn.execute("""
                    INSERT INTO patients (
                        name, age, gender, temp, sbp, dbp, spo2, pulse,
                        symptoms, priority, reasons, reasons_hi, reasons_pa,
                        actions, actions_hi, actions_pa,
                        teacher_notes, teacher_notes_hi, teacher_notes_pa,
                        consent, synced, created
                    ) VALUES (
                        :name, :age, :gender, :temp, :sbp, :dbp, :spo2, :pulse,
                        :symptoms, :priority, :reasons, :reasons_hi, :reasons_pa,
                        :actions, :actions_hi, :actions_pa,
                        :teacher_notes, :teacher_notes_hi, :teacher_notes_pa,
                        :consent, :synced, :created
                    )
                """, p)
    conn.close()

def add_patient(d):
    init_db()
    conn = get_conn()
    now_str = datetime.datetime.now().isoformat(timespec="seconds")
    with conn:
        cur = conn.execute("""
            INSERT INTO patients (
                name, age, gender, temp, sbp, dbp, spo2, pulse,
                symptoms, priority, reasons, reasons_hi, reasons_pa,
                actions, actions_hi, actions_pa,
                teacher_notes, teacher_notes_hi, teacher_notes_pa,
                consent, synced, created
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?,
                ?, ?, ?,
                ?, ?, ?,
                ?, 0, ?
            )
        """, (
            d.get("name"),
            int(d.get("age", 30)),
            d.get("gender", "Other"),
            float(d.get("temp", 37.0)),
            int(d.get("sbp", 120)),
            int(d.get("dbp", 80)),
            int(d.get("spo2", 98)),
            int(d.get("pulse", 75)),
            d.get("symptoms", ""),
            d.get("priority", "Routine"),
            d.get("reasons", ""),
            d.get("reasons_hi", ""),
            d.get("reasons_pa", ""),
            d.get("actions", ""),
            d.get("actions_hi", ""),
            d.get("actions_pa", ""),
            d.get("teacher_notes", ""),
            d.get("teacher_notes_hi", ""),
            d.get("teacher_notes_pa", ""),
            int(d.get("consent", 1)),
            now_str
        ))
        pid = cur.lastrowid
    conn.close()
    return pid

def get_queue():
    init_db()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return sorted(rows, key=lambda r: (_RANK.get(r["priority"], 3), r["created"]), reverse=False)

def get_patient(pid):
    init_db()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients WHERE id = ?", (pid,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None

def mark_synced():
    init_db()
    conn = get_conn()
    with conn:
        conn.execute("UPDATE patients SET synced = 1")
    conn.close()

def delete_patient(pid):
    init_db()
    conn = get_conn()
    with conn:
        conn.execute("DELETE FROM patients WHERE id = ?", (pid,))
    conn.close()

def reset_db_with_samples():
    if os.path.exists(DB_PATH):
        try:
            os.remove(DB_PATH)
        except Exception:
            pass
    init_db()

# Auto-initialize
init_db()
