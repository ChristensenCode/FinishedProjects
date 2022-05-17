import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# If dn represents the nth digit of the fractional part,
# find the value of the following expression.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()

x = [str(i) for i in range(1, 1000001)]
total_string = ''.join(x)

values = np.array([1, 10, 100, 1000, 10000, 100000, 1000000])
value_1 = values - 1
answer = np.zeros(shape=values.shape, dtype='int32')

counter = 0
for j in np.nditer(value_1):
    picked = int(total_string[j])
    answer[counter] = picked
    counter += 1

print('The answer is {}.'.format(np.prod(answer)))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))

