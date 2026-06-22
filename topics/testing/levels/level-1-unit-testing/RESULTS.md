# Results — Testing Level 1 (Unit Testing)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | pytest test_calculator.py -v → 29 passed, 0 failed |
| C2 | PASS | pytest --collect-only → 29 tests collected |
| C3 | PASS | grep parametrize → found at lines 122, 134 |
| C4 | PASS | grep @pytest.fixture → found at line 12 |
| C5 | PASS | edge cases: zero inputs, negative numbers, large numbers tested |
| C6 | PASS | subtract, multiply, percentage, format_result bugs all caught |
| C7 | PASS | descriptive names like test_divide_by_zero, test_subtract_negative_numbers |
| C8 | PASS | from calculator import all 6 functions → OK |

## Overall
✅ CLEARED — all constraints pass. Testing Level 1 complete.
