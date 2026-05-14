# 💈 Barber Academy — Intelligent WhatsApp Scheduling System

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![WhatsApp](https://img.shields.io/badge/WhatsApp-Business_API-25D366?style=for-the-badge&logo=whatsapp)
![Google Calendar](https://img.shields.io/badge/Google-Calendar_API-4285F4?style=for-the-badge&logo=googlecalendar)
![VS Code](https://img.shields.io/badge/VS_Code-IDE-007ACC?style=for-the-badge&logo=visualstudiocode)

---

# 📌 Overview

Barber Academy is a scalable automation platform developed to modernize customer service and scheduling workflows for barbershops and barber schools.

The system integrates:

- WhatsApp Business API
- Google Calendar API
- Automated scheduling workflows
- Reminder systems
- Customer support automation
- Course lead generation

This project was designed as a real-world backend automation solution inspired by modern SaaS architectures.

---

# 🚀 Main Features

## 📲 WhatsApp Automation

- Interactive chatbot
- Automated customer service
- Human support redirection
- Dynamic service menus
- Automated responses

---

## 📅 Smart Scheduling

- Appointment scheduling
- Google Calendar synchronization
- Time slot management
- Real-time booking flow

---

## ⏰ Reminder System

- Automatic reminder notifications
- Scheduled WhatsApp alerts
- Attendance optimization
- Customer engagement automation

---

## 🎓 Lead Generation

- Course presentation flow
- Student acquisition automation
- Service and pricing showcase
- Conversion-oriented chatbot flow

---

# 🧠 System Architecture

```text
Customer
   ↓
WhatsApp Business API
   ↓
Flask Webhook Server
   ↓
Python Backend Logic
   ↓
Google Calendar API
   ↓
Reminder & Scheduling System
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend logic |
| Flask | Webhook server |
| Requests | API communication |
| WhatsApp Business API | Messaging integration |
| Google Calendar API | Scheduling integration |
| JSON | Data exchange |
| HTTP | API requests |
| Ngrok | Public webhook exposure |
| VS Code | Development environment |

---

# 📂 Project Structure

```bash
chatbot-barbearia/
│
├── app.py
├── credenciais.json
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone repository

```bash
git clone https://github.com/MarcusPaulodev1/Meu-Portif-lio-.git
```

---

## 2️⃣ Open with VS Code

```bash
code .
```

---

## 3️⃣ Create virtual environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\\Scripts\\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## 4️⃣ Install dependencies

```bash
pip install flask requests
pip install google-api-python-client
pip install google-auth-httplib2
pip install google-auth-oauthlib
```

---

# 🔑 API Configuration

## WhatsApp Business API

Configure inside:

```python
TOKEN_DE_ACESSO = "SEU_TOKEN"
ID_NUMERO = "SEU_PHONE_ID"
```

Meta Developers:

https://developers.facebook.com/

---

## Google Calendar API

1. Create project on Google Cloud
2. Enable Google Calendar API
3. Create service account
4. Download credentials JSON
5. Rename file to:

```bash
credenciais.json
```

---

# ▶️ Running The Project

## Start Flask server

```bash
python app.py
```

Expected output:

```bash
Running on http://127.0.0.1:5000
```

---

## Expose local server

```bash
ngrok http 5000
```

Example URL:

```bash
https://abc123.ngrok-free.app
```

---

# 🔗 Webhook Configuration

Inside Meta Developers:

```text
WhatsApp → Configuration → Webhook
```

Webhook URL:

```text
https://SEU_NGROK/webhook
```

---

# 💬 Example Conversation

```text
👤 User:
Oi

🤖 Bot:
👋 Bem-vindo à Barber Academy ✂️

1️⃣ Agendar corte
2️⃣ Conhecer cursos
3️⃣ Ver preços
4️⃣ Falar com atendente
5️⃣ Endereço e horário
```

---

# 📈 Business Impact

This project demonstrates:

- Backend engineering
- API integrations
- Automation systems
- Scheduling workflows
- SaaS-oriented architecture
- Real-world business applications
- Customer service optimization

---

# 🔥 Future Improvements

- OpenAI integration
- AI-powered conversations
- Admin dashboard
- CRM integration
- Payment systems
- Analytics dashboard
- Database persistence
- Multi-user management

---

# 🎯 Target Market

- Barbershops
- Barber schools
- Beauty salons
- Clinics
- Local businesses
- Service companies

---

# 👨‍💻 Author

Marcus Paulo

- Software Engineering Student
- Python Automation Developer
- Backend & API Integration Enthusiast

## 🔗 LinkedIn

https://www.linkedin.com/in/marcus-paulo-00a2833a6
