# Results — Web App Level 1 (Backend + Static HTML)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | GET / → HTTP 200, HTML with form and guestbook |
| C2 | PASS | POST / → HTTP 302 redirect, Alice appears on page |
| C3 | PASS | Alice, Bob, Carol all visible on same page |
| C4 | PASS | ls -R → app.py, templates/index.html, static/style.css |
| C5 | PASS | grep Jinja2 → {{ }}, {% %} found at multiple lines |
| C6 | PASS | each entry shows name and message separately |
| C7 | PASS | link tag in HTML, curl /static/style.css → CSS content |

## Overall
✅ CLEARED — all constraints pass. Web App Level 1 complete.
