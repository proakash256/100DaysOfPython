import random
import string

print("\n\n******************************** Welcome to the Password Generator ********************************\n\n")

letters = list(string.ascii_letters)
numbers = [str(i) for i in range(0, 10)]
symbols = ['!', "@", "#", '$', '%', '&', '*', '(', ')', '_', '-', '+', '{', '}', '[', ']']

alphabets = int(input("How many Alphabets you want to add in the Password : "))
num = int(input("\nHow many Digits you want to add in the Password : "))
syl = int(input("\nHow many Symbols you want to add in the Password : "))

password = ''
l1 = []
for i in range(0, alphabets):
    l1.append(random.choice(letters))

for i in range(0, num):
    l1.append(random.choice(numbers))

for i in range(0, syl):
    l1.append(random.choice(symbols))

random.shuffle(l1)

for i in l1:
    password += i

print("\n\nYour Secure Password is : ", password)
