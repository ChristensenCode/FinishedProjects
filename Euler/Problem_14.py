# Problem 14 Which starting number, under one million, will
# produce the longest chain?
from timeit import default_timer as timer
'''
start = timer()
chain = []
length = []
for n in range(1,1000001):
	entry = n
	if n % 2 != 0:
		chain = []
		while n != 1:
			if n % 2 == 0:
				n = n/2
			else:
				n = 3*n+1
			chain.append(n)
		length.append(len(chain))

		maximum = max(length)
print('Largest Starting Value: '+str(length.index(maximum)*2+1))
end = timer()
print(end-start)
'''
import time
start = time.time()
# This code was faster becase he appended only maximum values
# that were longer than previous ones. Mine were appending every
# time which took additional computer resources.
def collatz(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return count
 
max = [0,0]
for i in range(1000000):
    c = collatz(i)
    if c > max[0]:
        max[0] = c
        max[1] = i
 
elapsed = (time.time() - start)
print ("found %s at length %s in %s seconds" % (max[1],max[0],elapsed))