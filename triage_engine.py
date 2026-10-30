"""
AI Triage Decision Support & Clinical Teacher Engine
Designed for Rural Health Centres / Sub-Centres / ASHA Workers.
Incorporates WHO ETAT and Indian NHM frontline triage standards.
Provides tri-lingual explainable rationale, emergency protocol actions,
and clinical teaching insights for health workers.
"""

def evaluate_vitals(age, sbp, dbp, spo2, temp, pulse):
    status = {
        "spo2": "normal",
        "sbp": "normal",
        "dbp": "normal",
        "temp": "normal",
        "pulse": "normal"
    }

    # SpO2 evaluation
    if spo2 < 90:
        status["spo2"] = "critical"
    elif spo2 <= 94:
        status["spo2"] = "warning"

    # Blood Pressure (Adult standard, adjusted if pediatric)
    if age < 12:
        if sbp > 130 or sbp < 70:
            status["sbp"] = "critical"
        elif sbp > 115 or sbp < 80:
            status["sbp"] = "warning"
    else:
        if sbp >= 180 or sbp < 85 or dbp >= 115 or dbp < 50:
            status["sbp"] = "critical"
            status["dbp"] = "critical"
        elif sbp >= 140 or sbp < 95 or dbp >= 90 or dbp < 60:
            status["sbp"] = "warning"
            status["dbp"] = "warning"

    # Temperature
    if temp >= 39.5 or temp < 35.0:
        status["temp"] = "critical"
    elif temp >= 38.0 or temp < 36.0:
        status["temp"] = "warning"

    # Pulse (Age-dependent)
    if age <= 1:
        if pulse > 170 or pulse < 80:
            status["pulse"] = "critical"
        elif pulse > 150 or pulse < 90:
            status["pulse"] = "warning"
    elif age < 12:
        if pulse > 140 or pulse < 60:
            status["pulse"] = "critical"
        elif pulse > 120 or pulse < 70:
            status["pulse"] = "warning"
    else:
        if pulse > 130 or pulse < 45:
            status["pulse"] = "critical"
        elif pulse > 100 or pulse < 55:
            status["pulse"] = "warning"

    return status

