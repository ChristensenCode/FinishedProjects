# Largest Palindrome Product

palin = []
repeats = range(0,1000)
number = range(1,1000)

for x in repeats:
	for y in number:
		pal = x*y
		#print(pal)
		first = str(pal)[:3]		
		#print(first)
		reverse = str(pal)[::-1]
		last = reverse[:3]
		#print(last)
		if first == last:
			palin.append(pal)

print(max(palin))
