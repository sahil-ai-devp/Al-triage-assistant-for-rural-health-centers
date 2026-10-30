# Multilingual dictionary & Clinical Teacher Knowledge Base for English, Hindi, and Punjabi

LANGS = {
    "en": "English",
    "hi": "हिन्दी (Hindi)",
    "pa": "ਪੰਜਾਬੀ (Punjabi)"
}

# UI Labels across all 3 languages
UI = {
    "en": {
        "app_title": "Rural PHC AI Triage & Clinical Mentor",
        "app_subtitle": "Intelligent Frontline Decision Support for Rural Health Centres & ASHA Workers",
        "badge_tag": "CT Group CSE / AI-ML Portfolio",
        "nav_triage": "🩺 Triage Desk",
        "nav_teacher": "🎓 Clinical Teacher & Quiz",
        "nav_protocols": "📋 Rural Emergency Protocols",
        "assessment_title": "Patient Vital Signs & Triage Intake",
        "quick_presets": "⚡ Quick Test Scenarios:",
        "preset_emergency": "Adult Heart Attack",
        "preset_infant": "Infant High Fever",
        "preset_routine": "Routine Cough",
        "preset_trauma": "Bleeding Trauma",
        "lbl_name": "Patient Full Name",
        "ph_name": "e.g. Jaswinder Singh",
        "lbl_age": "Age (Years)",
        "lbl_gender": "Gender",
        "g_male": "Male",
        "g_female": "Female",
        "g_other": "Other",
        "lbl_temp": "Temperature (°C)",
        "lbl_sbp": "Systolic BP (mmHg)",
        "lbl_dbp": "Diastolic BP (mmHg)",
        "lbl_spo2": "SpO2 Saturation (%)",
        "lbl_pulse": "Pulse / Heart Rate (bpm)",
        "lbl_symptoms": "Reported Symptoms & Red Flags",
        "voice_mic_btn": "🎙️ Voice Input (Speak Symptoms)",
        "voice_listening": "Listening... Speak symptoms in English, Hindi, or Punjabi",
        "consent_text": "Informed Consent: Patient / Attendant agrees to local digital health assessment.",
        "btn_assess": "Analyze & Determine Triage Priority",
        "btn_reset": "Clear Form",
        "result_header": "Clinical Triage Assessment Result",
        "badge_emergency": "EMERGENCY - RED (Immediate 0 min)",
        "badge_urgent": "URGENT - YELLOW (Within 15-30 min)",
        "badge_routine": "ROUTINE - GREEN (Standard OPD)",
        "btn_listen_tts": "🔊 Read Aloud (Voice)",
        "tts_speaking": "Playing clinical audio...",
        "lbl_why": "Clinical Reasoning (Why this priority?):",
        "lbl_action_protocol": "Immediate Emergency Action Protocol:",
        "lbl_teacher_insight": "🎓 Clinical Teacher's Educational Note:",
        "btn_print_slip": "🖨️ Print Clinical Referral Slip",
        "btn_whatsapp_sos": "🚨 WhatsApp Emergency SOS to 108/Doctor",
        "queue_title": "Live Patient Queue (Sorted by Medical Urgency)",
        "stat_emergency": "Emergency",
        "stat_urgent": "Urgent",
        "stat_routine": "Routine",
        "stat_pending": "Pending Cloud Sync",
        "filter_all": "All Patients",
        "search_ph": "Search patient by name or symptom...",
        "col_id": "Token #",
        "col_name": "Patient",
        "col_vitals": "Vitals Summary",
        "col_priority": "Triage Priority",
        "col_reasons": "Clinical Rationale",
        "col_time": "Intake Time",
        "col_actions": "Actions",
        "btn_sync": "☁️ Sync to District Central Server",
        "btn_delete": "Delete",
        "btn_view_slip": "Referral Slip",
        "no_patients": "No patients currently in queue. Add a patient above to test.",
        "footer_text": "Designed for Primary Health Centres (PHC) & Health and Wellness Centres (Ayushman Arogya Mandir). Always consult a licensed Medical Officer.",
        "offline_badge": "🟢 Offline-First Active (Local SQLite)",
        "sync_success": "All pending records successfully synchronized with district registry!"
    },
    "hi": {
        "app_title": "ग्रामीण PHC एआई ट्राइएज एवं क्लिनिकल शिक्षक",
        "app_subtitle": "ग्रामीण स्वास्थ्य केंद्रों और आशा कार्यकर्ताओं के लिए त्वरित जीवन रक्षक निर्णय प्रणाली",
        "badge_tag": "सीटी ग्रुप सीएसई / एआई-एमएल पोर्टफोलियो",
        "nav_triage": "🩺 ट्राइएज डेस्क",
        "nav_teacher": "🎓 क्लिनिकल शिक्षक एवं क्विज़",
        "nav_protocols": "📋 ग्रामीण आपातकालीन प्रोटोकॉल",
        "assessment_title": "मरीज़ के जीवन संकेत एवं लक्षण जांच",
        "quick_presets": "⚡ त्वरित परीक्षण परिदृश्य:",
        "preset_emergency": "सीने का दर्द (हार्ट अटैक)",
        "preset_infant": "शिशु को तेज़ बुखार",
        "preset_routine": "सामान्य खांसी-जुकाम",
        "preset_trauma": "गंभीर रक्तस्राव",
        "lbl_name": "मरीज़ का पूरा नाम",
        "ph_name": "जैसे: जसविंदर सिंह",
        "lbl_age": "उम्र (वर्ष)",
        "lbl_gender": "लिंग",
        "g_male": "पुरुष",
        "g_female": "महिला",
        "g_other": "अन्य",
        "lbl_temp": "तापमान (°C)",
        "lbl_sbp": "ऊपरी बीपी - Systolic (mmHg)",
        "lbl_dbp": "निचला बीपी - Diastolic (mmHg)",
        "lbl_spo2": "ऑक्सीजन SpO2 (%)",
        "lbl_pulse": "नाड़ी की गति - Pulse (bpm)",
        "lbl_symptoms": "मरीज़ के लक्षण एवं खतरे के संकेत",
        "voice_mic_btn": "🎙️ बोलकर लक्षण बताएं (Voice Input)",
        "voice_listening": "सुन रहे हैं... हिंदी, पंजाबी या अंग्रेजी में लक्षण बोलें",
        "consent_text": "सहमति: मरीज़ या परिजन डिजिटल जांच और डेटा सहेजने के लिए सहमत हैं।",
        "btn_assess": "जांच करें और प्राथमिकता तय करें",
        "btn_reset": "फॉर्म रीसेट करें",
        "result_header": "क्लिनिकल ट्राइएज जांच परिणाम",
        "badge_emergency": "आपातकाल - लाल (तत्काल 0 मिनट)",
        "badge_urgent": "अति-आवश्यक - पीला (15-30 मिनट में)",
        "badge_routine": "सामान्य - हरा (नियमित ओपीडी)",
        "btn_listen_tts": "🔊 आवाज़ में सुनें (Voice)",
        "tts_speaking": "ऑडियो बजाया जा रहा है...",
        "lbl_why": "क्लिनिकल कारण (यह प्राथमिकता क्यों चुनी गई?):",
        "lbl_action_protocol": "तत्काल आपातकालीन प्राथमिक उपचार (First Aid):",
        "lbl_teacher_insight": "🎓 क्लिनिकल शिक्षक की सीख (शैक्षणिक बिंदु):",
        "btn_print_slip": "🖨️ रेफरल पर्ची प्रिंट करें",
        "btn_whatsapp_sos": "🚨 108 / डॉक्टर को WhatsApp SOS भेजें",
        "queue_title": "मरीज़ों की लाइव कतार (चिकित्सा प्राथमिकता अनुसार क्रमबद्ध)",
        "stat_emergency": "आपातकाल",
        "stat_urgent": "अति-आवश्यक",
        "stat_routine": "सामान्य",
        "stat_pending": "सिंक बाकी",
        "filter_all": "सभी मरीज़",
        "search_ph": "नाम या लक्षण द्वारा मरीज़ खोजें...",
        "col_id": "टोकन #",
        "col_name": "मरीज़",
        "col_vitals": "जीवन संकेत",
        "col_priority": "प्राथमिकता",
        "col_reasons": "कारण",
        "col_time": "समय",
        "col_actions": "कार्रवाई",
        "btn_sync": "☁️ जिला मुख्य सर्वर से सिंक करें",
        "btn_delete": "हटाएं",
        "btn_view_slip": "रेफरल पर्ची",
        "no_patients": "वर्तमान में कोई मरीज़ कतार में नहीं है। ऊपर फॉर्म भरकर जांच करें।",
        "footer_text": "प्राथमिक स्वास्थ्य केंद्र (PHC) और आयुष्मान आरोग्य मंदिर के लिए तैयार। आपात स्थिति में तुरंत डॉक्टर की सलाह लें।",
        "offline_badge": "🟢 ऑफलाइन सुरक्षित (स्थानीय SQLite डेटाबेस)",
        "sync_success": "सभी शेष मरीज़ों का डेटा सफलतापूर्वक जिला रजिस्ट्री से सिंक हो गया!"
    },
    "pa": {
        "app_title": "ਪੇਂਡੂ PHC ਏ.ਆਈ. ਟ੍ਰਾਇਏਜ ਅਤੇ ਕਲੀਨਿਕਲ ਅਧਿਆਪਕ",
        "app_subtitle": "ਪੇਂਡੂ ਸਿਹਤ ਕੇਂਦਰਾਂ ਅਤੇ ਆਸ਼ਾ ਵਰਕਰਾਂ ਲਈ ਜੀਵਨ-ਰੱਖਿਅਕ ਕਲੀਨਿਕਲ ਸਹਾਇਕ ਪ੍ਰਣਾਲੀ",
        "badge_tag": "ਸੀ.ਟੀ. ਗਰੁੱਪ ਸੀ.ਐੱਸ.ਈ. / ਏ.ਆਈ.-ਐੱਮ.ਐੱਲ. ਪੋਰਟਫੋਲੀਓ",
        "nav_triage": "🩺 ਟ੍ਰਾਇਏਜ ਡੈਸਕ",
        "nav_teacher": "🎓 ਕਲੀਨਿਕਲ ਸਿੱਖਿਅਕ ਅਤੇ ਕੁਇਜ਼",
        "nav_protocols": "📋 ਪੇਂਡੂ ਐਮਰਜੈਂਸੀ ਪ੍ਰੋਟੋਕੋਲ",
        "assessment_title": "ਮਰੀਜ਼ ਦੇ ਜੀਵਨ ਸੰਕੇਤ ਅਤੇ ਲੱਛਣਾਂ ਦੀ ਜਾਂਚ",
        "quick_presets": "⚡ ਤੁਰੰਤ ਟੈਸਟ ਕੇਸ:",
        "preset_emergency": "ਛਾਤੀ ਵਿੱਚ ਦਰਦ (ਦਿਲ ਦਾ ਦੌਰਾ)",
        "preset_infant": "ਛੋਟੇ ਬੱਚੇ ਨੂੰ ਤੇਜ਼ ਬੁਖ਼ਾਰ",
        "preset_routine": "ਆਮ ਖੰਘ-ਜ਼ੁਕਾਮ",
        "preset_trauma": "ਗੰਭੀਰ ਖੂਨ ਵਗਣਾ",
        "lbl_name": "ਮਰੀਜ਼ ਦਾ ਪੂਰਾ ਨਾਮ",
        "ph_name": "ਜਿਵੇਂ: ਜਸਵਿੰਦਰ ਸਿੰਘ",
        "lbl_age": "ਉਮਰ (ਸਾਲ)",
        "lbl_gender": "ਲਿੰਗ",
        "g_male": "ਪੁਰਸ਼",
        "g_female": "ਮਹਿਲਾ",
        "g_other": "ਹੋਰ",
        "lbl_temp": "ਤਾਪਮਾਨ (°C)",
        "lbl_sbp": "ਉੱਪਰਲਾ ਬੀ.ਪੀ. - Systolic (mmHg)",
        "lbl_dbp": "ਹੇਠਲਾ ਬੀ.ਪੀ. - Diastolic (mmHg)",
        "lbl_spo2": "ਆਕਸੀਜਨ SpO2 (%)",
        "lbl_pulse": "ਨਬਜ਼ ਦੀ ਗਤੀ - Pulse (bpm)",
        "lbl_symptoms": "ਮਰੀਜ਼ ਦੇ ਲੱਛਣ ਅਤੇ ਖ਼ਤਰੇ ਦੇ ਨਿਸ਼ਾਨ",
        "voice_mic_btn": "🎙️ ਬੋਲ ਕੇ ਲੱਛਣ ਦੱਸੋ (Voice Input)",
        "voice_listening": "ਸੁਣ ਰਹੇ ਹਾਂ... ਪੰਜਾਬੀ, ਹਿੰਦੀ ਜਾਂ ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਲੱਛਣ ਬੋਲੋ",
        "consent_text": "ਸਹਿਮਤੀ: ਮਰੀਜ਼ ਜਾਂ ਪਰਿਵਾਰ ਡਿਜੀਟਲ ਜਾਂਚ ਅਤੇ ਡੇਟਾ ਸਾਂਭਣ ਲਈ ਸਹਿਮਤ ਹੈ।",
        "btn_assess": "ਜਾਂਚ ਕਰੋ ਅਤੇ ਤਰਜੀਹ ਤੈਅ ਕਰੋ",
        "btn_reset": "ਫਾਰਮ ਸਾਫ਼ ਕਰੋ",
        "result_header": "ਕਲੀਨਿਕਲ ਟ੍ਰਾਇਏਜ ਜਾਂਚ ਨਤੀਜਾ",
        "badge_emergency": "ਐਮਰਜੈਂਸੀ - ਲਾਲ (ਤੁਰੰਤ 0 ਮਿੰਟ)",
        "badge_urgent": "ਜ਼ਰੂਰੀ - ਪੀਲਾ (15-30 ਮਿੰਟ ਅੰਦਰ)",
        "badge_routine": "ਆਮ - ਹਰਾ (ਆਮ ਓ.ਪੀ.ਡੀ.)",
        "btn_listen_tts": "🔊 ਆਵਾਜ਼ ਵਿੱਚ ਸੁਣੋ (Voice)",
        "tts_speaking": "ਆਡੀਓ ਚਲ ਰਿਹਾ ਹੈ...",
        "lbl_why": "ਕਲੀਨਿਕਲ ਕਾਰਨ (ਇਹ ਤਰਜੀਹ ਕਿਉਂ ਚੁਣੀ ਗਈ?):",
        "lbl_action_protocol": "ਤੁਰੰਤ ਐਮਰਜੈਂਸੀ ਮੁੱਢਲੀ ਸਹਾਇਤਾ (First Aid):",
        "lbl_teacher_insight": "🎓 ਕਲੀਨਿਕਲ ਅਧਿਆਪਕ ਦੀ ਸਿੱਖਿਆ (ਮਹੱਤਵਪੂਰਨ ਨੁਕਤਾ):",
        "btn_print_slip": "🖨️ ਰੈਫਰਲ ਪਰਚੀ ਪ੍ਰਿੰਟ ਕਰੋ",
        "btn_whatsapp_sos": "🚨 108 / ਡਾਕਟਰ ਨੂੰ WhatsApp SOS ਭੇਜੋ",
        "queue_title": "ਮਰੀਜ਼ਾਂ ਦੀ ਲਾਈਵ ਕਤਾਰ (ਮੈਡੀਕਲ ਤਰਜੀਹ ਮੁਤਾਬਕ ਲੜੀਬੱਧ)",
        "stat_emergency": "ਐਮਰਜੈਂਸੀ",
        "stat_urgent": "ਜ਼ਰੂਰੀ",
        "stat_routine": "ਆਮ",
        "stat_pending": "ਸਿੰਕ ਬਾਕੀ",
        "filter_all": "ਸਾਰੇ ਮਰੀਜ਼",
        "search_ph": "ਨਾਮ ਜਾਂ ਲੱਛਣ ਰਾਹੀਂ ਮਰੀਜ਼ ਲੱਭੋ...",
        "col_id": "ਟੋਕਨ #",
        "col_name": "ਮਰੀਜ਼",
        "col_vitals": "ਜੀਵਨ ਸੰਕੇਤ",
        "col_priority": "ਤਰਜੀਹ",
        "col_reasons": "ਕਾਰਨ",
        "col_time": "ਸਮਾਂ",
        "col_actions": "ਕਾਰਵਾਈ",
        "btn_sync": "☁️ ਜ਼ਿਲ੍ਹਾ ਕੇਂਦਰੀ ਸਰਵਰ ਨਾਲ ਸਿੰਕ ਕਰੋ",
        "btn_delete": "ਮਿਟਾਓ",
        "btn_view_slip": "ਰੈਫਰਲ ਪਰਚੀ",
        "no_patients": "ਇਸ ਸਮੇਂ ਕੋਈ ਮਰੀਜ਼ ਕਤਾਰ ਵਿੱਚ ਨਹੀਂ ਹੈ। ਜਾਂਚ ਲਈ ਉੱਪਰ ਫਾਰਮ ਭਰੋ।",
        "footer_text": "ਪ੍ਰਾਇਮਰੀ ਹੈਲਥ ਸੈਂਟਰ (PHC) ਅਤੇ ਆਯੁਸ਼ਮਾਨ ਅਰੋਗਿਆ ਮੰਦਰ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ। ਹਮੇਸ਼ਾ ਡਾਕਟਰ ਦੀ ਸਲਾਹ ਲਵੋ।",
        "offline_badge": "🟢 ਆਫ਼ਲਾਈਨ ਸੁਰੱਖਿਅਤ (ਸਥਾਨਕ SQLite ਡੇਟਾਬੇਸ)",
        "sync_success": "ਸਾਰੇ ਬਕਾਇਆ ਮਰੀਜ਼ਾਂ ਦਾ ਡੇਟਾ ਜ਼ਿਲ੍ਹਾ ਰਜਿਸਟਰੀ ਨਾਲ ਸਿੰਕ ਹੋ ਗਿਆ ਹੈ!"
    }
}

