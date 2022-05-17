# Problem 25
# Fibonacci Sequence

starting = [1,1]
n = 1

while True:
    n2 = starting[n]+starting[n-1]
    if len(str(n2)) == 1000:
        break
    else:
        starting.append(n2)
        n += 1

print(len(starting)+1)
