"""Practice with List syntax."""

# initialize an empty list of floats with the name my_numbers
my_numbers: list[float] = []  # <- literal

# add the value 1.5 to numbers

my_numbers.append(1.5)

print(my_numbers)

game_points: list[int] = [102, 86, 94]

# prints out 94.

print(game_points[2])

# change 86 to 72

game_points[1] = 72

# print length of list

len(game_points)

# removing an item from a list

game_points.pop(1)  # pop to an index, depsite having parentheses

print(game_points)