# Symptoms list with native names and speech recognition keywords
SYMPTOMS = [
    {
        "id": "Chest pain",
        "en": "Chest pain",
        "hi": "सीने में दर्द",
        "pa": "ਛਾਤੀ ਵਿੱਚ ਦਰਦ",
        "icon": "💔",
        "danger": True,
        "keywords": ["chest pain", "chest", "heart", "सीने में दर्द", "छाती में दर्द", "छाती", "ਦਰਦ", "ਛਾਤੀ", "ਛਾਤੀ ਚ ਦਰਦ"]
    },
    {
        "id": "Breathlessness",
        "en": "Breathlessness",
        "hi": "साँस फूलना",
        "pa": "ਸਾਹ ਚੜ੍ਹਨਾ",
        "icon": "🫁",
        "danger": True,
        "keywords": ["breathlessness", "breathing", "short of breath", "सांस", "साँस", "ਦਮ", "ਸਾਹ", "ਸਾਹ ਚੜ੍ਹਨਾ"]
    },
    {
        "id": "Unconscious/seizure",
        "en": "Unconscious / Seizure",
        "hi": "बेहोशी / दौरा",
        "pa": "ਬੇਹੋਸ਼ੀ / ਦੌਰਾ",
        "icon": "⚡",
        "danger": True,
        "keywords": ["unconscious", "faint", "seizure", "fit", "fits", "बेहोश", "दौरा", "बेहोशी", "ਮਿਰਗੀ", "ਦੌਰਾ", "ਬੇਹੋਸ਼"]
    },
    {
        "id": "Heavy bleeding",
        "en": "Heavy bleeding",
        "hi": "भारी रक्तस्राव",
        "pa": "ਭਾਰੀ ਖੂਨ ਵਗਣਾ",
        "icon": "🩸",
        "danger": True,
        "keywords": ["bleeding", "blood", "heavy bleeding", "खून", "रक्त", "ਖੂਨ", "ਲਹੂ"]
    },
    {
        "id": "Fever",
        "en": "High Fever",
        "hi": "तेज़ बुखार",
        "pa": "ਤੇਜ਼ ਬੁਖ਼ਾਰ",
        "icon": "🌡️",
        "danger": False,
        "keywords": ["fever", "pyrexia", "temperature", "बुखार", "ताप", "ਬੁਖਾਰ", "ਤਾਪ"]
    },
    {
        "id": "Vomiting",
        "en": "Vomiting",
        "hi": "उल्टी",
        "pa": "ਉਲਟੀ",
        "icon": "🤢",
        "danger": False,
        "keywords": ["vomit", "vomiting", "nausea", "उल्टी", "जी मिचलाना", "ਉਲਟੀ", "ਕੈਅ"]
    },
    {
        "id": "Headache",
        "en": "Severe Headache",
        "hi": "तेज़ सिरदर्द",
        "pa": "ਤੇਜ਼ ਸਿਰ ਦਰਦ",
        "icon": "🤕",
        "danger": False,
        "keywords": ["headache", "head ache", "सिरदर्द", "सर दर्द", "ਸਿਰ ਦਰਦ"]
    },
    {
        "id": "Cough",
        "en": "Persistent Cough",
        "hi": "लगातार खाँसी",
        "pa": "ਲਗਾਤਾਰ ਖੰਘ",
        "icon": "😷",
        "danger": False,
        "keywords": ["cough", "coughing", "खांसी", "खाँसी", "ਖੰਘ"]
    }
]

