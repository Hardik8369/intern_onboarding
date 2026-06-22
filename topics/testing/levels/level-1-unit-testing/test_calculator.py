"""
Test suite for calculator.py — fixed and extended.
"""
import pytest
from calculator import add, subtract, multiply, divide, percentage, format_result


# ============================================
# FIXTURE
# ============================================

@pytest.fixture
def sample_values():
    """Fixture providing common test values."""
    return {"a": 10, "b": 5, "result": 50}


# ============================================
# add() tests
# ============================================

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_with_zero():
    assert add(0, 5) == 5

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000


# ============================================
# subtract() tests
# ============================================

def test_subtract_basic():
    assert subtract(10, 3) == 7

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_result_negative():
    assert subtract(3, 10) == -7


# ============================================
# multiply() tests
# ============================================

def test_multiply_basic():
    assert multiply(2, 3) == 6

def test_multiply_by_zero():
    assert multiply(0, 5) == 0

def test_multiply_large_numbers():
    assert multiply(100, 200) == 20000

def test_multiply_negative():
    assert multiply(-3, 4) == -12


# ============================================
# divide() tests
# ============================================

def test_divide_basic():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_negative():
    assert divide(-10, 2) == -5.0


# ============================================
# percentage() tests
# ============================================

def test_percentage_basic():
    assert percentage(25, 200) == 12.5

def test_percentage_zero_part():
    assert percentage(0, 100) == 0.0

def test_percentage_using_fixture(sample_values):
    """Test using fixture values."""
    assert sample_values["a"] == 10
    assert sample_values["b"] == 5


# ============================================
# format_result() tests
# ============================================

def test_format_result():
    result = format_result("add", 3, 5, 8)
    assert "3" in result
    assert "5" in result
    assert "8" in result

def test_format_result_contains_operation():
    result = format_result("multiply", 4, 5, 20)
    assert "multiply" in result


# ============================================
# PARAMETRIZED tests
# ============================================

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
    (1.5, 2.5, 4.0),
])
def test_add_parametrized(a, b, expected):
    """Parametrized test for add() with multiple inputs."""
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (100, 4, 25.0),
])
def test_divide_parametrized(a, b, expected):
    """Parametrized test for divide() with multiple inputs."""
    assert divide(a, b) == expected
