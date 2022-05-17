# Problem 17 Number Letter Counts
ones = ['one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
hundreds = ['hundred']
ands = ['and']
thousands = ['thousand']

l_ones = []
l_teens = []
l_tens = []
l_hundreds = []
l_thousands = []
l_ands = []

# Length of Ones
for i in range(len(ones)):
	total_length = len(ones[i])
	l_ones.append(total_length)
print(sum(l_ones))

# Length of Teens
for i in range(len(teens)):
	total_length = len(teens[i])
	l_teens.append(total_length)
print(sum(l_teens))

# Length of Hundreds
for i in range(len(hundreds)):
	total_length = len(hundreds[i])
	l_hundreds.append(total_length)
print(sum(l_hundreds))

# Length of Ands
for i in range(len(ands)):
	total_length = len(ands[i])
	l_ands.append(total_length)
print(sum(l_ands))

sums = sum(l_ones)*9*11+sum(l_teens)*10+sum(l_hundreds)*99*10+sum(l_ands)*99*10+len(thousands)
print(sums)

# from 1 to 99
# you use 9 x ones
#         1 x teens 
#         8 x tens
#         total = length(ones)*9+length(teens)+length(tens)*8
# from 100 to 999
# you use 9 x hundreds
#         81 x ones
#         10 x teens
#         99 x ands
