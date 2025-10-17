data = [104, 105, 110, 4, 120, 130, 130, 360, 150,
        160, 170, 350, 183, 185, 5,  187, 188, 191]

min_valid = 100
max_valid = 200

# This will go through the list backwards and remove the values that are not in range
# We do not need the list to be sorted for this
for index in range(len(data)-1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        del data[index]


# This will also loop through the list in reverse
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        del data[top_index - index]
