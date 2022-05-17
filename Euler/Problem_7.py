# Problem 7 100001st Prime

primes = []
number = 1000000

for x in range(2, number+1):
	isPrime = True
	for y in range(2, int(x**0.5)+1):
		if x%y ==0:
			isPrime = False
			break
	if isPrime:
		primes.append(x)
	if len(primes) == 10001:
		print(primes[-1])
		break
