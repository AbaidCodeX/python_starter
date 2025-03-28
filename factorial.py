import math


def factorial_math(n):
    """Calculate factorial using Python's built-in math module."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(n)


# Example Usage
num = 5
print(f"Factorial of {num} is: {factorial_math(num)}")
print("This is version 4 in factorial.py")
print("This is version 5 updated in factorial.py")
