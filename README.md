# AI-Assisted Research Document Classifier (Django + HTMX + Local LLM)

A small internal-tool style web app that automates **research document classification**.
Built with **Django** for the backend, **HTMX** for dynamic UI updates (no heavy JS),
and a **local LLM (Ollama)** for AI-based classification — so it can run without paid APIs.

## Why this project
This project simulates a real “research workflow automation” tool:
- Paste a document / research snippet
- Get an automatic category prediction
- Store results and view history

It’s designed with a modular “AI layer” so you can swap between:
- local LLM (Ollama)
- rule-based fallback
- cloud LLM later (if needed)

## Features
- Django backend (models, views, ORM)
- Dynamic UI updates using HTMX (history updates without full page reload)
- Local LLM classification via Ollama REST API
- Stores document title, content, predicted category, timestamp
- Minimal CSS via Django static files

## Tech Stack
- Python
- Django
- HTMX
- Ollama (local LLM)
- SQLite (default Django DB)

## Screenshots (optional)
Add screenshots here after you push:
- `screenshots/home.png`
- `screenshots/history.png`

## Getting Started

## 1) Clone the repo

git clone <YOUR_REPO_URL>
cd research_ai
## 2) Create & activate virtual environment

python3 -m venv venv
source venv/bin/activate
## 3) Install dependencies

python3 -m pip install --upgrade pip
python3 -m pip install django requests
## 4) Run migrations

python3 manage.py makemigrations
python3 manage.py migrate
## 5) Install & run Ollama (local AI)
Install Ollama: https://ollama.com

Pull a lightweight model:

ollama pull llama3.2:1b
(Usually Ollama runs in the background on macOS. If needed:)
ollama serve

## 6) Run the server

python3 manage.py runserver
Open:
http://127.0.0.1:8000/

## How the AI works
The app sends the document text to a locally running LLM (Ollama) using its REST API and
asks it to output exactly one of these categories:

- Technology

- Finance

- Healthcare

- General

## Notes
No API keys required (local inference)

Designed to be extended with better prompts, background tasks, or cloud models

