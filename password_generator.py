# RaghavaB

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

len_pass = int(input("Enter the length of the password : "))
len_letter = int(input("Enter the number of letters needed : "))
len_number = int(input("Enter the number of numbers needed : "))
len_symbol = int(input("Enter the number of symbols needed : "))
pass_ = []

if (len_letter + len_number + len_symbol) > len_pass:
    print("The entered number of required char does not match the needed length for the password.")

for i in range(1, len_letter+1):
    loc = random.randint(0, 31)
    pass_.append(letters[loc])

for i in range(1, len_number+1):
    loc = random.randint(0, 9)
    pass_.append(numbers[loc])

for i in range(1, len_symbol+1):
    loc = random.randint(0, 8)
    pass_.append(symbols[loc])

random.shuffle(pass_)
for i in pass_:
    print(i, end="")
