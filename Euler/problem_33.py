from time import time
from fractions import Fraction
import numpy as np

#==================================================================
# If the product of these four fractions is given in its lowest
# common terms, find the value of the denominator.
#==================================================================

start_time = time()
total_num = []
total_den = []
values = []
for numerator in range(10, 100):
    for denominator in range(10, 100):
        if numerator > denominator:
            continue
        else:
            correct_fraction = numerator / denominator
            combined = str(numerator) + str(denominator)
            if combined[1] == combined[2] and int(combined[3]) != 0 and correct_fraction != 1:
                integer_numerator = int(combined[0])
                integer_denominator = int(combined[3])
                possible_fraction = integer_numerator / integer_denominator
                if possible_fraction == correct_fraction:
                    total_num.append(integer_numerator)
                    total_den.append(integer_denominator)
                    values.append(possible_fraction)
            else:
                continue
elapsed_time = time() - start_time
print(elapsed_time)
values_nparray = np.array(values)
values_prod = np.prod(values_nparray)
string_values_prod = str(values_prod)
string_values_prod = string_values_prod[:4]
print(Fraction(string_values_prod))
