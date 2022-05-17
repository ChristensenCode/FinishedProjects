import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
a = [x for x in range(1, 100)]
b = [y for y in range(1, 100)]

answer = []
for value_1 in a:
    intermediate = []
    for value_2 in b:
        init_calc = value_1 ** value_2
        step_one = list(str(init_calc))
        digital = [int(summation) for summation in step_one]
        digital_sum = sum(digital)
        intermediate.append(digital_sum)
    answer.append(max(intermediate))
final_answer = max(answer)
print("The answer is: {}".format(final_answer))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
