import math


def is_prime_optimized(n):
    """Check if a number is prime using the square root method."""
    if n < 2:
        return False
    if n in (2, 3):  # Handle small prime cases
        return True
    if n % 2 == 0 or n % 3 == 0:  # Eliminate even and multiples of 3 early
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):  # Check odd numbers only
        if n % i == 0:
            return False
    return True


# Example Usage
num = 29
print(f"{num} is prime: {is_prime_optimized(num)}")
