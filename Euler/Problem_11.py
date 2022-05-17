# Problem 11 Largest Product in Grid
import numpy as np

f = open('problem11.txt')
values = f.readlines()
f.close()

matrice = []
for value in values:
	x = value.replace('\n','')
	matrice.append(x)


matrice[:] = [''.join(matrice[:])]
matrice = str(matrice[0]).replace(' ','')
best = []

# Finds the greatest horizontal multiple.
f = 0
s = 1
v = []
quad = []
product = []
L1 = matrice
next = 0

for row in range(1,21):
	f = 0+next
	s = 1+next	
	for plus in range(1,34,2):
		for test1 in range(0,4):
			if int(L1[f]) == 0:
				quad.append(int(L1[s]))
			else:
				both = int(L1[f:s+1])
				quad.append(both)
			f+=2
			s+=2
		prod = np.prod(np.array(quad))
		product.append(prod)
		quad = []
		f = 1+plus
		s = 2+plus

	quad = []
	next = next+40
best.append(max(product))

# Finds the greatest vertical multiple.
f = 0
s = 1
i = 0
next = 0
v = []
quad = []
product = []
for row in range(1,18):
	f = 0+next
	s = 1+next	
	for plus in range(1,40,2):
		for test1 in range(0,4):
			if int(L1[f]) == 0:
				quad.append(int(L1[s]))
			else:
				both = int(L1[f:s+1])
				quad.append(both)
			f+=40
			s+=40
		prod = np.prod(np.array(quad))
		product.append(prod)
		quad = []
		f = 1+plus+next
		s = 2+plus+next

	quad = []
	next = next+40
best.append(max(product))

# Finds the greatest diagonal multiple (right to left).
f = 0
s = 1
i = 0
next = 0
v = []
quad = []
product = []
for row in range(1,18):
	f = 0+next
	s = 1+next
	for plus in range(1,34,2):
		for test1 in range(0,4):
			if int(L1[f]) == 0:
				quad.append(int(L1[s]))
			else:
				both = int(L1[f:s+1])
				quad.append(both)
			f += 42
			s += 42
		prod = np.prod(np.array(quad))
		product.append(prod)
		quad = []
		f = 1+plus+next
		s = 2+plus+next
	quad = []
	next = next+40
best.append(max(product))

# Finds the greatest diagonal multiple (left to right)

f = 0
s = 1
i = 0
next = 0
v = []
quad = []
product = []
for row in range(1,18):
	f = 120+next
	s = 121+next	
	for plus in range(1,34,2):
		for test1 in range(0,4):
			if int(L1[f]) == 0:
				quad.append(int(L1[s]))
			else:
				both = int(L1[f:s+1])
				quad.append(both)
			f = f-38
			s = s-38
		prod = np.prod(np.array(quad))
		product.append(prod)
		quad = []
		f = 1+plus+120+next
		s = 2+plus+120+next
	quad = []
	next = next+40
best.append(max(product))
winner = max(best)
print(best)
print(winner)