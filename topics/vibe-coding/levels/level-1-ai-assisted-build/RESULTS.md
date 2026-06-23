# Results — Vibe Coding Level 1 (AI-Assisted Build)

## Constraint Results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | PROMPT_LOG.md exists with 4 prompts, each with what was asked, AI response summary, and what was done with it |
| C2 | PASS | VERIFICATION.md exists with 9 test cases, each with input, expected, actual, and pass/fail |
| C3 | PASS | python3 md2html.py --help prints usage, input file arg, and -o output flag |
| C4 | PASS | sample1.md converts correctly — h1, strong, em, ul/li, a, pre/code, blockquote all present in output |
| C5 | PASS | nonexistent.md → "Error: input file not found." No traceback. No args → argparse usage error shown |
| C6 | PASS | ls shows sample1.md, sample2.md, sample1.html, sample2.html all present |
| C7 | PASS | AI score: 4/5 — "Iterated properly. Each prompt triggered by actual testing. Three concrete modifications made to AI output. Knows when not to accept output." |
| C8 | PASS | AI score: 3/5 — "Two real bugs documented with specific fixes. Structure is good and bug documentation is honest." |

## AI Review Summary

C7 reviewed with Claude — score 4/5. Prompts show clear iteration: build → test → observe
failure → targeted prompt. Three places where AI output was modified or rejected rather than
blindly accepted.

C8 reviewed with Claude — score 3/5. Two bugs found and fixed (if/elif ordering, greedy
regex). Edge case coverage noted as an area for improvement but core happy path and CLI
error handling all verified.

## Overall
✅ CLEARED — all 8 constraints pass. Vibe Coding Level 1 complete.
