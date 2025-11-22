# EventQR Gen Backend

A lightweight backend service for generating QR codes for events.
Built with **FastAPI**, **Python 3.14**, and **Poetry**, this backend provides a foundation
for QR code creation, validation, and future integrations with AWS Lambda and event workflows.

---

## 🚀 Tech Stack

- **Python 3.14**
- **FastAPI**
- **Uvicorn**
- **Poetry**

---

## 📁 Project Structure

```
eventqr-gen-backend/
    app/
        main.py
        api/
        services/
        utils/
    tests/
    pyproject.toml
```

---

## ▶️ Running Locally

### 1. Install dependencies

```bash
poetry install
```

### 2. Start the development server

```bash
poetry run uvicorn app.main:app --reload
```

API starts at:

```
http://127.0.0.1:8000
```

---

## 🧪 Running Tests

```bash
poetry run pytest
```
