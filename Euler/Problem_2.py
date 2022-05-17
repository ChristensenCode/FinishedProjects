# Even Fibonacci Numbers

fib = [1,2]
value = True

while fib[-1] < 4000000:
	test = fib[-1]+fib[-2]
	fib.append(test)	
	print(fib)
	
	even = []
	for value in fib:
		if value % 2 == 0:
			even.append(value)
			print(even)
	total = sum(even)
print(total)	