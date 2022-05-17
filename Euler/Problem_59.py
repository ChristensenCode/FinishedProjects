import numpy as np
from time import time
from pprint import pprint
from string import ascii_lowercase
from itertools import product

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Decrypt the message and find the sum of the ASCII values in the original text.
# So i need to figure out the key...there are 3 letter with 26 possibilities...
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()
# Reads in the encrypted text
with open('./Problem_59.txt') as f:
    long_values = f.readlines()

# Splits the input file based on comman
list_of_string = long_values[0].split(',')

# Converts the list of strings into integers
list_of_integers = [int(i) for i in list_of_string]

# Generates all the possible keywords.
keywords = [tuple(map(lambda x: ord(x), i)) for i in product(ascii_lowercase, repeat=3)]
threes = [i for i in range(0, len(list_of_string)+1, 3)]

split_inputs = []
for i in range(len(threes)-1):
    start_value = threes[i]
    ending_value = threes[i+1]
    values = tuple(list_of_integers[start_value:ending_value])
    split_inputs.append(values)


def solver():
    # Iterates through the keywords until one creates the phrase ' the ' because i figured the phrase would contain it.
    for keyword in keywords:
        final = []
        words = []
        for i in split_inputs:
            counter = 0
            for index, j in enumerate(i):
                key = keyword[index]
                value = j
                test = value ^ key
                # print('Key Value\t\t', key)
                # print('Message Value\t', value)
                # print('XOR Value\t\t', test)
                # print('*' * 50)
                final.append(test)
                words.append(chr(test))
            if ' the ' in ''.join(words):
                return keyword


def answer_text(keyword):
    # Decrypt the text using the keyword
    final = []
    words = []
    for i in split_inputs:
        for index, j in enumerate(i):
            key = keyword[index]
            value = j
            test = value ^ key
            final.append(test)
            words.append(chr(test))
    return sum(final), ''.join(words)


x = solver()
y = answer_text(x)

print("The answer is: {}".format(y[0]))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
print(y[1])