def assess(sym, age=30, sbp=120, dbp=80, spo2=98, temp=37.0, pulse=75, gender="Other"):
    sym_set = set(sym) if isinstance(sym, (list, set, tuple)) else set(s.strip() for s in sym.split(",") if s.strip())
    vitals_status = evaluate_vitals(age, sbp, dbp, spo2, temp, pulse)

    reasons_en = []
    reasons_hi = []
    reasons_pa = []

    actions_en = []
    actions_hi = []
    actions_pa = []

    teacher_notes_en = []
    teacher_notes_hi = []
    teacher_notes_pa = []

    is_emergency = False
    is_urgent = False

    # --- 1. CRITICAL RED FLAGS (EMERGENCY) ---
    if "Unconscious/seizure" in sym_set:
        is_emergency = True
        reasons_en.append("Active or recent seizure / loss of consciousness (Airway compromise risk)")
        reasons_hi.append("बेहोशी या दौरा (श्वसन मार्ग अवरुद्ध होने का गंभीर खतरा)")
        reasons_pa.append("ਬੇਹੋਸ਼ੀ ਜਾਂ ਦੌਰਾ (ਸਾਹ ਨਾਲੀ ਬੰਦ ਹੋਣ ਦਾ ਗੰਭੀਰ ਖ਼ਤਰਾ)")
        actions_en.append("Place in lateral recovery position; maintain clear airway; do not insert objects into mouth; call 108 immediately.")
        actions_hi.append("मरीज़ को करवट के बल लिटाएं (रिकवरी पोज़िशन); मुँह में कुछ न डालें; 108 पर तुरंत कॉल करें।")
        actions_pa.append("ਮਰੀਜ਼ ਨੂੰ ਪਾਸੇ ਦੇ ਭਾਰ ਲਿਟਾਓ; ਮੂੰਹ ਵਿੱਚ ਕੁਝ ਨਾ ਪਾਓ; 108 'ਤੇ ਤੁਰੰਤ ਕਾਲ ਕਰੋ।")
        teacher_notes_en.append("Teaching Note: In rural seizures, rule out hypoglycemia (fingerprick glucometer) and eclampsia in pregnant females.")
        teacher_notes_hi.append("सीख: ग्रामीण क्षेत्र में दौरे के समय तुरंत ब्लड शुगर (ग्लूकोज) जाँचें और गर्भवती महिलाओं में एक्लम्पसिया की जांच करें।")
        teacher_notes_pa.append("ਸਿੱਖਿਆ: ਦੌਰੇ ਸਮੇਂ ਸ਼ੂਗਰ (ਗਲੂਕੋਜ਼) ਤੁਰੰਤ ਚੈੱਕ ਕਰੋ ਅਤੇ ਗਰਭਵਤੀ ਔਰਤਾਂ ਵਿੱਚ ਐਕਲੈਂਪਸੀਆ ਦੀ ਜਾਂਚ ਕਰੋ।")

    if "Heavy bleeding" in sym_set:
        is_emergency = True
        reasons_en.append("Active heavy hemorrhage (Hypovolemic shock hazard)")
        reasons_hi.append("भारी रक्तस्राव (रक्त की कमी से शॉक का खतरा)")
        reasons_pa.append("ਭਾਰੀ ਖੂਨ ਵਗਣਾ (ਖੂਨ ਦੀ ਕਮੀ ਨਾਲ ਸਦਮੇ ਦਾ ਖ਼ਤਰਾ)")
        actions_en.append("Apply direct firm pressure with clean gauze/cloth; elevate bleeding limb if possible; initiate wide-bore IV line.")
        actions_hi.append("साफ कपड़े या गॉज से सीधा दबाव बनाएं; यदि संभव हो तो अंग को ऊपर उठाएं; आई.वी. लाइन लगाएं।")
        actions_pa.append("ਸਾਫ਼ ਕੱਪੜੇ ਨਾਲ ਸਿੱਧਾ ਦਬਾਅ ਪਾਓ; ਸੰਭਵ ਹੋਵੇ ਤਾਂ ਅੰਗ ਉੱਚਾ ਰੱਖੋ; ਤੁਰੰਤ ਡਾਕਟਰੀ ਸਹਾਇਤਾ ਲਵੋ।")
        teacher_notes_en.append("Teaching Note: Direct pressure stops >90% of external bleeds. Avoid removing soaked dressings; pack more layers on top.")
        teacher_notes_hi.append("सीख: सीधा दबाव 90% से अधिक रक्तस्राव रोकता है। भीगे कपड़े को न हटाएं, ऊपर से और कपड़ा लगाएं।")
        teacher_notes_pa.append("ਸਿੱਖਿਆ: ਸਿੱਧਾ ਦਬਾਅ 90% ਤੋਂ ਵੱਧ ਖੂਨ ਰੋਕਦਾ ਹੈ। ਭਿੱਜੇ ਕੱਪੜੇ ਨੂੰ ਨਾ ਹਟਾਓ, ਉੱਪਰ ਹੋਰ ਕੱਪੜਾ ਰੱਖੋ।")

    if spo2 < 90:
        is_emergency = True
        reasons_en.append(f"Severe hypoxemia (SpO2 {spo2}% < 90%)")
        reasons_hi.append(f"गंभीर ऑक्सीजन की कमी (SpO2 {spo2}% < 90%)")
        reasons_pa.append(f"ਆਕਸੀਜਨ ਦੀ ਭਾਰੀ ਘਾਟ (SpO2 {spo2}% < 90%)")
        actions_en.append("Start high-flow supplemental oxygen (4-6 L/min via nasal cannula or mask) immediately.")
        actions_hi.append("तुरंत 4-6 लीटर/मिनट ऑक्सीजन मास्क या नेज़ल कैनुला से शुरू करें।")
        actions_pa.append("ਤੁਰੰਤ 4-6 ਲੀਟਰ/ਮਿੰਟ ਆਕਸੀਜਨ ਮਾਸਕ ਰਾਹੀਂ ਸ਼ੁਰੂ ਕਰੋ।")
        teacher_notes_en.append("Teaching Note: Tissue hypoxia sets in rapidly below 90%. Keep the patient sitting upright (orthopneic position) to maximize lung volume.")
        teacher_notes_hi.append("सीख: 90% से नीचे ऊतकों को नुकसान होता है। फेफड़ों को पूरा विस्तार देने के लिए मरीज़ को सीधा बैठाएं।")
        teacher_notes_pa.append("ਸਿੱਖਿਆ: 90% ਤੋਂ ਹੇਠਾਂ ਫੇਫੜਿਆਂ ਨੂੰ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ। ਮਰੀਜ਼ ਨੂੰ ਸਿੱਧਾ ਬਿਠਾਓ ਤਾਂ ਜੋ ਸਾਹ ਸੌਖਾ ਆਵੇ।")

    if "Chest pain" in sym_set and (spo2 < 94 or sbp >= 160 or sbp < 90 or pulse > 105 or age > 45):
        is_emergency = True
        reasons_en.append(f"Acute Chest Pain with cardiovascular risk markers (Age {age}, SBP {sbp}, SpO2 {spo2}%)")
        reasons_hi.append(f"सीने में दर्द के साथ हृदय संबंधी जोखिम संकेत (आयु {age}, बीपी {sbp}, ऑक्सीजन {spo2}%)")
        reasons_pa.append(f"ਛਾਤੀ ਵਿੱਚ ਦਰਦ ਦੇ ਨਾਲ ਦਿਲ ਦੇ ਖ਼ਤਰੇ ਦੇ ਸੰਕੇਤ (ਉਮਰ {age}, ਬੀ.ਪੀ. {sbp}, ਆਕਸੀਜਨ {spo2}%)")
        actions_en.append("Perform urgent 12-lead ECG; keep patient at complete bed rest; give chewable Aspirin 300mg + Sorbitrate (if SBP > 100); prepare transfer.")
        actions_hi.append("तत्काल ईसीजी (ECG) करें; मरीज़ को पूरा आराम दें; एस्पिरिन 300mg चबाने को दें; उच्च केंद्र रेफर करें।")
        actions_pa.append("ਤੁਰੰਤ ਈ.ਸੀ.ਜੀ. (ECG) ਕਰੋ; ਮਰੀਜ਼ ਨੂੰ ਪੂਰਾ ਆਰਾਮ ਦਿਓ; ਐਸਪਰੀਨ 300mg ਚਬਾਉਣ ਲਈ ਦਿਓ; ਵੱਡੇ ਹਸਪਤਾਲ ਰੈਫਰ ਕਰੋ।")
        teacher_notes_en.append("Teaching Note: In rural settings, radiating chest pain to left arm or jaw in adults is Acute Coronary Syndrome until proven otherwise.")
        teacher_notes_hi.append("सीख: बाएं हाथ या जबड़े तक फैलने वाला दर्द दिल के दौरे का प्रमुख लक्षण है। देरी न करें।")
        teacher_notes_pa.append("ਸਿੱਖਿਆ: ਖੱਬੇ ਹੱਥ ਜਾਂ ਜਬਾੜੇ ਤੱਕ ਜਾਣ ਵਾਲਾ ਦਰਦ ਦਿਲ ਦੇ ਦੌਰੇ ਦਾ ਮੁੱਖ ਲੱਛਣ ਹੈ। ਤੁਰੰਤ ਕਦਮ ਚੁੱਕੋ।")

    if "Breathlessness" in sym_set and (spo2 <= 92 or pulse > 120 or temp >= 38.8):
        is_emergency = True
        reasons_en.append("Respiratory distress with vital decompensation")
        reasons_hi.append("गंभीर सांस की तकलीफ और असामान्य जीवन संकेत")
        reasons_pa.append("ਸਾਹ ਲੈਣ ਵਿੱਚ ਭਾਰੀ ਔਖ ਅਤੇ ਗੰਭੀਰ ਸੰਕੇਤ")
        actions_en.append("Administer nebulization (Salbutamol) if wheezing present; position upright; monitor continuous pulse oximetry.")
        actions_hi.append("यदि घरघराहट हो तो नेबुलाइज़र दें; मरीज़ को सीधा बैठाएं; ऑक्सीजन की लगातार निगरानी करें।")
        actions_pa.append("ਨੇਬੂਲਾਈਜ਼ਰ ਦਿਓ; ਮਰੀਜ਼ ਨੂੰ ਸਿੱਧਾ ਬਿਠਾਓ; ਆਕਸੀਜਨ ਦੀ ਲਗਾਤਾਰ ਜਾਂਚ ਕਰੋ।")

    if sbp >= 190 or (sbp >= 170 and "Headache" in sym_set):
        is_emergency = True
        reasons_en.append(f"Hypertensive crisis (SBP {sbp} mmHg) with organ symptom risk")
        reasons_hi.append(f"अत्यधिक उच्च रक्तचाप (SBP {sbp} mmHg) और सिरदर्द")
        reasons_pa.append(f"ਬਹੁਤ ਜ਼ਿਆਦਾ ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ (SBP {sbp} mmHg) ਅਤੇ ਸਿਰ ਦਰਦ")
        actions_en.append("Administer antihypertensive protocol as per medical officer; rest in quiet room; screen for stroke/neurologic deficit.")
        actions_hi.append("शांत कमरे में आराम कराएं; डॉक्टर के निर्देशानुसार बीपी की दवा दें; स्ट्रोक के लक्षणों की जांच करें।")
        actions_pa.append("ਸ਼ਾਂਤ ਕਮਰੇ ਵਿੱਚ ਆਰਾਮ ਦਿਓ; ਡਾਕਟਰ ਅਨੁਸਾਰ ਦਵਾਈ ਦਿਓ; ਲਕਵੇ (ਸਟ੍ਰੋਕ) ਦੇ ਲੱਛਣ ਚੈੱਕ ਕਰੋ।")

    # Pediatric Emergency Rule
    if age <= 2 and (temp >= 39.0 or spo2 < 93 or pulse > 160):
        is_emergency = True
        reasons_en.append(f"Pediatric red flag in infant (Age {age} yr, Temp {temp}°C, SpO2 {spo2}%)")
        reasons_hi.append(f"शिशु में आपातकालीन बाल स्वास्थ्य संकेत (आयु {age} वर्ष, तापमान {temp}°C)")
        reasons_pa.append(f"ਛੋਟੇ ਬੱਚੇ ਵਿੱਚ ਐਮਰਜੈਂਸੀ ਚੇਤਾਵਨੀ (ਉਮਰ {age} ਸਾਲ, ਤਾਪਮਾਨ {temp}°C)")
        actions_en.append("Immediate warm transport to pediatric facility; skin-to-skin or warm wrap; keep airway clear; assess hydration.")
        actions_hi.append("शिशु को गर्म रखें; तुरंत बाल रोग विशेषज्ञ के पास रेफर करें; स्तनपान या ओआरएस जारी रखें।")
        actions_pa.append("ਬੱਚੇ ਨੂੰ ਗਰਮ ਰੱਖੋ; ਤੁਰੰਤ ਬਾਲ ਰੋਗ ਮਾਹਿਰ ਕੋਲ ਭੇਜੋ; ਮਾਂ ਦਾ ਦੁੱਧ ਜਾਂ ਓ.ਆਰ.ਐੱਸ. ਜਾਰੀ ਰੱਖੋ।")
        teacher_notes_en.append("Teaching Note: Infants decompensate much faster than adults. Hypothermia or lethargy in febrile infants is critical.")
        teacher_notes_hi.append("सीख: छोटे बच्चे बड़ों की तुलना में बहुत जल्दी गंभीर स्थिति में पहुँच जाते हैं। सुस्ती को नज़रअंदाज़ न करें।")
        teacher_notes_pa.append("ਸਿੱਖਿਆ: ਛੋਟੇ ਬੱਚੇ ਬਹੁਤ ਤੇਜ਼ੀ ਨਾਲ ਬਿਮਾਰ ਹੁੰਦੇ ਹਨ। ਸੁਸਤੀ ਜਾਂ ਠੰਡੇ ਪੈਣ ਨੂੰ ਗੰਭੀਰਤਾ ਨਾਲ ਲਵੋ।")

    # --- 2. URGENT SIGNS (Priority Yellow) ---
    if not is_emergency:
        if temp >= 38.5:
            is_urgent = True
            reasons_en.append(f"High pyrexia / fever ({temp}°C)")
            reasons_hi.append(f"तेज़ बुखार ({temp}°C)")
            reasons_pa.append(f"ਤੇਜ਼ ਬੁਖ਼ਾਰ ({temp}°C)")
            actions_en.append("Cold sponging with tap water; Paracetamol dose according to body weight; test for malaria / dengue if endemic.")
            actions_hi.append("सामान्य पानी की पट्टी रखें; वज़न अनुसार पैरासिटामोल दें; मलेरिया/डेंगू की जांच कराएं।")
            actions_pa.append("ਮੱਥੇ 'ਤੇ ਗਿੱਲੀਆਂ ਪੱਟੀਆਂ ਰੱਖੋ; ਵਜ਼ਨ ਮੁਤਾਬਕ ਪੈਰਾਸੀਟਾਮੋਲ ਦਿਓ; ਮਲੇਰੀਆ/ਡੇਂਗੂ ਟੈਸਟ ਕਰਵਾਓ।")
            teacher_notes_en.append("Teaching Note: Always use lukewarm or tap water for sponging. Never use ice water, which causes vasoconstriction and shivering.")
            teacher_notes_hi.append("सीख: कभी भी बर्फ के पानी से पट्टी न करें, केवल सामान्य नल के पानी का उपयोग करें ताकि कंपकंपी न छूटे।")
            teacher_notes_pa.append("ਸਿੱਖਿਆ: ਬਰਫ਼ ਵਾਲੇ ਪਾਣੀ ਨਾਲ ਕਦੇ ਵੀ ਪੱਟੀਆਂ ਨਾ ਕਰੋ, ਆਮ ਪਾਣੀ ਵਰਤੋ ਤਾਂ ਜੋ ਕਾਂਬਾ ਨਾ ਛਿੜੇ।")

        if sbp >= 160 or dbp >= 100:
            is_urgent = True
            reasons_en.append(f"Stage 2 Hypertension (BP {sbp}/{dbp} mmHg)")
            reasons_hi.append(f"उच्च रक्तचाप (बीपी {sbp}/{dbp} mmHg)")
            reasons_pa.append(f"ਹਾਈ ਬਲੱਡ ਪ੍ਰੈਸ਼ਰ (ਬੀ.ਪੀ. {sbp}/{dbp} mmHg)")
            actions_en.append("Repeat BP measurement after 15 mins of quiet rest; review adherence to anti-hypertensives; schedule medical review.")
            actions_hi.append("15 मिनट आराम के बाद दोबारा बीपी नापें; नियमित दवाओं की समीक्षा करें।")
            actions_pa.append("15 ਮਿੰਟ ਆਰਾਮ ਤੋਂ ਬਾਅਦ ਮੁੜ ਬੀ.ਪੀ. ਚੈੱਕ ਕਰੋ; ਰੋਜ਼ਾਨਾ ਦਵਾਈਆਂ ਦੀ ਜਾਂਚ ਕਰੋ।")

        if spo2 <= 94 and spo2 >= 90:
            is_urgent = True
            reasons_en.append(f"Mild-to-moderate hypoxemia (SpO2 {spo2}%)")
            reasons_hi.append(f"हल्की से मध्यम ऑक्सीजन की कमी (SpO2 {spo2}%)")
            reasons_pa.append(f"ਆਕਸੀਜਨ ਦੀ ਹਲਕੀ ਘਾਟ (SpO2 {spo2}%)")
            actions_en.append("Keep patient resting comfortably; re-check probe on warm finger; prepare low-flow O2 if dyspneic.")
            actions_hi.append("मरीज़ को आराम दें; उंगली गर्म करके दोबारा प्रोब लगाएं; ज़रूरत पड़ने पर ऑक्सीजन दें।")
            actions_pa.append("ਮਰੀਜ਼ ਨੂੰ ਆਰਾਮ ਨਾਲ ਬਿਠਾਓ; ਉਂਗਲ ਸਾਫ਼ ਕਰਕੇ ਮੁੜ ਚੈੱਕ ਕਰੋ; ਲੋੜ ਪੈਣ 'ਤੇ ਆਕਸੀਜਨ ਦਿਓ।")

        if "Vomiting" in sym_set and ("Fever" in sym_set or pulse > 100):
            is_urgent = True
            reasons_en.append("Persistent vomiting with signs of early dehydration")
            reasons_hi.append("उल्टी के साथ निर्जलीकरण (डिहाइड्रेशन) के प्रारंभिक लक्षण")
            reasons_pa.append("ਉਲਟੀਆਂ ਦੇ ਨਾਲ ਸਰੀਰ ਵਿੱਚ ਪਾਣੀ ਦੀ ਘਾਟ ਦੇ ਸੰਕੇਤ")
            actions_en.append("Administer slow sips of Oral Rehydration Solution (ORS); anti-emetic per medical standing order.")
            actions_hi.append("घूंट-घूंट करके ओआरएस (ORS) पिलाएं; डॉक्टर की सलाह से उल्टी रोकने की दवा दें।")
            actions_pa.append("ਹੌਲੀ-ਹੌਲੀ ਓ.ਆਰ.ਐੱਸ. (ORS) ਘੋਲ ਪਿਲਾਓ; ਡਾਕਟਰ ਦੀ ਸਲਾਹ ਨਾਲ ਦਵਾਈ ਦਿਓ।")

        if "Chest pain" in sym_set and not is_emergency:
            is_urgent = True
            reasons_en.append("Undifferentiated chest pain (requires clinical ECG triage)")
            reasons_hi.append("सीने में दर्द (ईसीजी और डॉक्टर की जांच आवश्यक)")
            reasons_pa.append("ਛਾਤੀ ਵਿੱਚ ਦਰਦ (ਈ.ਸੀ.ਜੀ. ਅਤੇ ਡਾਕਟਰੀ ਜਾਂਚ ਲਾਜ਼ਮੀ)")
            actions_en.append("Keep patient at rest; record resting ECG; doctor evaluation within 30 minutes.")
            actions_hi.append("मरीज़ को आराम कराएं; ईसीजी करें; 30 मिनट में डॉक्टर को दिखाएं।")
            actions_pa.append("ਮਰੀਜ਼ ਨੂੰ ਆਰਾਮ ਦਿਓ; ਈ.ਸੀ.ਜੀ. ਕਰੋ; 30 ਮਿੰਟ ਵਿੱਚ ਡਾਕਟਰ ਨੂੰ ਦਿਖਾਓ।")

        if "Breathlessness" in sym_set and not is_emergency:
            is_urgent = True
            reasons_en.append("Exertional or acute shortness of breath (Needs auscultation)")
            reasons_hi.append("सांस फूलने की शिकायत (स्टेथोस्कोप से फेफड़ों की जांच जरूरी)")
            reasons_pa.append("ਸਾਹ ਚੜ੍ਹਨ ਦੀ ਸ਼ਿਕਾਇਤ (ਫੇਫੜਿਆਂ ਦੀ ਡਾਕਟਰੀ ਜਾਂਚ ਜ਼ਰੂਰੀ)")
            actions_en.append("Assess respiratory rate; auscultate for wheeze/crackles; consider bronchodilator puff.")
            actions_hi.append("श्वसन दर (सांस की गति) नापें; सीने की आवाज़ सुनें; इनहेलर की आवश्यकता देखें।")
            actions_pa.append("ਸਾਹ ਦੀ ਗਤੀ ਚੈੱਕ ਕਰੋ; ਸੀਨੇ ਦੀ ਜਾਂਚ ਕਰੋ; ਇਨਹੇਲਰ ਦੀ ਲੋੜ ਵੇਖੋ।")

    # --- 3. FINAL DETERMINATION ---
    if is_emergency:
        priority = "Emergency"
    elif is_urgent:
        priority = "Urgent"
    else:
        priority = "Routine"
        reasons_en.append("Stable vital signs; no immediate red flags identified; routine outpatient consultation")
        reasons_hi.append("सभी जीवन संकेत सामान्य हैं; कोई गंभीर खतरा नहीं; नियमित ओपीडी परामर्श")
        reasons_pa.append("ਸਾਰੇ ਜੀਵਨ ਸੰਕੇਤ ਆਮ ਹਨ; ਕੋਈ ਖ਼ਤਰਨਾਕ ਲੱਛਣ ਨਹੀਂ; ਆਮ ਓ.ਪੀ.ਡੀ. ਜਾਂਚ")
        actions_en.append("General OPD consultation; symptomatic home remedies; advise immediate return if breathing difficulty or high fever develops.")
        actions_hi.append("सामान्य ओपीडी पर्ची बनाएं; घरेलू देखभाल बताएं; सांस फूलने या तेज़ बुखार होने पर तुरंत वापस आने की सलाह दें।")
        actions_pa.append("ਆਮ ਓ.ਪੀ.ਡੀ. ਜਾਂਚ ਕਰਵਾਓ; ਘਰੇਲੂ ਦੇਖਭਾਲ ਦੱਸੋ; ਤਕਲੀਫ਼ ਵਧਣ 'ਤੇ ਤੁਰੰਤ ਵਾਪਸ ਆਉਣ ਦੀ ਸਲਾਹ ਦਿਓ।")
        teacher_notes_en.append("Teaching Note: In routine rural cases, always reinforce preventive health, hygiene, and danger-sign counseling.")
        teacher_notes_hi.append("सीख: सामान्य मरीज़ों को भी खतरे के लक्षण समझाएं ताकि स्थिति बिगड़ने पर वे समय पर अस्पताल आ सकें।")
        teacher_notes_pa.append("ਸਿੱਖਿਆ: ਆਮ ਮਰੀਜ਼ਾਂ ਨੂੰ ਵੀ ਖ਼ਤਰੇ ਦੇ ਸੰਕੇਤ ਸਮਝਾਓ ਤਾਂ ਜੋ ਲੋੜ ਪੈਣ 'ਤੇ ਉਹ ਸਮੇਂ ਸਿਰ ਹਸਪਤਾਲ ਪਹੁੰਚ ਸਕਣ।")

    return {
        "priority": priority,
        "reasons": "; ".join(reasons_en),
        "reasons_hi": " • ".join(reasons_hi),
        "reasons_pa": " • ".join(reasons_pa),
        "actions": "; ".join(actions_en),
        "actions_hi": " • ".join(actions_hi),
        "actions_pa": " • ".join(actions_pa),
        "teacher_notes": " ".join(teacher_notes_en) if teacher_notes_en else "Clinical Teaching: Always record baseline vitals before administering any medication.",
        "teacher_notes_hi": " ".join(teacher_notes_hi) if teacher_notes_hi else "नैदानिक सीख: कोई भी दवा देने से पहले हमेशा मरीज़ के बीपी, पल्स और ऑक्सीजन को नोट करें।",
        "teacher_notes_pa": " ".join(teacher_notes_pa) if teacher_notes_pa else "ਕਲੀਨਿਕਲ ਸਿੱਖਿਆ: ਕੋਈ ਵੀ ਦਵਾਈ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ ਮਰੀਜ਼ ਦੇ ਬੀ.ਪੀ., ਨਬਜ਼ ਅਤੇ ਆਕਸੀਜਨ ਦੀ ਜਾਂਚ ਜ਼ਰੂਰ ਕਰੋ।",
        "vitals_status": vitals_status
    }
