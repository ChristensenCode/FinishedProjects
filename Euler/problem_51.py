import numpy as np
from time import time
from pprint import pprint
import re

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Find the smallest prime which, by replacing part of the
# number (not necessarily adjacent digits) with the same
# digit, is part of an eight prime value family.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

start_time = time()
prime_list = primesfrom2to(1000000)[4:]
ending = [1, 3, 7, 9]
regulars = [1, 3, 5, 7, 9]
stringPrimes = [str(x) for x in prime_list]

possibles = []
for numberCount in stringPrimes:
    for numberCheck in range(10):
        if numberCount.count(str(numberCheck)) == 3:
            # print(numberCount)
            indices = [i for i, a in enumerate(numberCount) if a == str(numberCheck)]
            possibles = []
            for value in range(10):
                numberList = list(numberCount)
                numberList[indices[0]] = str(value)
                numberList[indices[1]] = str(value)
                numberList[indices[2]] = str(value)
                ListToInteger = "".join(numberList)
                if len(str(int(ListToInteger))) == len(ListToInteger) and int(ListToInteger) in prime_list:
                    possibles.append(int(ListToInteger))
                    if len(possibles) == 8:
                        answer = possibles
print("The answer is: {}".format(answer[0]))
elapsed_time = time() - start_time
print('The answer was found in {0:.4f} s.'.format(elapsed_time))
