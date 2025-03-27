from sympy import isprime


def is_prime_sympy(n):
    """Check if a number is prime using the sympy library."""
    return isprime(n)


# Example Usage
num = 29
print(f"{num} is prime: {is_prime_sympy(num)}")
print("This is version 4 in prime.py")
