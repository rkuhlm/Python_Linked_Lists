data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200
counter_min = 0
counter_max = 0

for index, value in enumerate(data):
    if value <= min_valid:
        counter_min = counter_min + 1
    elif value >= max_valid:
        counter_max = counter_max + 1

print(counter_min)
print(counter_max)

del data[:counter_min]
counter_max = len(data) - counter_min
del data[counter_max:]

print(data)

# Both do the same thing

# stop = 0
# for index, value in enumerate(data):
#   if value >= min_valid:
#      stop = index
#     break

# print(stop)
# del data[:stop] # up to but not including STOP
# print(data)

# for num, val in enumerate(data):
# if val >= max_valid:
#    stop = num
#   break

# print()
# print(num)
# del data[num:]
# print(data)
