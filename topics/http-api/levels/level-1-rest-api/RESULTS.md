# Results — HTTP API Level 1 (REST API)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | POST /bookmarks → Google bookmark created, HTTP 201 |
| C2 | PASS | GET /bookmarks → JSON array with bookmark, HTTP 200 |
| C3 | PASS | GET /bookmarks/1 → bookmark with id:1, HTTP 200 |
| C4 | PASS | GET /bookmarks/999 → error message, HTTP 404 |
| C5 | PASS | PUT /bookmarks/2 → GitHub Updated with tags, HTTP 200 |
| C6 | PASS | DELETE /bookmarks/2 → HTTP 204, then GET returns 404 |
| C7 | PASS | GET /bookmarks → length=1, only Google remains |
| C8 | PASS | both GET /bookmarks and GET /bookmarks/1 return Valid JSON |

## Overall
✅ CLEARED — all constraints pass. HTTP API Level 1 complete.
