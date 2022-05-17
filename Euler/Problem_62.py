"""
The cube, 41063625 (3453), can be permuted to produce two other cubes:
56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly
five permutations of its digits are cube.
"""

from time import time


def main():
    # This was the 3 value so i might as well start here
    value_to_check = 346
    possibles = {}
    while True:
        # Calculates the cube of the number
        cubed_values = value_to_check * value_to_check * value_to_check
        cubed_value_to_str = tuple(sorted(str(cubed_values)))
        if cubed_value_to_str in possibles.keys():
            possibles[cubed_value_to_str].append(value_to_check)
            if len(possibles[cubed_value_to_str]) == 5:
                return min(possibles[cubed_value_to_str]) ** 3
        else:
            possibles[cubed_value_to_str] = [value_to_check]
        value_to_check += 1


if __name__ == "__main__":
    start_time = time()
    answer = main()
    print(answer)
    print("The answer is: {}".format(answer))
    elapsed_time = time() - start_time
    print("The answer was found in {0:.4f} s.".format(elapsed_time))
