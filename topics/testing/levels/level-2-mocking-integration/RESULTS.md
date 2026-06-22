# Results — Testing Level 2 (Mocking & Integration)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | pytest test_weather_reporter.py -v → 12 passed, 0 failed |
| C2 | PASS | --collect-only → 12 tests collected |
| C3 | PASS | patch used at lines 34,51,62,90,107,125,166 |
| C4 | PASS | status_code 404, pytest.raises(ValueError), Timeout tested |
| C5 | PASS | side_effect used at lines 117 (list) and 128 (exception) |
| C6 | PASS | test_integration_get_and_format calls get_current_weather + format_weather_report |
| C7 | PASS | all requests.get calls are patched, no real HTTP calls |

## Overall
✅ CLEARED — all constraints pass. Testing Level 2 complete. Testing topic fully cleared!
