# Results — Docker Level 1 (Dockerfile Basics)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | cat Dockerfile → FROM python:3.11-slim |
| C2 | PASS | docker build -t counter-app . → build completed successfully |
| C3 | PASS | curl /health → HTTP 200, {"status":"ok"} |
| C4 | PASS | curl / → Hello! You are visitor #2 |
| C5 | PASS | .dockerignore excludes __pycache__, .git, *.pyc, *.md |
| C6 | PASS | slim tag, WORKDIR, EXPOSE 5000, USER appuser |

## Overall
✅ CLEARED — all constraints pass. Docker Level 1 complete.
