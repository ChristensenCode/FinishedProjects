# Evaluate the Sum of all amicablew numbers under 1000
import math
n2c = 10000

value = [x for x in range(1,n2c+1)]
amicable_numbers = []
for number in value:
    amicable_list = []
    for i in range(1,number+1):
        if number == i:
            continue
        elif number % i == 0:
            amicable_list.append(i)
    sum_amicable = sum(amicable_list)
    level_2 = []
    for n in range(1,sum_amicable+1):
        if n == sum_amicable:
            continue
        elif sum_amicable % n == 0:
            level_2.append(n)
    sum_level_2 = sum(level_2)
    if sum_level_2 == number:
        if sum_level_2 == sum_amicable:
            continue
        else:
            amicable_numbers.append(sum_level_2)
print(amicable_numbers)
answer = sum(amicable_numbers)
print(answer)
