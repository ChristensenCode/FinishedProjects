import numpy as np
from time import time
from collections import Counter
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
# but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
minimum = 100000
maximum = 200000
test_array = np.arange(minimum, maximum)[:, np.newaxis]
columns = np.array([1, 2, 3, 4, 5, 6])[:, np.newaxis].transpose()

possibles = test_array * columns
answer_found = False
for i in possibles:
    checker = []
    # print('-' * 60)
    for index, j in enumerate(i):
        numpyToString = sorted(str(j))
        checker.append(Counter(numpyToString).keys())
        if checker[index] != checker[index-1]:
            break
        elif len(checker) == 6:
            answer_found = True
            break
    if answer_found:
        break
print("The answer is: {}".format(i[0]))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
