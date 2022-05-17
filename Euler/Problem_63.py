"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
"""
from time import time

counter = 0


def main():
    i = 1
    power = 1
    successes = 0
    total = 0
    while True:
        possible = i ** power
        possible_str = str(possible)
        if len(possible_str) == power:
            successes += 1
            total += 1
        elif len(possible_str) > power:
            power += 1
            i = 1
            if successes == 0:
                return total
            successes = 0
        i += 1


if __name__ == "__main__":
    start_time = time()
    answer = main()
    print("The answer is: {}".format(answer))
    elapsed_time = time() - start_time
    print("The answer was found in {0:.4f} s.".format(elapsed_time))
