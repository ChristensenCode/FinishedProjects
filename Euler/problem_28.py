import time

start = time.time()
total = []
for n in range(1, 1002,2):
    right_corner = n**2
    total.append(right_corner)

    left_corner = n**2-(n-1)
    total.append(left_corner)

    bottom_left = n**2-2*(n-1)
    total.append(bottom_left)

    bottom_right = n**2-3*(n-1)
    total.append(bottom_right)
total_set = set(total)
elapsed = time.time() - start
print(f"The sum of the diagonals is: {sum(total_set)} and was completed in {elapsed} seconds.")