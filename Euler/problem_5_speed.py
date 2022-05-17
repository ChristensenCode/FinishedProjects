import numpy as np
from time import time
unique_values = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
value_to_check = unique_values
flag = True
start_time = time()
while flag:
    modulus_check_values = np.arange(1, 21)
    value_to_check_array = np.ones_like(modulus_check_values) * value_to_check
    possible_answers = value_to_check_array % modulus_check_values
    if sum(possible_answers) == 0:
        flag = False
    else:
        value_to_check += unique_values
elapsed_time = time() - start_time
print(f'Total Time {elapsed_time}')
print(f"The answer is {value_to_check}.")
