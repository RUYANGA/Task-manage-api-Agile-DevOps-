# 📘 Task Management API

[![CI](https://github.com/RUYANGA/Task-manage-api-Agile-DevOps-/actions/workflows/ci.yml/badge.svg)](https://github.com/RUYANGA/Task-manage-api-Agile-DevOps-/actions/workflows/ci.yml)

A lightweight Task Management REST API built with **FastAPI** to demonstrate Agile development practices and DevOps automation using CI/CD, testing, and in-memory data storage.

---

## 🚀 Project Overview

This project is a simple Task Management system that allows users to:

- Create tasks
- View all tasks
- Update tasks
- Delete tasks
- Check system health

It uses **in-memory storage (Python list/dictionary)** to focus on Agile workflow, API design, testing, and CI/CD rather than database complexity.

---

## 🛠 Tech Stack

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- Git & GitHub
- GitHub Actions (CI/CD)
- Logging (standard library)

---

## 🚦 Getting Started

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/)

### Installation

```bash
git clone https://github.com/RUYANGA/Task-manage-api-Agile-DevOps-.git
cd task-management-api
poetry install
```

### Running the Server

```bash
poetry run uvicorn app.main:app --reload
```

API available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Interactive docs (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Running Tests

```bash
poetry run pytest
poetry run pytest -v          # verbose
poetry run pytest tests/test_health.py  # single file
```

---

## 📁 Project Structure

```text
task-management-api/
│
├── app/
│   ├── main.py          # API routes
│   ├── models.py        # Pydantic data models
│   ├── tasks.py         # In-memory storage
│   └── logger.py        # Logging setup
│
├── tests/
│   ├── test_create.py
│   ├── test_get.py
│   ├── test_update.py
│   ├── test_delete.py
│   └── test_health.py
│
├── .github/workflows/
│   └── ci.yml           # CI pipeline
│
├── SPRINT0.md           # Sprint 0 — Planning
├── SPRINT1_REVIEW.md    # Sprint 1 — Review & Retrospective
├── SPRINT2_REVIEW.md    # Sprint 2 — Review & Retrospective
│
├── pyproject.toml
└── README.md
```

---

## 📡 API Reference

### Home

```
GET /
```

Response: `{"message": "Task API"}`

### Health Check

```
GET /health
```

Response: `{"status": "healthy"}`

### Create Task

```
POST /tasks
Content-Type: application/json

{
  "title": "Buy groceries"
}
```

Response `200`:
```json
{
  "id": 1,
  "title": "Buy groceries",
  "completed": false
}
```

Response `422` (missing title): validation error

### Get All Tasks

```
GET /tasks
```

Response `200`:
```json
[
  { "id": 1, "title": "Buy groceries", "completed": false }
]
```

### Update Task

```
PUT /tasks/1
Content-Type: application/json

{
  "title": "Buy vegetables"
}
```

Response `200`: updated task object
Response `404`: `{"detail": "Task not found"}`

### Delete Task

```
DELETE /tasks/1
```

Response `200`: `{"message": "Task deleted"}`
Response `404`: `{"detail": "Task not found"}`

---

## 📋 Product Backlog

| ID | User Story | Priority | Estimate | Acceptance Criteria |
|----|-----------|----------|----------|-------------------|
| US-001 | Create task | High | 2 pts | `POST /tasks` with a `title` creates a task and returns it with `id` and `completed=false`. |
| US-002 | View all tasks | High | 1 pt | `GET /tasks` returns list of all tasks (empty array if none). |
| US-003 | Update task | High | 2 pts | `PUT /tasks/{id}` updates the title. Returns 404 if not found. |
| US-004 | Delete task | High | 1 pt | `DELETE /tasks/{id}` removes the task. Returns 404 if not found. |
| US-005 | Health check | Medium | 1 pt | `GET /health` returns `{"status": "healthy"}`. |

**Total:** 7 story points

---

## 📌 Sprint Breakdown

### Sprint 1 — Core Features
- US-001 (Create task — 2 pts)
- US-002 (Get tasks — 1 pt)
- US-005 (Health check — 1 pt)
- CI pipeline setup
- Unit tests

[View Sprint 1 Review →](./SPRINT1_REVIEW.md)

### Sprint 2 — Improvement Phase
- US-003 (Update task — 2 pts)
- US-004 (Delete task — 1 pt)
- Improved logging
- Additional test coverage

[View Sprint 2 Review →](./SPRINT2_REVIEW.md)

---

## 📌 Agile Methodology

This project follows Agile principles with iterative development.

### Sprint 0 — Planning
[View Sprint 0 →](./SPRINT0.md)
- Product vision defined
- Product backlog with acceptance criteria and estimates
- Definition of Done (DoD) defined
- Sprint 1 and Sprint 2 planned

### Sprint 1 — Execution
- Create Task, Get Tasks, Health Check
- CI pipeline setup
- 8 unit tests
- [Review & Retrospective](./SPRINT1_REVIEW.md)

### Sprint 2 — Execution & Improvement
- Update Task, Delete Task
- Improved logging (request-level tracking)
- Additional tests
- [Review & Retrospective](./SPRINT2_REVIEW.md)

---

## 📡 Monitoring & Logging

All API endpoints log request activity using Python's standard `logging` module.

**Log format:**
```
2025-01-15 10:30:45,123 - INFO - Task created: id=1, title=Buy groceries
2025-01-15 10:31:02,456 - ERROR - Task not found: id=99
```

| Event | Log Level | Example |
|-------|-----------|---------|
| Task created | INFO | `Task created: id=1, title=Buy groceries` |
| Tasks listed | INFO | `Tasks listed: 2 items` |
| Task updated | INFO | `Task updated: id=1, new_title=Buy vegetables` |
| Task deleted | INFO | `Task deleted: id=1` |
| Task not found during update/delete | ERROR | `Task not found: id=99` |
| Health check | INFO | `Health check passed` |

---

## ✅ CI/CD Pipeline

The project uses **GitHub Actions** for continuous integration.

**Pipeline steps (`.github/workflows/ci.yml`):**
1. Checkout code
2. Set up Python 3.13
3. Install Poetry
4. Install dependencies (`poetry install`)
5. Run tests (`poetry run pytest`)

The pipeline triggers on every push to the `main` branch.

---

## 📌 Definition of Done (DoD)

A feature is considered complete when:

- Code is implemented and functional
- Unit tests are written and passing
- Code is committed with clear, incremental messages
- CI pipeline passes successfully
- Endpoint tested via Swagger UI or HTTP client

---

## 📄 Sprint Documents

- [Sprint 0 — Planning](./SPRINT0.md)
- [Sprint 1 — Review & Retrospective](./SPRINT1_REVIEW.md)
- [Sprint 2 — Review & Retrospective](./SPRINT2_REVIEW.md)
