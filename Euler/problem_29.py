power_list = []
for a in range(2, 101):
    for b in range(2, 101):
        powers = a ** b
        power_list.append(powers)
print(len(power_list))

power_set = set(power_list)
print(len(power_set))