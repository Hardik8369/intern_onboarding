# Results — Linux Level 1 (Command-Line Basics)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | ls -R workspace → shows notes.txt, notes-backup.txt, secrets/, scripts/, api-key.txt, hello.sh |
| C2 | PASS | cat workspace/notes.txt → my first file |
| C3 | PASS | diff workspace/notes.txt workspace/notes-backup.txt → no output (identical) |
| C4 | PASS | ls -l workspace/secrets/api-key.txt → -rw------- 1 hardik_gowda |
| C5 | PASS | ls -l workspace/scripts/hello.sh → -rwxr-xr-x 1 hardik_gowda |
| C6 | PASS | ./workspace/scripts/hello.sh → hello |
| C7 | PASS | cd workspace/secrets && pwd && cat api-key.txt → correct path and mysecretkey123 |

## Overall
✅ CLEARED — all constraints pass. Linux topic complete (you entered at the level you chose and passed it).
