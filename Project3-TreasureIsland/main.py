print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
print('''Welcome to Treasure Island.
Your mission is to find the treasure\n\n''')
ch1 = input('You\'re at a crossroad.Where would you like to go? Type "left" or "right".\n').lower()
if ch1 == "left":
    ch2 = input('You\'ve come to a Lake. There is an Island in the middle of the Lake. Type "wait" to wait for a boat '
                'or type "swim to swim across.\n"').lower()
    if ch2 == "wait":
        ch3 = input('You\'ve arrived at the island Unharmed. There is a Castle with 3 Doors of colours "Red", '
                    '"Yellow", and "Blue".Open the correct Door to win the game.\n').lower()
        if ch3 == "red":
            print("Oh No!! You fell into a Lava Lake. Game Over!!\n")
        elif ch3 == "yellow":
            print("Congratulations!! You Have Won the Game!!\n")
        else:
            print("Sorry!! You fell into a Valley. Game Over!!\n")
    else:
        print("The Lake was too turbulent to swim. Game Over!!\n")

else:
    print("You fell into a Hole. Game Over!!\n")
