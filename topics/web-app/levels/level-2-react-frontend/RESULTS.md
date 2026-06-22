# Results — Web App Level 2 (React Frontend)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | GET /api/entries → JSON array with Alice entries |
| C2 | PASS | curl http://172.19.69.233:5173/ → HTTP 200, HTML with React content |
| C3 | PASS | React fetches entries from Flask API on load |
| C4 | PASS | POST /api/entries → entry created successfully |
| C5 | PASS | Access-Control-Allow-Origin: http://localhost:5173 header present |
| C6 | PASS | App.jsx, Guestbook.jsx, EntryForm.jsx, main.jsx - 4 components |
| C7 | PASS | Flask on port 5001, React on port 5173, both running simultaneously |

## Overall
✅ CLEARED — all constraints pass. Web App Level 2 complete.
