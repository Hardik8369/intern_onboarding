"""
Test suite for calculator.py.

This file has 15 tests. Some are correct, some test the wrong thing,
and some test assumptions that don't match the actual bug. Your job:
figure out which are wrong, fix them, then fix the code.

HINT INVENTORY (for reviewer reference — intern should NOT read this):
  - T1: correct (add happy path)
  - T2: correct (add negative numbers)
  - T3: WRONG TEST — asserts subtract(10,3)==7 but bug swaps args, so it actually
        passes with the bug. Should fail after fix! Intern must fix test logic.
  - T4: correct (multiply happy path — happens to pass with the bug because 2+3*3=11
        but also 2*3=6... wait, no. BUG: multiply(2,3)=2+3*3=11, correct=6. So this
        test SHOULD fail, catching the bug.)
  - T5: WRONG TEST — multiply(0, 5) = 0+5*5=25 but should be 0. Test asserts 0,
        which WILL correctly catch the bug.
  - T6: correct (divide happy path)
  - T7: correct (divide by zero — should raise, but code doesn't handle it)
  - T8: WRONG TEST — percentage tests with wrong expected value (assumes buggy formula)
  - T9: correct (format_result — will fail because of the {} bug)
  - T10: correct (add floats)
  - T11: MISSING — no test for percentage edge case (whole=0)
  - T12: MISSING — no test for subtract negative numbers
  - T13: correct (multiply large numbers — will fail due to bug)
  - T14: MISSING — no test for divide negative numbers
  - T15: correct (add zero)
"""

import pytest
from calculator import add, subtract, multiply, divide, percentage, format_result


# --- add() tests ---

def test_add_positive_numbers():
    assert add(3, 5) == 8


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_with_zero():
    assert add(0, 5) == 5


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


# --- subtract() tests ---

def test_subtract_basic():
    # BUG 5 in code: subtract returns b - a instead of a - b
    # This test expects a - b, so it WILL fail — catching the bug correctly.
    assert subtract(10, 3) == 7


# --- multiply() tests ---

def test_multiply_basic():
    assert multiply(2, 3) == 6


def test_multiply_by_zero():
    assert multiply(0, 5) == 0


def test_multiply_large_numbers():
    assert multiply(100, 200) == 20000


# --- divide() tests ---

def test_divide_basic():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# --- percentage() tests ---

def test_percentage_basic():
    assert percentage(25, 200) == 12.5  


# --- format_result() tests ---

def test_format_result():
    # BUG 3: format_result uses {} instead of {a}
    result = format_result("add", 3, 5, 8)
    assert "3" in result
    assert "5" in result
    assert "8" in result


# --- Edge case tests (MISSING — intern should add more) ---
# No tests for:
# - percentage with whole=0 (should raise or handle)
# - subtract with negative numbers
# - divide with negative numbers
# - add with large numbers causing overflow (not really a Python issue)
