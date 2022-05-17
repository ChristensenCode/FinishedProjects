coins = [1, 2, 5, 10, 20, 50, 100, 200]

#==================================================================
# How many different ways can £2 be made using any number of coins?
#==================================================================

'''
1. Start with 200 then start removing values at bigger and bigger increments.
2. Recursively loop through those values and count the number of ways to make 2 pounds.
'''
import math
from time import time
# Benchmarking start time
start_time = time()

# Value to be reduced
starting_value = 200

# Possible change types
change_types = [1, 2, 5, 10, 20, 50, 100, 200]
max_coins = []

for change_type in change_types:
    x = 200/change_type
    x = math.floor(x)
    max_coins.append(x)

coin_counter = 0

coin_counter = 0
for a in range (0, 2):
    remainder_a = starting_value - a * 200
    if remainder_a >= 0:
        for b in range(0, 3):
            remainder_b = remainder_a - b * 100
            if remainder_b >= 0:
                for c in range(5):
                    remainder_c = remainder_b - c * 50
                    if remainder_c >= 0:
                        for d in range(11):
                            remainder_d = remainder_c - d * 20
                            if remainder_d >= 0:
                                for e in range(21):
                                    remainder_e = remainder_d - e * 10
                                    if remainder_e >= 0:
                                        for f in range (41):
                                            remainder_f = remainder_e - f * 5
                                            if remainder_f >= 0:
                                                for g in range (101):
                                                    remainder_g = remainder_f - g * 2
                                                    if remainder_g >= 0:
                                                        coin_counter += 1
                                                    else:
                                                        break
                                            else:
                                                break
                                    else:
                                        break
                            else:
                                break
                    else:
                        break
            else:
                break
    else:
        break
elapsed_time = time() - start_time
print(elapsed_time)
print(coin_counter)
