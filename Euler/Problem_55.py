import numpy as np
from time import time
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# How many Lychrel numbers are there below ten-thousand?
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

start_time = time()

'''
The maximum iteration value is less than 50.
'''

def isPalindrome(integer_input):
    stringer = str(integer_input)
    if stringer == stringer[::-1]:
        return True
    else:
        return False

def flipper(integer_number, counter=1):
    counter += 1
    string_conversion = str(integer_number)
    flipped_string = string_conversion[::-1]
    back_to_integer = int(flipped_string)
    final_answer = integer_number + back_to_integer
    palindrome_checker = isPalindrome(final_answer)
    if palindrome_checker:
        return final_answer
    if counter == 50:
        return False
    else:
        return flipper(final_answer, counter)
solution = []
for iterable in range(1, 10001):
    x = flipper(iterable)
    if x == False:
        solution.append(iterable)
print("The answer is: {}".format(len(solution)))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
