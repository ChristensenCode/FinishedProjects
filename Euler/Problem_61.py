import numpy as np
from time import time
from collections import OrderedDict
from itertools import islice


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
# are all figurate (polygonal) numbers and are generated
# by the following formulae:
# Triangle	 	    P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Square	 	    P4,n=n2	 	        1, 4, 9, 16, 25, ...
# Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	    	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
# Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
# Octagonal	 	    P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
# The ordered set of three 4-digit numbers: 8128, 2882, 8281,
# has three interesting properties.
#
# The set is cyclic, in that the last two digits of each number
# is the first two digits of the
# next number (including the last number with the first).
# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281),
# and pentagonal (P5,44=2882),
# is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.
# Find the sum of the only ordered set of six cyclic 4-digit numbers
# for which each polygonal type: triangle, square, pentagonal, hexagonal,
# heptagonal, and octagonal,
# is represented by a different number in the set.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
start_time = time()


def tri(start, end):
    values = np.arange(start, end)
    return values * (values + 1) / 2


def square(start, end):
    values = np.arange(start, end)
    return values ** 2


def penta(start, end):
    values = np.arange(start, end)
    return values * (3 * values - 1) / 2


def hexa(start, end):
    values = np.arange(start, end)
    return values * (2 * values - 1)


def hepta(start, end):
    values = np.arange(start, end)
    return values * (5 * values - 3) / 2


def octo(start, end):
    values = np.arange(start, end)
    return values * (3 * values - 2)


def clean_third_zeroes(array_to_check):
    return np.array(list(filter(lambda x: "0" != x[2], array_to_check)))


tris = clean_third_zeroes(tri(45, 141).astype("int").astype("str"))
squares = clean_third_zeroes(square(32, 99).astype("int").astype("str"))
pentas = clean_third_zeroes(penta(26, 82).astype("int").astype("str"))
hexes = clean_third_zeroes(hexa(24, 71).astype("int").astype("str"))
heptas = clean_third_zeroes(hepta(21, 64).astype("int").astype("str"))
octos = clean_third_zeroes(octo(20, 59).astype("int").astype("str"))

collective = {
    "squares": squares,
    "pentas": pentas,
    "hexes": hexes,
    "heptas": heptas,
    "octos": octos,
}

all_keys = {
    "tris",
    "squares",
    "pentas",
    "hexes",
    "heptas",
    "octos",
}


def recursive_function(dict_to_check, chain=OrderedDict()):
    copy_dict = {}
    value = ""
    last_value = list(chain.items())[-1]
    last_two = last_value[0][2:]
    for key, values in dict_to_check.items():
        for value in values:
            first_two = value[:2]
            if last_two == first_two:
                copy_dict = dict_to_check.copy()
                del copy_dict[key]
                sliced = {}
                for index, chains in enumerate(chain):
                    if value[:2] == chains[:2]:
                        sliced = OrderedDict(islice(chain.items(), index))
                        sliced[value] = key
                        recursive_function(copy_dict, chain=sliced)
                        # Logical Checks
                        valuable = sliced.values()
                        # removes repeated values since each is unique
                        unique_check = len(set(valuable)) == len(valuable)

                        # The final value should only be 6
                        length_check = len(sliced) == 6
                        first_value = list(islice(sliced.keys(), 1))[0][:2]
                        part_one_last = len(list(sliced)) - 1
                        part_two_last = len(list(sliced))
                        last_value = list(
                            islice(
                                sliced, part_one_last, part_two_last
                            )
                        )
                        last_value = last_value[0][2:]
                        # The last value should continue the first
                        linked = first_value == last_value
                        if unique_check and length_check and linked:
                            sliced = list(sliced)

                            # Makes sure the final value actual works
                            correct = False
                            for index, thingy in enumerate(
                                list(sliced)[: len(sliced) - 1]
                            ):
                                x = thingy[2:]
                                y = sliced[index + 1][:2]
                                if x != y:
                                    correct = False
                                    break
                                correct = True
                            if correct:
                                elapsed_time = time() - start_time
                                sliced = map(lambda x: int(x), sliced)
                                print(
                                    f"The answer {sum(list(sliced))} " +
                                    f"was found in {elapsed_time} s."
                                )

                else:
                    chain[value] = key
                    recursive_function(copy_dict, chain=chain)


for tri_value in tris:
    recursive_function(collective, chain=OrderedDict({tri_value: "tri"}))
