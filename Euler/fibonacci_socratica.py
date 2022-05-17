"""
Memoization
"""
from functools import lru_cache


def fibonacci_original(n):
    """calculates the fibonacci sequence

    Args:
        n (int): number to checvk

    Returns:
        int: value of fib
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_original(n - 1) + fibonacci_original(n - 2)


fibonacci_cache = {}


@lru_cache(maxsize=1000)
def fibonacci_modified(n):
    if isinstance(n, int) is False:
        raise TypeError("Value provided is not an int!")
    elif n < 1:
        raise ValueError("n must be positive!")

    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_modified(n - 1) + fibonacci_modified(n - 2)

    fibonacci_cache[n] = value
    return value


for n in range(1, 101):
    print(n, ":", fibonacci_modified(n))
