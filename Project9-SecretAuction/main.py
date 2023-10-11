import art
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print(art.logo)
bidders = {}
while True:
    name = input("Enter the Name : ")
    bid = int(input("Enter the Bid : $"))
    bidders[name] = bid
    cls()
    ch = input("Are there any more bidders ?? Type 'Yes' or 'No' : ")
    ch.lower()
    if ch == "no":
        break
m = 0
won = ""
for i in bidders:
    if bidders[i] > m:
        m = bidders[i]
        won = i
print(f"{won} won the Auction with a bid of {m}")
