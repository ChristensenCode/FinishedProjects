import numpy as np
from time import time
from pprint import pprint
import re
import collections
import math

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# For which value of p ≤ 1000, is the number of solutions maximised?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()

#
# a^2 + b^2 = c^2
# a = sqrt(c^2-b^2)
# a + b + c = perimeter
# could i iterate on the angle?
# theta_a + theta_b + 90 = 180
#
possibles = {}
period_finder = re.compile('[.0]')
for a in range(3, 500):
    for b in range(3, 500):
        c = math.sqrt(a**2 + b**2)
        string_c = str(c)
        if len(string_c) < 11:
            p = a + b + c
            possibles.setdefault(p, [])
            possibles[p].append((a, b, c))
winner = {}
for k, v in possibles.items():
    combo_length = len(v)
    winner[k] = combo_length
inverse = [(value, key) for key, value in winner.items()]
print("The answer is {} with {} combinations.".format(int(max(inverse)[1]), winner[max(inverse)[1]]))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
