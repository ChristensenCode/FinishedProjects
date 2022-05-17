from time import time
from numba import njit

# ==================================================================
# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.
# ==================================================================

start_time = time()
summations = set()
pandigital = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# pandigital = range(1, 10)


def set_length_checker(original):
    if len(set(original)) != len(original):
        return True
    return False


for i in range(1, 49):
    string_i = str(i)
    if set_length_checker(string_i):
        continue
    for j in range(1, 1964):
        string_j = str(j)
        if set_length_checker(string_j):
            continue
        product = i * j
        string_product = str(product)
        if set_length_checker(string_product):
            continue

        value = "{}{}{}".format(string_i, string_j, string_product)
        integer_value = int(value)
        sorted_integer_value = sorted(value)
        if sorted_integer_value == pandigital:
            summations.add(product)

elapsed_time = time() - start_time
print(f"The answer is {sum(summations)} in {elapsed_time:.2f} seconds.")
