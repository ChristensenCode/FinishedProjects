import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Find the sum of all 0 to 9 pandigital numbers with this property.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
d8 = [str(x) for x in range(100, 1001) if x % 17 == 0 and len(str(x)) == len(set(str(x)))]

# Function creates a list of possible 3 digit items according to divisibility
def pandigital_finder(divider, plus_one_list):
    three_digit_holder = []
    for individual in plus_one_list:
        for i in range(10):
            i_string = str(i)
            level = i_string + individual[:2]
            if int(level) % divider == 0 and len(level) == len(set(level)):
                three_digit_holder.append(level)
    return three_digit_holder


def pandigital_combiner(lower_list, upper_list):
    combined_list = []
    for i in upper_list:
        for j in lower_list:
            possible_combined = j[0] + i
            possible_combined_length = len(possible_combined)
            possible_combined_set = set(possible_combined)
            if j[1:] == i[:2] and possible_combined_length == len(possible_combined_set):
                combined_list.append(possible_combined)
    return combined_list

sub_string_dict = {'d8':d8}
for i in reversed(range(2, 8)):
    divide_values = [2, 3, 5, 7, 11, 13]
    sub_string_dict['d'+str(i)] = pandigital_finder(divide_values[i-2], sub_string_dict['d'+ str(i+1)])

paired_down = {}
paired_down['final'] = pandigital_combiner(sub_string_dict['d7'], sub_string_dict['d8'])
for i in reversed(range(3, 8)):
    lower_list = sub_string_dict['d' + str(i-1)]
    paired_down['final'] = pandigital_combiner(lower_list, paired_down['final'])
final_answer = []

for i in range(10):
     for j in paired_down['final']:
        winning = str(i) + j
        if len(winning) == len(set(winning)):
            final_answer.append(int(winning))
final_summation = sum(set(final_answer))
print('The answer is {}.'.format(final_summation))

elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
