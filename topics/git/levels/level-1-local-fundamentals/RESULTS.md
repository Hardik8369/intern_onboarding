# Results — Git Level 1 (Local Fundamentals)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | ls -R → README.md, notes.md, scripts/hello.sh, summary.md, .git/ exists |
| C2 | PASS | git log --oneline main → 6 commits with meaningful messages |
| C3 | PASS | git log --all --graph → shows diverge and rejoin with add-summary branch |
| C4 | PASS | 2 commits on add-summary branch before merge |
| C5 | PASS | git log --merges main → merge commit: merge add-summary branch into main |
| C6 | PASS | graph clearly shows fork and join with coherent commit messages |

## Overall
✅ CLEARED — all constraints pass. Git Level 1 complete.
