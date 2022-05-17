#Problem 6 Squares of Sums Minus Sum of Squares

sum_q = []

for x in range(1,101):
	y = x**2
	sum_q.append(y)
print(sum(sum_q))

n=0
for x in range(1,101):
	n=x+n

square = n**2
print(square)

total = square-sum(sum_q)
print(total)