# Educational Clinical Cases for Frontline Workers / Students (Interactive Teacher Mode)
TRAINING_CASES = [
    {
        "id": 1,
        "scenario_en": "54-year-old farmer complains of sudden crushing chest pain radiating to his left shoulder, cold sweat, SpO2 89%, BP 170/105, Pulse 115 bpm.",
        "scenario_hi": "54 वर्षीय किसान अचानक सीने में भारी दबाव और बाएं कंधे तक फैलते दर्द की शिकायत करता है, पसीना आ रहा है, ऑक्सीजन 89%, बीपी 170/105, नाड़ी 115 bpm।",
        "scenario_pa": "54 ਸਾਲਾ ਕਿਸਾਨ ਅਚਾਨਕ ਛਾਤੀ ਵਿੱਚ ਭਾਰੀ ਦਬਾਅ ਅਤੇ ਖੱਬੇ ਮੋਢੇ ਤੱਕ ਜਾਂਦੇ ਦਰਦ ਦੀ ਸ਼ਿਕਾਇਤ ਕਰਦਾ ਹੈ, ਪਸੀਨਾ, ਆਕਸੀਜਨ 89%, ਬੀ.ਪੀ. 170/105, ਨਬਜ਼ 115 bpm।",
        "vitals": {"age": 54, "temp": 36.9, "sbp": 170, "spo2": 89, "pulse": 115},
        "correct": "Emergency",
        "explanation_en": "Emergency (Red). The combination of radiating chest pain, severe hypoxemia (SpO2 89%), and sympathetic distress strongly indicates Acute Coronary Syndrome (Myocardial Infarction). Requires immediate oxygen and 108 transfer.",
        "explanation_hi": "आपातकाल (लाल)। सीने का दर्द कंधे तक फैलना, कम ऑक्सीजन (89%) और पसीना हार्ट अटैक (Acute Coronary Syndrome) का स्पष्ट संकेत है। तुरंत ऑक्सीजन लगाएं और 108 एम्बुलेंस बुलाएं।",
        "explanation_pa": "ਐਮਰਜੈਂਸੀ (ਲਾਲ)। ਮੋਢੇ ਤੱਕ ਜਾਂਦਾ ਦਰਦ, ਘੱਟ ਆਕਸੀਜਨ (89%) ਅਤੇ ਪਸੀਨਾ ਦਿਲ ਦੇ ਦੌਰੇ ਦਾ ਪੱਕਾ ਸੰਕੇਤ ਹਨ। ਤੁਰੰਤ ਆਕਸੀਜਨ ਲਗਾਓ ਅਤੇ 108 ਐਂਬੂਲੈਂਸ ਮੰਗਵਾਓ।",
        "key_learning_en": "Remember: Radiating chest pain + hypoxemia is always RED triage. Time to balloon or thrombolysis is crucial.",
        "key_learning_hi": "याद रखें: सीने का दर्द + कम ऑक्सीजन हमेशा लाल (आपातकाल) श्रेणी में आता है। समय ही जीवन है।",
        "key_learning_pa": "ਚੇਤੇ ਰੱਖੋ: ਛਾਤੀ ਵਿੱਚ ਦਰਦ + ਘੱਟ ਆਕਸੀਜਨ ਹਮੇਸ਼ਾ ਲਾਲ (ਐਮਰਜੈਂਸੀ) ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਹੁੰਦੀ ਹੈ। ਸਮੇਂ ਸਿਰ ਇਲਾਜ ਜ਼ਿੰਦਗੀ ਬਚਾਉਂਦਾ ਹੈ।"
    },
    {
        "id": 2,
        "scenario_en": "10-month-old infant brought with high fever of 39.8°C, lethargic, rapid breathing (Pulse 168 bpm, SpO2 91%). Mother says child is not breastfeeding.",
        "scenario_hi": "10 महीने का शिशु 39.8°C तेज़ बुखार के साथ लाया गया, बच्चा सुस्त है, तेज़ सांस ले रहा है (नाड़ी 168 bpm, ऑक्सीजन 91%)। माँ का कहना है कि बच्चा दूध नहीं पी रहा।",
        "scenario_pa": "10 ਮਹੀਨਿਆਂ ਦਾ ਬੱਚਾ 39.8°C ਤੇਜ਼ ਬੁਖ਼ਾਰ ਨਾਲ ਲਿਆਂਦਾ ਗਿਆ, ਬੱਚਾ ਸੁਸਤ ਹੈ, ਤੇਜ਼ ਸਾਹ ਲੈ ਰਿਹਾ ਹੈ (ਨਬਜ਼ 168 bpm, ਆਕਸੀਜਨ 91%)। ਮਾਂ ਕਹਿੰਦੀ ਹੈ ਕਿ ਬੱਚਾ ਦੁੱਧ ਨਹੀਂ ਪੀ ਰਿਹਾ।",
        "vitals": {"age": 1, "temp": 39.8, "sbp": 85, "spo2": 91, "pulse": 168},
        "correct": "Emergency",
        "explanation_en": "Emergency (Red). IMNCI danger signs present: inability to breastfeed, extreme lethargy, high pyrexia, and infant tachycardia (>160 bpm). High risk of sepsis or severe pneumonia.",
        "explanation_hi": "आपातकाल (लाल)। शिशु में स्तनपान न कर पाना और सुस्ती IMNCI के अनुसार गंभीर खतरे के संकेत हैं। सेप्सिस या निमोनिया का भारी जोखिम है।",
        "explanation_pa": "ਐਮਰਜੈਂਸੀ (ਲਾਲ)। ਬੱਚੇ ਦਾ ਦੁੱਧ ਨਾ ਪੀਣਾ ਅਤੇ ਸੁਸਤੀ ਗੰਭੀਰ ਖ਼ਤਰੇ ਦੇ ਨਿਸ਼ਾਨ ਹਨ। ਨਿਮੋਨੀਆ ਜਾਂ ਇਨਫੈਕਸ਼ਨ ਦਾ ਭਾਰੀ ਖ਼ਤਰਾ ਹੈ।",
        "key_learning_en": "Pediatric Rule: Infants who cannot feed or are abnormally sleepy require urgent secondary care referral without delay.",
        "key_learning_hi": "बाल स्वास्थ्य नियम: दूध न पी सकने वाले या अत्यधिक सुस्त शिशु को तुरंत बड़े अस्पताल रेफर करना अनिवार्य है।",
        "key_learning_pa": "ਬਾਲ ਸਿਹਤ ਨਿਯਮ: ਜਿਹੜਾ ਬੱਚਾ ਦੁੱਧ ਨਾ ਪੀਵੇ ਜਾਂ ਬਹੁਤ ਸੁਸਤ ਹੋਵੇ, ਉਸਨੂੰ ਤੁਰੰਤ ਵੱਡੇ ਹਸਪਤਾਲ ਭੇਜਣਾ ਜ਼ਰੂਰੀ ਹੈ।"
    },
    {
        "id": 3,
        "scenario_en": "28-year-old woman has had 6 episodes of vomiting since morning, mild headache, Temp 38.6°C, BP 105/70, Pulse 108 bpm, SpO2 97%. Alert and oriented.",
        "scenario_hi": "28 वर्षीय महिला को सुबह से 6 बार उल्टी हुई है, हल्का सिरदर्द, तापमान 38.6°C, बीपी 105/70, नाड़ी 108 bpm, ऑक्सीजन 97%। मरीज़ पूरी तरह सचेत है।",
        "scenario_pa": "28 ਸਾਲਾ ਔਰਤ ਨੂੰ ਸਵੇਰ ਤੋਂ 6 ਵਾਰ ਉਲਟੀ ਆਈ ਹੈ, ਹਲਕਾ ਸਿਰ ਦਰਦ, ਤਾਪਮਾਨ 38.6°C, ਬੀ.ਪੀ. 105/70, ਨਬਜ਼ 108 bpm, ਆਕਸੀਜਨ 97%। ਮਰੀਜ਼ ਪੂਰੀ ਹੋਸ਼ ਵਿੱਚ ਹੈ।",
        "vitals": {"age": 28, "temp": 38.6, "sbp": 105, "spo2": 97, "pulse": 108},
        "correct": "Urgent",
        "explanation_en": "Urgent (Yellow). High fever and persistent vomiting indicate risk of acute dehydration and electrolyte loss. Needs rapid oral rehydration therapy (ORS) or IV fluids within 30 minutes.",
        "explanation_hi": "अति-आवश्यक (पीला)। लगातार उल्टी और तेज़ बुखार शरीर में पानी की कमी (डिहाइड्रेशन) पैदा कर रहे हैं। 30 मिनट में ओआरएस या आईवी फ्लूइड शुरू करना जरूरी है।",
        "explanation_pa": "ਜ਼ਰੂਰੀ (ਪੀਲਾ)। ਲਗਾਤਾਰ ਉਲਟੀ ਅਤੇ ਤੇਜ਼ ਬੁਖ਼ਾਰ ਪਾਣੀ ਦੀ ਘਾਟ ਕਰ ਰਹੇ ਹਨ। 30 ਮਿੰਟ ਵਿੱਚ ਓ.ਆਰ.ਐੱਸ. ਜਾਂ ਗਲੂਕੋਜ਼ ਬੋਤਲ ਸ਼ੁਰੂ ਕਰਨੀ ਜ਼ਰੂਰੀ ਹੈ।",
        "key_learning_en": "Dehydration Management: Assess tongue dryness, skin turgor, and urine output before considering IV versus oral rehydration.",
        "key_learning_hi": "सीख: जीभ का सूखापन और त्वचा का लचीलापन जांचें। यदि संभव हो तो ओआरएस (ORS) सबसे सुरक्षित है।",
        "key_learning_pa": "ਸਿੱਖਿਆ: ਜੀਭ ਦੀ ਖੁਸ਼ਕੀ ਅਤੇ ਚਮੜੀ ਚੈੱਕ ਕਰੋ। ਜੇਕਰ ਮਰੀਜ਼ ਪੀ ਸਕਦਾ ਹੈ ਤਾਂ ਓ.ਆਰ.ਐੱਸ. ਸਭ ਤੋਂ ਵਧੀਆ ਹੈ।"
    },
    {
        "id": 4,
        "scenario_en": "40-year-old man visits with dry cough for 4 days, no shortness of breath, Temp 36.8°C, BP 122/80, SpO2 98%, Pulse 74 bpm. Normal chest sounds.",
        "scenario_hi": "40 वर्षीय व्यक्ति 4 दिनों से सूखी खांसी की शिकायत लेकर आया, सांस में कोई तकलीफ नहीं, तापमान 36.8°C, बीपी 122/80, ऑक्सीजन 98%, नाड़ी 74 bpm।",
        "scenario_pa": "40 ਸਾਲਾ ਵਿਅਕਤੀ 4 ਦਿਨਾਂ ਤੋਂ ਸੁੱਕੀ ਖੰਘ ਨਾਲ ਆਇਆ, ਸਾਹ ਲੈਣ ਵਿੱਚ ਕੋਈ ਔਖ ਨਹੀਂ, ਤਾਪਮਾਨ 36.8°C, ਬੀ.ਪੀ. 122/80, ਆਕਸੀਜਨ 98%, ਨਬਜ਼ 74 bpm।",
        "vitals": {"age": 40, "temp": 36.8, "sbp": 122, "spo2": 98, "pulse": 74},
        "correct": "Routine",
        "explanation_en": "Routine (Green). Stable vital signs and absence of respiratory red flags mean this patient can safely wait for standard OPD consultation.",
        "explanation_hi": "सामान्य (हरा)। सभी जीवन संकेत पूरी तरह स्थिर हैं और सांस की कोई आपात स्थिति नहीं है। नियमित ओपीडी परामर्श उपयुक्त है।",
        "explanation_pa": "ਆਮ (ਹਰਾ)। ਸਾਰੇ ਜੀਵਨ ਸੰਕੇਤ ਬਿਲਕੁਲ ਸਥਿਰ ਹਨ ਅਤੇ ਕੋਈ ਐਮਰਜੈਂਸੀ ਨਹੀਂ ਹੈ। ਆਮ ਓ.ਪੀ.ਡੀ. ਵਿੱਚ ਦਿਖਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।",
        "key_learning_en": "Screening Tip: Ask about duration of cough. If cough > 2 weeks, refer for sputum smear testing for Tuberculosis (TB Mukt Bharat).",
        "key_learning_hi": "टीबी स्क्रीनिंग: यदि खांसी 2 सप्ताह से अधिक रहे तो टीबी की जांच के लिए बलगम (sputum) का नमूना अवश्य भेजें।",
        "key_learning_pa": "ਟੀ.ਬੀ. ਸਕ੍ਰੀਨਿੰਗ: ਜੇਕਰ ਖੰਘ 2 ਹਫ਼ਤਿਆਂ ਤੋਂ ਵੱਧ ਰਹੇ ਤਾਂ ਬਲਗ਼ਮ ਦਾ ਟੈਸਟ ਕਰਵਾਉਣਾ ਜ਼ਰੂਰੀ ਹੈ।"
    }
]

