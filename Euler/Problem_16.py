# Problem 16 Power Digit Sum
x = 2**1000
print(x)
value = str(2**1000)
totalling = []
for i in range(len(value)):
	total = int(value[i])
	totalling.append(total)
print(sum(totalling))