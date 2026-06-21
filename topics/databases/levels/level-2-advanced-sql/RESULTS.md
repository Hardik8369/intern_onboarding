# Results — Databases Level 2 (Advanced SQL)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | v_task_summary(11 rows), v_project_stats(4 rows) |
| C2 | PASS | SELECT DISTINCT status → only in_progress and pending |
| C3 | PASS | idx_tasks_project_id, idx_tasks_status on tasks table |
| C4 | PASS | EXPLAIN → SEARCH tasks USING INDEX idx_tasks_project_id |
| C5 | PASS | 3-table join returns project name, task title, tag |
| C6 | PASS | ROW_NUMBER() ranks correctly per project, rank 1 = highest priority |
| C7 | PASS | Transaction created DevOps Setup project with 2 tasks atomically |

## Overall
✅ CLEARED — all constraints pass. Databases Level 2 complete. Databases topic fully cleared!
