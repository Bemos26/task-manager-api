# 📝 Task Manager API

A simple, clean, and fully documented CRUD API for managing tasks—built with FastAPI. Designed to simulate real-world backend engineering tasks, especially for freelancers and solo devs.

---

## 🚀 Features

- Create, read, update, and delete tasks
- Enforced `status` using Enum (`pending`, `in_progress`, `completed`)
- Auto-generated documentation via Swagger UI
- Written using FastAPI and Pydantic
- Uses in-memory Python list as a simulated database

---

## 🧰 Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- Git + GitHub

---

## 🛠️ Installation

1. **Clone the repo**

```bash
git clone https://github.com/Bemos26/task-manager-api.git
cd task-manager-api

- Create and activate a virtual environment
python -m venv venv
# then activate it:
# On Windows (PowerShell)
.\venv\Scripts\Activate.ps1


- Install dependencies
pip install -r requirements.txt


- Run the app
uvicorn main:app --reload



🔍 API Documentation
- Swagger UI: http://127.0.0.1:8000/docs
Use this interactive interface to test endpoints visually.

📬 Sample Endpoints
- GET /tasks – List all tasks
- POST /tasks – Create a task
- GET /tasks/{id} – Get a task by ID
- PUT /tasks/{id} – Update a task
- DELETE /tasks/{id} – Delete a task

🤝 Contributions
This project is open to contributions and feedback. Feel free to fork, clone, or suggest features!
