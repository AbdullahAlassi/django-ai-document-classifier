# 💡 AI-Assisted Research Document Classifier  
**Built with Django, HTMX, and Local AI Models (LLM)**

---

## 🌟 Overview

Streamline your research workflow with this intuitive document classification web app. Designed to automate the categorization of research documents, the app marries **cutting-edge AI** with the simplicity of **Django** and **HTMX** for a seamless user experience. Perfect for internal tools, it leverages a **local LLM (Ollama)**, ensuring you can perform AI-based tasks without relying on external APIs.

---

## 🤔 Why Choose This Project?
This tool simulates a real-world research automation setup, allowing you to:

🔹 Paste research snippets or document texts.  
🔹 Receive instant, AI-driven category predictions.  
🔹 Automatically store results and maintain a history of classifications.

### **AI Layer Flexibility**
The app is designed with modularity in mind, supporting:

✔️ Local LLM (Ollama).  
✔️ Rule-based fallback systems.  
✔️ Integration with cloud-based LLMs, should requirements evolve in the future.

---

## ✨ Features

🔸 Backend powered by Django (including models, views, and ORM).  
🔸 Dynamic UI updates using HTMX (enabling smooth interactions without full page reloads).  
🔸 AI-driven classification, leveraging **Ollama** (via REST API).  
🔸 Storage of:
- Document title.
- Content.
- Predicted category.
- Timestamps for each entry.
🔸 Lightweight styling via Django static files.

---

## 🛠 Tech Stack

🟢 **Backend**: Python, Django.  
🟢 **Frontend**: HTMX.  
🟢 **AI Integration**: Ollama (local large language model).  
🟢 **Database**: SQLite (default Django database).

---

## 📸 Screenshots (Optional)
Add screenshots to better illustrate the app's capabilities:
- Example: Home Screen - `screenshots/home.png`.  
- Example: Classification History - `screenshots/history.png`.

---

## 🚀 Quick Start Guide
Follow the steps below to set up and launch the project.

### 1️⃣ Clone the Repository
```bash
git clone <YOUR_REPOSITORY_URL>
cd django-ai-document-classifier
```

### 2️⃣ Create and Activate a Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
python3 -m pip install --upgrade pip
python3 -m pip install django requests
```

### 4️⃣ Apply Migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 5️⃣ Install and Run Ollama (Local AI)
- Install Ollama: [Ollama Installation Guide](https://ollama.com).  
- Pull a lightweight model:
```bash
ollama pull llama3.2:1b
```
- Start Ollama (if not running automatically):
```bash
ollama serve
```

### 6️⃣ Run the Server
```bash
python3 manage.py runserver
```
- Open the application in your browser:  
`http://127.0.0.1:8000/`

---

## 🧠 How the AI Works
The application sends document data to a locally running **LLM (Ollama)** via REST API, which following a general categorisation based on the context.

---

## 🔑 Key Highlights
✅ **No API Keys Required**: AI inference is performed locally.  
✅ **Highly Extensible**: Refine with better prompts, add background tasks, or integrate advanced cloud models as needed.

---
