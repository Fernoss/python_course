import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# to create random letters for the amount of the input
letters_list = []
for n in range(1, nr_letters + 1):
    letters_list.append(letters[random.randint(0,51)])

# to create random symbols for the amount of the input
symbols_list = []
for n in range(1, nr_symbols + 1):
    symbols_list.append(symbols[random.randint(0, 8)])

# to create random numbers for the amount of the input
numbers_list = []
for n in range(1, nr_numbers + 1):
    numbers_list.append(random.randint(0,9))

print(letters_list)
print(symbols_list)
print(numbers_list)

# total_characters = nr_symbols + nr_numbers + nr_letters
# for n in range(1, total_characters + 1):

letters_pass = ""
for n in range(0, len(letters_list)):
    letters_pass += letters_list[n]

print(letters_pass)

numbers_pass = ""
for n in range(0, len(numbers_list)):
    numbers_pass += str(numbers_list[n])

print(numbers_pass)

symbols_pass = ""
for n in range(0, len(symbols_list)):
    symbols_pass += symbols_list[n]

print(symbols_pass)
print(f"Your passwd is: {letters_pass}{numbers_pass}{symbols_pass}")