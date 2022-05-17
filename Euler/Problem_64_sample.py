from math import sqrt
from time import time


def main():
    upperbound = 10000
    result = 0
    for n in range(2, upperbound + 1):
        limit = int(sqrt(n))
        if limit * limit == n:
            continue
        period = 0
        d = 1
        m = 0
        a = limit
        while a != 2 * limit:
            m = int(d * a - m)
            d = int((n - m * m) / d)
            a = int((limit + m) / d)
            period += 1
        if period % 2 == 1:
            result += 1
    return result


if __name__ == "__main__":
    start_time = time()
    answer = main()
    print("The answer is: {}".format(answer))
    elapsed_time = time() - start_time
    print("The answer was found in {0:.4f} s.".format(elapsed_time))
