import time
import numpy as np
from numba import njit


def string_splitter(string_array):
    return sum((int(i) ** 5 for i in list(string_array)))


def main_numpy_version():
    start_time = time.time()
    max_number = (9 ** 5 * 10) // 3
    possibles = np.arange(2, max_number + 1).astype("str")
    possibles_ints = possibles.astype("int32")
    faster_string_splitter = np.vectorize(string_splitter)
    quinted = np.array(faster_string_splitter(possibles))
    good_ones = np.equal(possibles_ints, quinted)
    elapsed_time = time.time() - start_time

    print(
        f"The answer is {sum(possibles_ints * good_ones)} in {elapsed_time:.2f} seconds."
    )


def main_original():
    start_time = time.time()
    max_number = (9 ** 5 * 10) // 3
    cool_number = 0

    for i in range(2, max_number + 1):
        string_number = str(i)
        number_storage = sum((int(i) ** 5 for i in list(string_number)))
        if i == number_storage:
            cool_number += i
    elapsed_time = time.time() - start_time

    print(f"The answer is {cool_number} in {elapsed_time:.2f} seconds.")


if __name__ == "__main__":
    main_numpy_version()
    main_original()
