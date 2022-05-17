# Largest Prime Factor
import numpy as np

euler = 600851475143

n = euler
i = 2

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1
print(i)	
print (n)