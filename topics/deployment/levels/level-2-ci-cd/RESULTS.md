# Results — Deployment Level 2 (CI/CD)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | .github/workflows/deploy.yml exists with name, on, jobs, steps |
| C2 | PASS | 3 green workflow runs triggered by push to main |
| C3 | PASS | docker build --build-arg COMMIT_HASH=${{ github.sha }} |
| C4 | PASS | curl /health → HTTP 200, {"status":"ok"} |
| C5 | PASS | /version → c357f7e41580afa33442b24fccc1e2b0b3cfc07e matches git rev-parse HEAD |
| C6 | PASS | no hardcoded secrets in workflow file |
| C7 | PASS | 5 steps: Checkout, Setup Buildx, Build, Verify, Deploy complete |

## Public URL
https://my-ci-cd-deploy-production.up.railway.app

## Overall
✅ CLEARED — all constraints pass. Deployment Level 2 complete. Deployment topic fully cleared!
