def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Example Usage
num = 5
print(f"Factorial of {num} is: {factorial_recursive(num)}")
