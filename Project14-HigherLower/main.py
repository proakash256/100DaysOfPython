import art
from data import data
import random

score = 0


def generateRandom():
    return random.choice(data)


def format_data(account):
    return f"{account['name']}, {account['description']}, from {account['country']}"


print(art.logo)
A = generateRandom()
B = generateRandom()
print(f"Compare A: {format_data(A)}")
print(art.vs)
print(f"Against B: {format_data(B)}")
correct = 'a'
if B["follower_count"] > A["follower_count"]:
    correct = 'b'
guess = input("Who has more followers? Type A or B : ").lower()
while correct == guess:
    score += 1
    print(f"You got it right !! Current Score : {score}")
    print("------------------------------------------------------------")
    if correct == "b":
        A = B
    B = generateRandom()
    print(f"Compare A: {format_data(A)}")
    print(art.vs)
    print(f"Against B: {format_data(B)}")
    correct = 'a'
    if B["follower_count"] > A["follower_count"]:
        correct = 'b'
    guess = input("Who has more followers? Type A or B : ").lower()
print("------------------------------------------------------------")
print(f"Sorry !! Wrong Answer. Final Score : {score}")
