# Problem 9 Special Pythagorean Triplet
import numpy as np
	
for b in range(1,501):
	top = 10**6-2000*b
	bottom = 2000-2*b
	a = top/bottom
	if a > 0:
		if int(a) == a and isinstance(a,float) == True:
			c = 1000-a-b
			if a < b:
				if a**2+b**2 == c**2:
					print(int(a*b*c))