# Sprint 1 Review

## Sprint Goal
Deliver core CRUD foundation and CI pipeline.

## Completed Stories

| ID | Story | Status |
|----|-------|--------|
| US-001 | Create task | ✅ Done |
| US-002 | Get tasks | ✅ Done |
| US-005 | Health check | ✅ Done |

## Demo
- `POST /tasks` — creates a task with auto-generated ID, stores in memory
- `GET /tasks` — returns list of tasks (empty or populated)
- `GET /health` — returns `{"status": "healthy"}`
- Swagger UI available at `/docs`

## Evidence
- Unit tests for create task and health check pass
- CI pipeline runs tests on every push to `main`
- Commit history shows iterative development

---

## Retrospective

### What went well
- Small, focused commits made it easy to track progress
- Fast feedback from tests caught issues early
- CI pipeline was quick to set up with GitHub Actions

### What could be improved
- Better input validation needed (empty titles, missing fields)
- No way to update or delete tasks yet

### Improvements for Sprint 2
- Add update and delete endpoints (US-003, US-004)
- Improve logging with request-level details
- Add more comprehensive test coverage (edge cases)
