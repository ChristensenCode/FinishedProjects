"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to 
determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less 
than nine and relatively prime to nine, φ(9)=6.
n	Relatively Prime	φ(n)	n/φ(n)
2	1	                   1	2
3	1,2	                   2	1.5
4	1,3	                   2	2
5	1,2,3,4	               4	1.25
6	1,5	                   2	3
7	1,2,3,4,5,6	           6	1.1666...
8	1,3,5,7	               4	2
9	1,2,4,5,7,8	           6	1.5
10	1,3,7,9	               4	2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
https://en.wikipedia.org/wiki/Euler%27s_totient_function
"""

from typing import List
from numba import njit, vectorize
from time import time
from collections import Counter
import numpy as np
from tqdm import tqdm
from sympy.ntheory import factorint


def mathy(base, factor):
    return base ** (factor - 1) * (base - 1)


def main():

    n_over_phi = 0
    answer = 0
    for n in tqdm(range(2, 1000001)):
        builder = 1
        for base, factor in factorint(n).items():
            builder *= mathy(base, factor)
        test = n / builder
        if test > n_over_phi:
            answer = n
            n_over_phi = test
    return answer


if __name__ == "__main__":
    start_time = time()
    print("The answer is: {}".format(main()))
    elapsed_time = time() - start_time
    print("The answer was found in {0:.4f} s.".format(elapsed_time))
