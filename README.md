# English to Odia Translator Ecosystem 🚀

A full-stack, cross-platform translation application ecosystem built in a single 6-hour sprint. This project scales a local translation script into a production-ready, cloud-connected architecture supporting standalone native applications for both **Windows Desktop** and **Android Mobile**.

---

## 🌟 Key Features

* **Cloud-Powered Engine:** Zero local processing or heavy dependencies required on client machines.
* **Cross-Platform Accessibility:** Translate seamlessly via a dedicated desktop executable or a mobile app interface.
* **Clean & Responsive UI:** Modern dark-themed user interface optimized for smooth user experience and quick navigation.
* **Asynchronous Processing:** Built-in support for instant translations with shortcut keys (`Ctrl + Enter`).

---

## 🛠️ Architecture & Tech Stack

The ecosystem is split into two main core layers:

### 1. Backend (Cloud API)
* **Framework:** Python (Flask)
* **Security & Access:** Flask-CORS (Cross-Origin Resource Sharing) for cross-platform request handling.
* **Translation Core:** `deep-translator` (Google Translate Engine wrapper).
* **WSGI Production Server:** Gunicorn
* **Deployment Platform:** Hosted live on **Render.com**

### 2. Frontend & Client Layouts
* **UI Structure:** Semantic HTML5, CSS3 Grid/Flexbox UI design.
* **Desktop Wrapper:** Python `webview` + compiled into a standalone binary using `PyInstaller`.
* **Mobile Wrapper:** Android App Package (`.apk`) wrapped natively for mobile layout views.

---

## 📂 Project Repository Structure

```text
├── templates/
│   └── index.html         # Responsive User Interface (Targets Cloud Server URL)
├── file.py                # Flask Backend API Endpoint Setup
├── gui.py                 # Desktop GUI Layout Execution Script
├── requirements.txt       # Production API Environment Packages
└── README.md              # Project Documentation
