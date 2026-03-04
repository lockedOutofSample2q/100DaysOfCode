import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the PyPassword Generator!")
print("How long password do you need?: ")
input_length = int(input())
print(f"Great, it would be {input_length} characters long.")
print("Would you like to inlcude numbers in your password? (y/n): ")
input_numbers = input()
print("Would you like to inlcude symbols in your password? (y/n): ")
input_symbols = input()
password = ""

if input_numbers == "y":
    if input_symbols == "y":
        new_array = alphabets + numbers + symbols
        for i in range(input_length):
            password += random.choice(new_array)
    else :
        new_array = alphabets + numbers 
        for i in range(input_length):
            password += random.choice(new_array)
elif input_symbols == "y":
    new_array = alphabets + symbols
    for j in range(input_length):
        password += random.choice(new_array)
else : 
    for i in range(input_length):
        password += random.choice(alphabets)
print(f"Your password is: {password}")
