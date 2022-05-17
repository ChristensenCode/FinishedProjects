from time import time
from numba import njit, prange
import pandas as pd


@njit
def apply_calc(n):
    if n % 2 == 0:
        return n/2
    return 3 * n + 1


@njit
def calculate_term_number_length(guess_value):
    term_list = []
    starting_value = guess_value
    while True:
        term_list.append(guess_value)
        guess_value = apply_calc(guess_value)
        if guess_value == 1:
            term_list.append(1)
            return starting_value, len(term_list)


start_time = time()
array_values = []
for i in prange(13, 1000000):
    array_values.append(calculate_term_number_length(i))
df = pd.DataFrame(array_values, columns=['guess_value', 'sequence_length'])
elapsed_time = time() - start_time
print(f'Total Time {elapsed_time}')
starting_number = df.iloc[df.sequence_length.argmax()][0]
chain_length = df.iloc[df.sequence_length.argmax()][1]
print(f"The answer is {starting_number} with a length of {chain_length}")
