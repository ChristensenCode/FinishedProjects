# Multiples of 3 and 5
import sys
import matplotlib as plt

three = []
five = []

for value in range(1,1000):
	if value % 3 == 0:
		three.append(value)
	elif value % 5 == 0:
		five.append(value)
	else:
		print('')
total = sum(three)+sum(five)
print(total)
print("test")
