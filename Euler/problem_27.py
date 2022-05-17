from pprint import pprint
import csv
import time


start = time.time()
prime_list = []
with open("gistfile1.txt") as csvfile:
    primes = csv.reader(csvfile, delimiter = ',')
    for prime in primes:
        prime_list.append(prime)
prime_list = prime_list[0]
#print(prime_list)


ab_dict = {}
for b in prime_list:
    #print(f"B:  {b}")
    #print('-' * 120)
    b = int(b)
    for a in range(-1000, 1001):
        #print(f"A:   {a}")
        #print('-'*60)
        storage = []
        for n in range(0,101):
            #print(f"This is n: {n}")
            value = n**2+a*n+b
            if str(value) in prime_list:
                storage.append(value)
                #print(len(storage))
            else:
                break
        if len(storage) == 1 or len(storage) == 2:
            pass
        else:
            ab_dict.update({(a,b):len(storage)})
#pprint(ab_dict)
answer = max(ab_dict, key=ab_dict.get)
elapsed = time.time() - start
print(elapsed)
print(f"The Answer is: {answer[0]*answer[1]} found in {elapsed} (s).")

