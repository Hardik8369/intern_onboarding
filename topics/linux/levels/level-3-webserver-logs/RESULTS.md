# Results — Linux Level 3 (Live Web Server Logs)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | docker ps -a → 790a797bfeca nginx-logs ran successfully |
| C2 | PASS | head -3 captured-access.log → every line starts with 172.17.0.1, wc -l → 60 |
| C3 | PASS | awk '$9 ~ /^4[0-9][0-9]$/' captured-access.log | wc -l → 10 |
| C4 | PASS | ./analyze-live.sh captured-access.log → prints all 4 sections |
| C5 | PASS | ./analyze-live.sh → Usage: ./analyze-live.sh <logfile> [N] |
| C6 | PASS | 4xx errors: 10, 5xx errors: 0 match independent awk check |
| C7 | PASS | wc -l → 60 matches Total requests processed: 60 |
| C8 | PASS | docker stop nginx-logs && docker rm nginx-logs → docker ps -a shows nothing |

## Overall
✅ CLEARED — all constraints pass. Linux Level 3 complete. Linux topic fully cleared!
