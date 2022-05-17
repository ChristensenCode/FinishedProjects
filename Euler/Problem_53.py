import numpy as np
from time import time
from pprint import pprint
from math import factorial

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()


def combinatronics(n, r):
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    output_value = (numerator/denominator)
    return output_value

answers = []
for n in range(1, 101):
    for r in range(n):
        x = combinatronics(n, r)
        if x > 1000000:
            # print(n, r)
            answers.append(x)
print("The answer is: {}".format(len(answers)))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))

