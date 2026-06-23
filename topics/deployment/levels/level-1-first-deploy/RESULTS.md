# Results — Deployment Level 1 (First Deploy)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | curl https://my-first-deploy-production-10ae.up.railway.app/ → HTTP 200, Hello from production! |
| C2 | PASS | curl /health → {"environment":"production","status":"ok"} |
| C3 | PASS | environment: production (APP_ENVIRONMENT set in Railway) |
| C4 | PASS | Railway built from Dockerfile (Docker build steps in logs) |
| C5 | PASS | github.com/Hardik8369/my-first-deploy has app.py, Dockerfile, requirements.txt |
| C6 | PASS | 3 consecutive requests all return HTTP 200 with production |
| C7 | PASS | Railway logs show Flask starting on 0.0.0.0:5000 |

## Public URL
https://my-first-deploy-production-10ae.up.railway.app

## Overall
✅ CLEARED — all constraints pass. Deployment Level 1 complete.
