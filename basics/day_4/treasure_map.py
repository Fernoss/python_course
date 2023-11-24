# x marks the spot
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map_grid = [line1, line2, line3]

# Asking for coordinates
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to bury the treasure?\n"
                 "  A   B   C\n"
                 "1\n"
                 "2\n"
                 "3\n"
                 "Choose a number and a letter.\n")

# splitting input into a list
coordinates_from_input = position.split(",")

# assigning coordinates
number_one = int(coordinates_from_input[0]) - 1
# print(number_one), testing
# print(type(number_one)), testing

if coordinates_from_input[1] == "A":
    number_two = 0
elif coordinates_from_input[1] == "B":
    number_two = 1
else:
    number_two = 2

map_grid[number_one][number_two] = str("X")
print(f"Your map:")
print(f"{line1}\n{line2}\n{line3}")