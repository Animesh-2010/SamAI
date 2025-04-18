**HealthSync - Smart Healthcare Platform
Overview
 HealthSync is a comprehensive healthcare management platform that connects patients and doctors through real-time monitoring, AI-powered assistance, and seamless communication. 
 The platform features:
    -Patient Dashboard: Track vital signs, manage medications, and communicate with healthcare providers
    -Doctor Interface: Monitor patients, review health data, and manage appointments
    -AI Health Assistant: Get instant health guidance and symptom analysis
    -Real-time Data Sharing: Securely share medical records and test results
    -Appointment Management: Schedule and track medical consultations

Features
 For Patients
  -Real-time health monitoring (blood glucose, blood pressure)
  -Medication tracking and reminders
  -Secure file upload for medical records
  -AI-powered health chatbot
  -Appointment scheduling
  -Emergency SOS functionality

 For Doctors
  -Patient health dashboard
  -Real-time alerts for critical readings
  -Appointment management
  -Secure file sharing
  -Comprehensive patient history

Installation
  Clone the repository:
      -git clone https://github.com/yourusername/HealthSync.git
      -cd HealthSync

  Install dependencies:
      -pip install -r requirements.txt
  
  Add your Groq API key:
      -GROQ_API_KEY=your_api_key_here
  
  Run the application:
      -python app.py

Access the application at http://localhost:5000

Login Credentials
 Patient Login:
   Username: patient
   Password: patient123
 Doctor Login:
   Username: doctor
   Password: doctor123

HealthSync/
├── app.py                # Main Flask application
├── static/               # Static files (CSS, JS, images)
│   └── uploads/          # File upload directory
├── templates/            # HTML templates
│   ├── index.html        # Landing page
│   ├── index2.html       # Patient dashboard
│   ├── index3.html       # Doctor interface
│   ├── chatbot.html      # Standalone chatbot page
│   └── login.html        # Login page
├── data/                 # Data storage directory
├── requirements.txt      # Python dependencies
└── README.md             # This file  
