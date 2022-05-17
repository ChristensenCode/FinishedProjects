from time import time
from math import factorial

# ==================================================================
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
# ==================================================================

start_time = time()

fact_dict = {}
visual_fact_dict = {}
for i in range(3, 50000):
    string_i = str(i)
    fac_total = []
    digits = []
    for j in string_i:
        integer_j = int(j)
        fac_total.append(factorial(integer_j))
        digits.append(integer_j)
    if sum(fac_total) == i:
        fact_dict[i] = fac_total
        blank_string = ""
        counter = 0
        for k in digits:
            visual = "{}! ".format(k)
            if counter < len(digits)-1:
                blank_string = blank_string + visual + '+ '
            else:
                blank_string = (blank_string + visual).strip()
            counter += 1
        visual_fact_dict[i] = blank_string

answer = []
for key, value in visual_fact_dict.items():
    answer.append(key)
    formatted_string = value + ' = ' + str(key)
    print(formatted_string)
elapsed_time = (time() - start_time)
print("Compute Time: " + str(elapsed_time) + " seconds")
print("The answer is: {}".format(sum(answer)))
