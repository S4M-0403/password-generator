import random

letters = ['Q','W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'] # list containing both upper case and lower case letters

numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # list containing all numbers

symbols = ['!', '@', '#', '$' , '%', '^', '&', '*', '(',')','{','}','[', ']','/','|'] #list containing symbols

print("Welcome to Password generator using python!")

numberOfLetters = int(input("Enter the number of letters you want in your password: "))
numberOfNumbers = int(input("Enter the number of numbers you want in your password: "))
numberOfSymbols = int(input("Enter the number of symbols you want in your password: "))

totalLength = numberOfLetters + numberOfNumbers + numberOfSymbols
print(f"Total length of your password is {totalLength}")
password_list = []

for i in range(1, numberOfLetters+1):
    password_list.append(random.choice(letters))
for i in range(1, numberOfNumbers+1):
    password_list+=random.choice(numbers)
for i in range(1, numberOfSymbols+1):
    password_list+=random.choice(symbols)
random.shuffle(password_list)
password = " "
for i in password_list:
    password+=i
print(password)