# Problem 23
# Non-Abundant sums

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

# Creates a list of abundant numbers
from pprint import pprint
from time import time
import numpy as np


def proper_divisor(n):
    divisors = []
    # possible_divisors = np.arange(1, n)
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) > n:
        return n


def main():
    start_time = time()
    abundant_numbers = []
    n = 0
    combined_values = []
    for x in range(1, 28124):
        if proper_divisor(x) is not None:
            abundant_numbers.append(x)
            # print('-'*60)
            # print(abundant_numbers[n])
            # print('-'*60)
            for value in abundant_numbers:
                combined = abundant_numbers[n] + value
                # print(combined)
                combined_values.append(combined)
            n += 1
    # pprint(set(abundant_numbers))
    numbers = []
    for i in range(1, 28124):
        numbers.append(i)
    number_set = set(numbers)
    combined_numbers = set(combined_values)
    cannot = number_set.difference(combined_numbers)

    elapsed_time = time() - start_time
    print(f"Total Time {elapsed_time}")
    print(sum(cannot))


if __name__ == "__main__":
    main()
