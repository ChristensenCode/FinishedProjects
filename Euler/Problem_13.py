# Problem 13 Work out the first ten digits of the sum of the
# one-hundred 50 digits numbers.

f = open('problem_13.txt')
values = f.readlines()
f.close()

matrice = []
for value in values:
	x = value.replace('\n','')
	matrice.append(x)

print(matrice)

i = 0
total = 0
for n in range(1,101):
	total = int(matrice[i])+total
	print(total)
	i += 1
test = str(total)
print(test[0:10])