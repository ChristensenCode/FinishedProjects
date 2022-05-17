# Problem 26
# Reciprocal Cycles
# How do i get a list of decimals?
from pprint import pprint

dict = {}
for test_number in range(2,1001):
    n = 0
    remainder_test_number = 1 % test_number
    multi_ten = remainder_test_number * 10
    repeater = [remainder_test_number]
    while True:
        value_dict = {test_number:repeater}
        next_value = multi_ten % test_number
        multi_ten = next_value * 10
        n += 1
        if next_value in repeater and n > 0:
            break
        repeater.append(next_value)
    dict.update(value_dict)
    #print(value_dict)

decimal_lengths = []
for v in dict.values():
    decimal_lengths.append(len(v))
print(f'{decimal_lengths.index(max(decimal_lengths))+2} has {max(decimal_lengths)} decimals.')
