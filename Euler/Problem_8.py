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
#print(len(thousand))
length = len(thousand)-4
value_list = []
n = 0
for i in range(0,length):
	combined = int(thousand[n])*int(thousand[n+1])*int(thousand[n+2])*int(thousand[n+3])
	n+=1
	value_list.append(combined)

print(value_list)
#print(max(value_list))
#print(len(value_list))
'''
while len(value_list) < len(thousand)-13:
	n = 0
	for 
'''
size = []
product = [int(thousand[0])]
n=0
for test in range(0,2):
	y = int(thousand[n])
	for i in range(0,4):
		x = int(thousand[n+i])
		size.append(x)	
		print(size)
		
		f
	del size[:4]
	
	n+=1

	
