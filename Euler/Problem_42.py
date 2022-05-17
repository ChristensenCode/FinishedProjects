import numpy as np
from time import time
from pprint import pprint
import string


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English
# words, how many are triangle words?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
with open('problem42.txt') as f:
    items = f.read().split('","')
    items[0] = 'A'
    items[-1] = 'YOUTH'

alphabet = string.ascii_uppercase
values = range(1, 27)
alphabet_dict = dict(zip(alphabet, values))

triangle_values = []
for k in range(1, 10001):
    triangle_calc = int(0.5 * k * (k + 1))
    triangle_values.append(triangle_calc)
counter = 0
for i in items:
    # print(i)
    number_replace_list = []
    for j in i:
        number_replace = alphabet_dict[j]
        number_replace_list.append(number_replace)
    # print(number_replace_list)
    summation = sum(number_replace_list)

    if summation in triangle_values:
        counter += 1

print('The answer is {}.'.format(counter))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))

