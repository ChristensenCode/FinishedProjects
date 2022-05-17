import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Find the last ten digits of the series,
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
bases = np.arange(1, 1001, dtype=object)
answer = bases ** bases
answer_object = np.sum(answer)
answer_string = str(answer_object)
answer_length = len(answer_string)
final_answer = answer_string[answer_length-10:]

print('The answer is {}'.format(final_answer))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))

