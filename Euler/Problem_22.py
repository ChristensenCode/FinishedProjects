# Problem 22
# Sort the list an alphabetical order.
# Assign a numerical value to each letter.
# what is the sum of all the names?
from pprint import pprint
import csv
import string

name_list = []
values = []
with open('problem_22.txt') as file:
    for name in file:
        test = name.split(',')
        for i in test:
            name_length = len(i)
            new_i = i[1:name_length-1].strip()
            name_list.append(new_i)
sorted_name_list = sorted(name_list,key = str)
alphabet = string.ascii_uppercase
a_dict = {}
for k,letter in enumerate(alphabet):
    a_dict[letter] = k+1
print(a_dict)

n = 0
for name in sorted_name_list:
    n += 1
    name_worth = []
    print(f'Name: \t{name}')
    print(f'Rank: \t{n}')
    for letter in name:
        letter_conversion = a_dict[letter]
        name_worth.append(letter_conversion)
        total_name_worth = sum(name_worth)*n
    values.append(total_name_worth)
print(f'Answer:\t{sum(values)}')
