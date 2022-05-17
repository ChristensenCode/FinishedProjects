# Problem 18
'''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

# From Jason

import time

# define a recursive function to create partial sums by row
def recSumAtRow(rowData, rowNum):
    # iterate over the given row
    for i in range(len(rowData[rowNum])):
        # add the largest of the values below-left or below-right
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
    # base case
    if len(rowData[rowNum])==1: return rowData[rowNum][0]
    # recursive case
    else: return recSumAtRow(rowData, rowNum-1)

	#Imports the data stored in problem18.txt
rows = []
with open('problem18.txt') as f:
	for line in f:

		rows.append([int(i) for i in line.rstrip('\n').split(" ")])
		print(rows)

start = time.time()
result = recSumAtRow(rows, len(rows)-2) # start at second to last row
elapsed = time.time() - start
 
 
print("%s found in %s seconds" % (result ,elapsed))