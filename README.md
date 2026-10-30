# 🩺 Rural PHC AI Triage & Clinical Mentor
### *Intelligent Frontline Decision Support & Clinical Teacher for Rural Health Centres*

> **Theme 1: AI & Intelligent Systems**  
> **Problem Statement ID:** `CTBF-AI-02` — *AI triage assistant for rural health centres*  
> **Domain:** MedTech / HealthTech / Rural Healthcare  
> **Institution:** CT Group of Institutions, Jalandhar  

---

## 🌟 Overview
In rural Primary Health Centres (PHCs) and Sub-Centres (Ayushman Arogya Mandirs) across Punjab and India, frontline health workers (such as **ASHA workers, ANMs, and staff nurses**) are often the very first point of contact for critically ill patients before a medical officer is available.

This project delivers a **professional, simple, user-friendly, and offline-capable AI Triage & Clinical Teacher system** designed specifically for rural healthcare dynamics:
1. **Free Tri-Lingual Interface (English, हिन्दी, ਪੰਜਾਬੀ)** with native script support.
2. **Speech Recognition (Voice Input)**: Speak symptoms naturally in English, Hindi, or Punjabi.
3. **Voice Narration (Text-to-Speech)**: Audio readouts for patients and health workers.
4. **"Clinical Teacher" Mode**: An interactive case simulator and explainable clinical engine that trains frontline workers and medical students on clinical protocols.
5. **WHO & NHM Grounded Decision Engine**: Multi-factor triage logic with age-specific vitals differentiation (pediatric vs. adult).
6. **Printable Clinical Referral Slips**: Formal Ayushman Arogya Mandir handover slips for ambulances and tertiary centers.
7. **Emergency WhatsApp SOS Alert**: 1-click dispatch generator for 108 Emergency Services.
8. **Offline-First Resilience**: Stored locally on SQLite; synchronizes with district servers when network connectivity resumes.

---

## 🚀 Key Features

### 1. 🌐 Tri-Lingual Accessibility (English / हिन्दी / ਪੰਜਾਬੀ)
- Instant seamless language toggle across all pages, forms, results, and protocols.
- Native medical terminology accurately adapted for Punjabi (Gurumukhi) and Hindi:
  - *Emergency* -> **ਆਪਾਤਕਾਲ (लाल) / ਐਮਰਜੈਂਸੀ (ਲਾਲ)**
  - *Urgent* -> **अति-आवश्यक (पीला) / ਜ਼ਰੂਰੀ (ਪੀਲਾ)**
  - *Routine* -> **सामान्य (हरा) / ਆਮ (ਹਰਾ)**

### 2. 🎙️ Voice Input & 🔊 Audio Readout (Accessible Healthcare)
- **Speech-to-Text (Voice Input)**: Frontline workers or patients can press the mic button and speak symptoms (e.g. *"ਸੀਨੇ ਵਿੱਚ ਬਹੁਤ ਦਰਦ ਹੈ"* or *"बुखार और उल्टी"*). The AI automatically maps spoken words to corresponding clinical red flags!
- **Text-to-Speech (TTS)**: Reads out the priority and immediate first aid instructions aloud in the chosen language.

### 3. 🎓 Unconventional "Clinical Teacher" & Simulation Engine
Beyond being a triage calculator, the system acts as a digital medical mentor:
- **Interactive Case Simulator**: Frontline workers and students can practice diagnosing simulated rural clinical emergencies (e.g., adult acute coronary syndrome, infant lethargy with high pyrexia, acute dehydration).
- **Explainable Clinical Reasoning (XAI)**: Explains the exact physiological reasoning behind every triage tier.
- **Key Takeaways & Educational Pearls**: Teaches best practices and common clinical pitfalls.
- **Rural Clinical Emergency Protocols**: Quick SOP handbooks for Snakebite management, Heat Stroke, Chest Pain, and Infant dehydration.

### 4. ⚡ Rapid Test Presets
Allows evaluators and demonstrators to test complex clinical scenarios with a single click:
- `🚨 Adult Heart Attack` (SpO2 88%, SBP 175, Chest Pain, Breathlessness -> **Emergency**)
- `👶 Infant High Fever` (Age 1, Temp 39.6°C, HR 165 bpm, SpO2 92% -> **Emergency**)
- `🩸 Bleeding Trauma` (BP 90/60, HR 126 bpm, Heavy Bleeding -> **Emergency**)
- `🟢 Routine Cough` (Vitals normal -> **Routine**)

### 5. 🖨️ Printable Referral Slip & WhatsApp SOS
- Generate formal print-ready clinical referral slips with vitals, rationale, and handover signatures.
- Pre-filled WhatsApp SOS alerts to transmit vital signs directly to on-call doctors or 108 drivers.

---

## 🛠️ Technology Stack
- **Backend:** Python 3, Flask
- **Database:** SQLite (local persistent database, zero external setup)
- **Frontend:** Responsive HTML5, Vanilla JavaScript, CSS3 Design System
- **APIs:** Web Speech Recognition API, Web Speech Synthesis (TTS) API
- **Medical Protocols:** WHO ETAT (Emergency Triage Assessment and Treatment), Indian National Health Mission (NHM)

---

## 💻 How to Run the Project

### 1. Prerequisites
- Python 3.9+
- Flask (`pip install Flask`)

### 2. Launch the Application
```bash
python app.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

### 3. Language Selection & Switching
- Click **English**, **हिन्दी**, or **ਪੰਜਾਬੀ** in the top navigation bar at any time to switch the interface.
- You can also navigate directly via URL:
  - English: `http://127.0.0.1:5000/?lang=en`
  - Hindi: `http://127.0.0.1:5000/?lang=hi`
  - Punjabi: `http://127.0.0.1:5000/?lang=pa`

### 4. Switching Modes
- Click **🩺 Triage Desk** for live intake and queue management.
- Click **🎓 Clinical Teacher & Quiz** for the interactive case simulator.
- Click **📋 Rural Emergency Protocols** for emergency first aid SOPs.

---

## 📂 Project Structure
```
flask-triage/
├── app.py                # Main Flask web application & API routing
├── database.py           # SQLite database layer with auto-seeding & persistence
├── triage_engine.py      # Clinical decision logic, pediatric checks & XAI generator
├── i18n.py               # Localization engine (EN, HI, PA) + Teacher knowledge base
├── triage.db             # Local SQLite database
├── templates/
│   ├── index.html        # Main interactive triage dashboard, teacher view & SOPs
│   └── referral.html     # Formal printable clinical referral slip
└── README.md             # Project documentation & presentation guide
```

---

## 🏆 Project Alignment
Developed for **CT Group of Institutions, Jalandhar** (Department of Computer Science & Engineering / AI-ML) under **Theme 1: AI & Intelligent Systems** (`CTBF-AI-02`).