# Rural Clinical Emergency Protocols (Handbook for frontline workers)
PROTOCOLS = [
    {
        "title_en": "Acute Snakebite Management",
        "title_hi": "सर्पदंश (साँप के काटने) का प्राथमिक उपचार",
        "title_pa": "ਸੱਪ ਦੇ ਡੰਗਣ 'ਤੇ ਮੁੱਢਲੀ ਸਹਾਇਤਾ",
        "icon": "🐍",
        "steps_en": [
            "Keep victim calm and completely immobilized (splint bitten limb at heart level).",
            "DO NOT apply tourniquet, do not cut wound, do not suck venom.",
            "Remove tight rings, bangles, or anklets before swelling occurs.",
            "Rush immediately to nearest hospital stocked with Anti-Snake Venom (ASV)."
        ],
        "steps_hi": [
            "मरीज़ को शांत रखें और डसे हुए अंग को बिल्कुल न हिलाएं (लकड़ी से स्थिर करें)।",
            "कसकर पट्टी (टूर्निकेट) न बांधें, चीरा न लगाएं और ज़हर चूसने का प्रयास न करें।",
            "अंगूठी, चूड़ियां या कड़े तुरंत उतार लें ताकि सूजन आने पर रुकावट न बने।",
            "एंटी-स्नेक वेनम (ASV) वाले नजदीकी अस्पताल तुरंत ले जाएं।"
        ],
        "steps_pa": [
            "ਮਰੀਜ਼ ਨੂੰ ਸ਼ਾਂਤ ਰੱਖੋ ਅਤੇ ਡੰਗੇ ਹੋਏ ਅੰਗ ਨੂੰ ਬਿਲਕੁਲ ਨਾ ਹਿਲਾਓ।",
            "ਟਾਈਟ ਰੱਸੀ ਨਾ ਬੰਨ੍ਹੋ, ਚੀਰਾ ਨਾ ਲਗਾਓ ਅਤੇ ਜ਼ਹਿਰ ਚੂਸਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਨਾ ਕਰੋ।",
            "ਮੁੰਦਰੀਆਂ ਜਾਂ ਕੜੇ ਤੁਰੰਤ ਉਤਾਰ ਲਵੋ ਤਾਂ ਜੋ ਸੋਜ ਵੇਲੇ ਨਸਾਂ ਨਾ ਦਬਣ।",
            "ਐਂਟੀ-ਸਨੇਕ ਵੈਨਮ (ASV) ਵਾਲੇ ਨੇੜਲੇ ਸਰਕਾਰੀ ਹਸਪਤਾਲ ਤੁਰੰਤ ਪਹੁੰਚਾਓ।"
        ]
    },
    {
        "title_en": "Severe Heat Stroke & Exhaustion",
        "title_hi": "लू (हीट स्ट्रोक) का आपातकालीन उपचार",
        "title_pa": "ਲੂ ਲੱਗਣ (ਹੀਟ ਸਟ੍ਰੋਕ) ਦਾ ਐਮਰਜੈਂਸੀ ਇਲਾਜ",
        "icon": "☀️",
        "steps_en": [
            "Move patient immediately to cool shaded area or ventilated room.",
            "Loosen tight clothing and spray cool water over skin while fanning vigorously.",
            "Apply wet cloth packs to neck, armpits, and groin where major blood vessels lie.",
            "If conscious and alert, offer cold ORS or salted lemon water in small sips."
        ],
        "steps_hi": [
            "मरीज़ को तुरंत ठंडी छाया या पंखे वाले हवादार कमरे में ले जाएं।",
            "कपड़े ढीले करें और शरीर पर सामान्य पानी छिड़ककर पंखा झलें।",
            "गर्दन, बगल (कांख) और जांघों पर ठंडे पानी की पट्टियां रखें।",
            "यदि मरीज़ पूरी तरह होश में हो तो धीरे-धीरे ओआरएस या नमकीन पानी पिलाएं।"
        ],
        "steps_pa": [
            "ਮਰੀਜ਼ ਨੂੰ ਤੁਰੰਤ ਛਾਂ ਵਿੱਚ ਜਾਂ ਹਵਾਦਾਰ ਕਮਰੇ ਵਿੱਚ ਲੈ ਜਾਓ।",
            "ਕੱਪੜੇ ਢਿੱਲੇ ਕਰੋ ਅਤੇ ਪਿੰਡੇ 'ਤੇ ਠੰਡਾ ਪਾਣੀ ਛਿੜਕ ਕੇ ਪੱਖਾ ਚਲਾਓ।",
            "ਗਰਦਨ ਅਤੇ ਕੱਛਾਂ 'ਤੇ ਗਿੱਲੀਆਂ ਪੱਟੀਆਂ ਰੱਖੋ ਤਾਂ ਜੋ ਸਰੀਰ ਦਾ ਤਾਪਮਾਨ ਘਟੇ।",
            "ਜੇਕਰ ਮਰੀਜ਼ ਹੋਸ਼ ਵਿੱਚ ਹੋਵੇ ਤਾਂ ਘੁੱਟ-ਘੁੱਟ ਕਰਕੇ ਓ.ਆਰ.ਐੱਸ. ਜਾਂ ਨਿੰਬੂ ਪਾਣੀ ਦਿਓ।"
        ]
    },
    {
        "title_en": "Chest Pain & Suspected Heart Attack",
        "title_hi": "सीने का दर्द और संभावित दिल का दौरा",
        "title_pa": "ਛਾਤੀ ਵਿੱਚ ਦਰਦ ਅਤੇ ਦਿਲ ਦਾ ਦੌਰਾ",
        "icon": "❤️‍🩹",
        "steps_en": [
            "Seat patient in semi-recumbent position (propped up at 45 degrees).",
            "Ensure free air flow; administer oxygen if SpO2 < 94%.",
            "Give Aspirin 300mg chewable immediately if no active bleeding or ulcer.",
            "Call 108 Emergency Ambulance for immediate transfer to Cath Lab / ICU."
        ],
        "steps_hi": [
            "मरीज़ को 45 डिग्री के कोण पर सहारा देकर बैठाएं।",
            "हवा आने दें; यदि ऑक्सीजन 94% से कम हो तो तुरंत ऑक्सीजन लगाएं।",
            "यदि आंतरिक रक्तस्राव न हो तो एस्पिरिन 300mg चबाने को दें।",
            "108 एम्बुलेंस को तत्काल कॉल करके आईसीयू वाले अस्पताल रेफर करें।"
        ],
        "steps_pa": [
            "ਮਰੀਜ਼ ਨੂੰ 45 ਡਿਗਰੀ 'ਤੇ ਸਹਾਰਾ ਦੇ ਕੇ ਬਿਠਾਓ।",
            "ਖੁੱਲ੍ਹੀ ਹਵਾ ਆਉਣ ਦਿਓ; ਜੇਕਰ ਆਕਸੀਜਨ 94% ਤੋਂ ਘੱਟ ਹੋਵੇ ਤਾਂ ਆਕਸੀਜਨ ਦਿਓ।",
            "ਡਾਕਟਰੀ ਨਿਯਮ ਅਨੁਸਾਰ ਐਸਪਰੀਨ 300mg ਚਬਾਉਣ ਲਈ ਦਿਓ।",
            "108 ਐਂਬੂਲੈਂਸ ਨੂੰ ਤੁਰੰਤ ਕਾਲ ਕਰਕੇ ਵੱਡੇ ਹਸਪਤਾਲ ਰੈਫਰ ਕਰੋ।"
        ]
    }
]

def get_text(key, lang="en"):
    lang_dict = UI.get(lang, UI["en"])
    return lang_dict.get(key, UI["en"].get(key, key))
