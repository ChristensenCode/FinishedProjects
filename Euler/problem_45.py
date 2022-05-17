import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Find the next triangle number that is also pentagonal
# and hexagonal.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
triangle_values = [i * (i + 1) / 2 for i in range(1, 100000)]
pentagonal_values = [i * (3 * i - 1) / 2 for i in range(1, 100000)]
hexagonal_values = [i * (2 * i - 1) for i in range(1,100000)]

x = set(triangle_values) & set(pentagonal_values) & set(hexagonal_values)
print(x)

elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
