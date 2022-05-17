import numpy as np
from time import time
from pprint import pprint
import math
from fractions import Fraction

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
num = 3
den = 2
answers = []
for i in range(1, 1000):
    num += 2 * den
    den = num - den
    if len(list(str(num))) > len(list(str(den))):
        answers.append(1)

print("The answer is: {}".format(len(answers)))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))