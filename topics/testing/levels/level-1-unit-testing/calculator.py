"""
Calculator module with deliberate bugs.

This module provides basic arithmetic operations. Several functions contain
intentional bugs that your tests should catch.

BUG INVENTORY (for reviewer reference — intern should NOT read this):
  1. divide() — no zero-division check, crashes on divide by zero
  2. percentage() — formula is wrong (uses multiply instead of divide)
  3. format_result() — wrong string format (uses {} instead of value)
  4. multiply() — off-by-one in a specific edge case: returns a + b * b instead of a * b
  5. subtract() — arguments are in wrong order
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    # BUG 5: arguments are swapped — returns b - a instead of a - b
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a multiplied by b."""
    # BUG 4: off-by-one — returns a + b * b instead of a * b
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b."""
    # BUG 1: no zero-division check — will crash
    return a / b


def percentage(part: float, whole: float) -> float:
    """Return what percentage 'part' is of 'whole' (0-100)."""
    # BUG 2: formula wrong — multiplies instead of dividing
    return part / whole * 100


def format_result(operation: str, a: float, b: float, result: float) -> str:
    """Format a calculation result as a human-readable string."""
    # BUG 3: uses template without formatting the value
    return f"The result of {operation} on {a} and {b} is {result}"
