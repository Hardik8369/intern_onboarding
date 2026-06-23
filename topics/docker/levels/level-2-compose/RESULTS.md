# Results — Docker Level 2 (Docker Compose)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | docker-compose.yml defines web (build) and redis (image) services |
| C2 | PASS | docker compose ps → both containers Up |
| C3 | PASS | curl /health → {"redis":"connected","status":"ok"} |
| C4 | PASS | curl / three times → visitor #3, #4, #5 |
| C5 | PASS | after docker compose down && up → visitor #6 (not reset) |
| C6 | PASS | redis hostname resolves to 172.18.0.2 |

## Overall
✅ CLEARED — all constraints pass. Docker Level 2 complete. Docker topic fully cleared!
