# Problem 12 Highly Divisible Triangular Number

divisors = []
n = 10
max = 10000
min = int(max/2)
'''
for x in range(1,max):
	print('x: '+str(x))
	for value in range(1,x+1):
		
		n+=1
		if x % value == 0:
			divisors.append(value)
	if sum(divisors) > 76576500:
		print(divisors)
		print(sum(divisors))
		break
	divisors = []

print('done')
print(n)
'''
'''

max = 10000000
min = int(max/2)
from functools import reduce
from math import sqrt

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

for x in range(min,max):
	test = factors(x)
	if len(test)>500:
		print(sum(test))
		break
print('done')
'''

import time
# Solution from JasonbHill
def num_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors
 
def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n
 
start = time.time()
index = find_triangular_index(500)
triangle = (index * (index + 1)) / 2
elapsed = (time.time() - start)
 
print ("result %s returned in %s seconds." % (triangle,elapsed))