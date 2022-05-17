# Problem 10


primes = []
number = 2000000

for x in range(2,number):
	isPrime = True
	for y in range(2,int(x**0.5)+1):
		if x%y ==0:
			isPrime = False
			break
	if isPrime:
		primes.append(x)

print(sum(primes))