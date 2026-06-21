# Results — Linux Level 2 (Shell Log Analyzer)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | ./analyze.sh sample-access.log → prints all 4 sections |
| C2 | PASS | ./analyze.sh → Usage: ./analyze.sh <logfile> [N] |
| C3 | PASS | ./analyze.sh sample-access.log → exactly 5 IPs listed |
| C4 | PASS | top 3 IPs match independent awk check: 203.0.113.7 142, 198.51.100.23 98, 192.0.2.88 71 |
| C5 | PASS | 4xx errors: 85, 5xx errors: 36 match independent awk check |
| C6 | PASS | busiest hour 14:00 count 137 matches independent check |
| C7 | PASS | total 526 matches wc -l |
| C8 | PASS | ./analyze.sh does-not-exist.log 5 → Error: file not found |

## Overall
✅ CLEARED — all constraints pass. Linux Level 2 complete.
