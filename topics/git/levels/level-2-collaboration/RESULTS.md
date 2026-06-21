# Results — Git Level 2 (Collaboration & Merge Conflicts)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | ls app.py notes/shared.md → both files exist, committed on main |
| C2 | PASS | grep conflict markers → no output (no markers remain) |
| C3 | PASS | git log → resolve merge conflict: combine greeting changes from both branches |
| C4 | PASS | git log --merges → merge feature/improve-greeting into main |
| C5 | PASS | python3 app.py → Hello from feature branch and the team! |
| C6 | PASS | git log --oneline --all → all messages are meaningful |
| C7 | PASS | git log --graph → shows fork and join collaboration pattern |

## Overall
✅ CLEARED — all constraints pass. Git Level 2 complete. Git topic fully cleared!
