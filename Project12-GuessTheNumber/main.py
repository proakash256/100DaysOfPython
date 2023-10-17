import random
from art import logo

print(logo)

print("Welcome to Guess the Number Game !!")
print("You have to find a Number between 1 and 100")
difficulty = input("Choose a Difficulty. Type 'easy' or 'hard' : ")
chances = 10
if difficulty == 'hard':
    chances = 5
num = random.randint(1, 100)
while chances > 0:
    print(f"You have {chances} chances to Guess the Number.")
    guess = int(input("Make a Guess : "))
    if guess == num:
        print("Congratulations!! You guessed the number right.")
        break
    elif guess > num:
        print("Too High!! Try again.")
    else:
        print("Too Low!! Try Again.")
    chances -= 1
if chances == 0:
    print("Sorry!! you finished all your chances.")
