# Results — Databases Level 1 (SQL Fundamentals)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | sqlite3 tasks.db < schema.sql → no errors |
| C2 | PASS | .schema shows 3 tables with FOREIGN KEY constraints |
| C3 | PASS | sqlite3 tasks.db < queries.sql → all 5 queries produce output |
| C4 | PASS | projects=3, tasks=11, task_tags=10 |
| C5 | PASS | 3 overdue tasks found: Fix login page bug, Integrate API, Write data validation |
| C6 | PASS | Mobile App with 4 tasks is the project with most tasks |
| C7 | PASS | schema.sql and queries.sql have comments and descriptive names |

## Overall
✅ CLEARED — all constraints pass. Databases Level 1 complete.
