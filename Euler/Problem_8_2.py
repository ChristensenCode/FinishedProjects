# Problem 8 Largest product in a series
import sys
f = open('problem8.txt','r')
values = f.readlines()
f.close()

thousand = []
for value in values:
	x = value.replace('\n','')
	thousand.append(x)

thousand[:] = [''.join(thousand[:])]
thousand = str(thousand[0])

length = len(thousand)-13
# This list will contain the first 13 numbers in the list.
size = []
product = [int(thousand[0])]
n=0
# Shifts the starting number from the start to the next value.
for test in range(0,length):
	y = int(thousand[n])
	for i in range(0,13):
		x = int(thousand[n+i])
		size.append(x)
		# Parses the big number into a list of 13.
		
	for v in range(1,13):
		if v > 0:
			y = size[v]*y
	# Multiples the starting value by the previous to get the product.		
	product.append(y)
	# Clears the list to start fresh.
	del size[:13]
	n+=1
# Searches through the list to find the largest value.
print(max(product))
	
