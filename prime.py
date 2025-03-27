def is_prime_basic(n):
    """Check if a number is prime using a basic loop."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Example Usage
num = 28
print(f"{num} is prime: {is_prime_basic(num)}")
