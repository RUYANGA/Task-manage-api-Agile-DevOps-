# Sprint 0 — Planning

## Product Vision
A lightweight Task Management REST API built with FastAPI to demonstrate Agile development practices and DevOps automation using CI/CD, testing, and in-memory data storage.

---

## Product Backlog

| ID | User Story | Priority | Estimate (Story Points) | Acceptance Criteria |
|----|-----------|----------|------------------------|---------------------|
| US-001 | As a user, I want to create a task so that I can track things I need to do. | High | 2 | A POST `/tasks` request with a `title` creates a new task and returns it with an `id` and `completed=false`. Optionally accepts `completed` (true/false) to set initial status. |
| US-002 | As a user, I want to view all tasks so that I can see what I need to work on. | High | 1 | A GET `/tasks` request returns a list of all tasks (empty array if none exist). |
| US-003 | As a user, I want to update a task so that I can change its title or completion status. | High | 2 | A PUT `/tasks/{id}` request updates the task's `title` and optionally `completed`. Returns 404 if the task doesn't exist. |
| US-004 | As a user, I want to delete a task so that I can remove completed or unwanted items. | High | 1 | A DELETE `/tasks/{id}` removes the task and returns a confirmation message. Returns 404 if the task doesn't exist. |
| US-005 | As a user, I want to check system health so that I know the API is running. | Medium | 1 | A GET `/health` request returns `{"status": "healthy"}`. |

**Total estimated effort:** 7 story points

---

## Definition of Done (DoD)

A feature is considered complete when:

- Code is implemented and functional
- Unit tests are written and passing
- Code is committed with clear, incremental messages
- CI pipeline passes successfully
- Endpoint tested via Swagger UI or HTTP client

---

## Sprint 1 Plan

**Sprint goal:** Deliver core CRUD foundation and CI pipeline.

**Selected stories:**
- US-001 (Create task) — 2 pts
- US-002 (Get tasks) — 1 pt
- US-005 (Health check) — 1 pt

**Sprint 1 total:** 4 story points

---

## Sprint 2 Plan

**Sprint goal:** Complete remaining CRUD operations and add monitoring/logging.

**Selected stories:**
- US-003 (Update task) — 2 pts
- US-004 (Delete task) — 1 pt

**Sprint 2 total:** 3 story points
