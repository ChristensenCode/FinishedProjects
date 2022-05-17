# Problem 24
# Lexicographic Permutations

import itertools

numbers = [0,1,2,3,4,5,6,7,8,9]
perm = itertools.permutations(numbers)
perms_24 = []
for i in list(perm):
    perms_24.append(i)
million = 10**6
answer = perms_24[million-1]
print(answer)
answer_string = ''
for value in perms_24[million-1]:
    answer_string = answer_string+str(value)
print(answer_string)
