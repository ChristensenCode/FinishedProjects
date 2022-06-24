"""
Using the numbers 1 to 10, and depending on arrangements, 
it is possible to form 16- and 17-digit strings. 
What is the maximum 16-digit string for a "magic" 5-gon ring?
"""
from itertools import permutations, combinations, product
from time import time

start_time = time()
numbers = set(range(1, 11))
possible_values = list(permutations(numbers, r=3))
solutions = []
winner_winner = 0
for lengths in range(27, 13, -1):
    proper_sums = list(filter(lambda x: sum(x) == lengths, possible_values))
    for first_term in proper_sums:
        possible_seconds = filter(lambda x: first_term[-1] == x[1], proper_sums)
        for second_term in possible_seconds:
            possible_thirds = filter(lambda x: second_term[-1] == x[1], proper_sums)
            for third_term in possible_thirds:
                possible_fours = filter(lambda x: third_term[-1] == x[1], proper_sums)
                for fourth_term in possible_fours:
                    possible_fives = filter(
                        lambda x: fourth_term[-1] == x[1], proper_sums
                    )
                    for fifth_term in possible_fives:
                        middles = [
                            str(first_term[1]),
                            str(second_term[1]),
                            str(third_term[1]),
                            str(fourth_term[1]),
                            str(fifth_term[1]),
                        ]
                        together = (
                            first_term
                            + second_term
                            + third_term
                            + fourth_term
                            + fifth_term
                        )
                        if len("".join(map(str, together))) != 16:
                            continue
                        all_present = set(together)

                        # All the middles need to be unique and all the numbers 1-10 need to appear
                        if len(set(middles)) != len(middles) or len(all_present) != 10:
                            continue

                        # the middle of the first terms needs to be the same as the last
                        # value of the last term.
                        if fifth_term[-1] == first_term[1]:
                            part_one = list(
                                [
                                    first_term,
                                    second_term,
                                    third_term,
                                    fourth_term,
                                    fifth_term,
                                ]
                            )

                            # puts list into smallest first while maintaining order.
                            smallest_start = min(map(lambda x: x[0], part_one))
                            answer_reorganized = part_one.copy()
                            for part in part_one:
                                if part[0] == smallest_start:
                                    break
                                x = answer_reorganized.pop(
                                    answer_reorganized.index(part)
                                )
                                answer_reorganized.append(x)

                            solutions.append(answer_reorganized)
                            combine_tuples = "".join(
                                map(str, sum(answer_reorganized, ()))
                            )
                            if int(combine_tuples) > winner_winner:
                                winner_winner = int(combine_tuples)
print("The answer is: {}".format(winner_winner))
elapsed_time = time() - start_time
print("The answer was found in {0:.4f} s.".format(elapsed_time))
