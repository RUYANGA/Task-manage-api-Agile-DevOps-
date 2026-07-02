# Sprint 2 Review

## Sprint Goal
Complete remaining CRUD operations and add monitoring/logging.

## Completed Stories

| ID | Story | Status |
|----|-------|--------|
| US-003 | Update task | ✅ Done |
| US-004 | Delete task | ✅ Done |

## Demo
- `PUT /tasks/{id}` — updates task title and/or `completed` status, returns 404 if not found
- `DELETE /tasks/{id}` — removes task, returns 404 if not found
- `POST /tasks` — optionally accepts `completed` field to set initial status
- Improved logging: all endpoints log operations with timestamps and details
- Validation: missing/invalid fields return 422

## Evidence
- 12 unit tests (5 for create, 3 for update, 2 for get, 1 for delete, 1 for health)
- CI pipeline continues to pass
- Full CRUD coverage including `completed` field support achieved

---

## Retrospective

### What went well
- Applied Sprint 1 feedback quickly (better logging, more tests)
- Full CRUD API with consistent error handling
- Logging added to every endpoint for traceability

### What could be improved
- In-memory storage resets between test runs; tests are order-dependent
- No persistent storage — data lost on restart
- No authentication or authorization

### Improvements for Future
- Replace in-memory list with a database (SQLite/PostgreSQL)
- Add authentication (JWT or API keys)
- Add pagination for large task lists
