import numpy as np
from time import time
from pprint import pprint
import re
import collections

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# What is the largest 1 to 9 pandigital 9-digit number
# that can be formed as the concatenated product of an
# integer with (1,2, ... , n) where n > 1?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
counter = 1
x = [i for i in range(1, 10)]
zero_checker = re.compile("[0]")
possibles = []
information = {}
for i in range(1, 10000):
    for j in range(1, 10):
        condition_array = i * np.array(x[:j])
        condition_list = condition_array.tolist()
        condition_list_string = [str(i) for i in condition_list]
        combined = "".join(condition_list_string)
        combined_set = set(combined)
        combined_length = len(combined)
        combined_set_length = len(combined_set)

        if (
            re.search(zero_checker, combined) is None
            and len(combined) == 9
            and combined_length == combined_set_length
        ):
            information[i] = [int(combined), (x[:j])]
            possibles.append(int(combined))

print("The answer is {}.".format(max(possibles)))
elapsed_time = time() - start_time
print("The answer was found in {0:.4f} s.".format(elapsed_time))

