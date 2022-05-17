import time

start_time = time.time()
max_number = (9 ** 5 * 10) // 3
new_max = 9 ** 5 * len(str(max_number))
cool_number = []

for i in range(2, max_number + 1):
    string_number = str(i)
    number_storage = []
    for v in string_number:
        fifth_power = int(v) ** 5
        number_storage.append(fifth_power)
    if i == sum(number_storage):
        cool_number.append(i)
elapsed_time = time.time() - start_time

print(f"The answer is {sum(cool_number)} in {elapsed_time:.2f} seconds.")
