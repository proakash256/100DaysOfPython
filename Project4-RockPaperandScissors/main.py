import random
print("\t_______________Welcome To The Game : Rock, Paper & Scissors_______________\n")

print("\n\tRules Of The Game:-\n\n")
print("\t1.Rock Crushes The Scissors Player Who Choose Rock, One Point Will Be Given To Him\n\n")
print("\t2.Paper Cover's The Rock Player Who Choose Paper Against The Rock, One Point Will Be Given To Him\n\n")
print("\t3.Scissors Cuts The Paper Player Who Choose Scissors, One Point Will Be Given To Him\n\n")
print("\tOnly Two Player's Can Play The Game One Will Be The Computer And Second Will Be The User!\n\n")
print("\t4.You Will Be Given Three Chances!\n\n")
print("\tScores Will Be Displayed At The End Of The Match\n\n")

name = input("\tPlease Enter The Name Of Player 1 : ")
print(f"\tPlayer 1 Is {name} And Player 2 Is Computer\n")
print("\n\n\tYou Have Three Attempts To Win The Game\n")

C_score = 0
P_score = 0

for i in range(0, 3):
    print("\n\n\t----------------------------")
    print(f"\n\t{name}'s Turn:-\n")
    print("\n\tPress->0 For Rock\n")
    print("\tPress->1 For Paper\n")
    print("\tPress->2 For Scissor\n\n")
    choice = int(input("\tEnter Your Choice : "))
    var = random.randint(0, 2)
    print(f"\tComputer's Choice : {var}")
    if choice > 2 or choice < 0:
        print("\n\t----------------------------")
        print("\n\t\tInvalid Choice!\n")
        print("\t----------------------------\n")
    elif choice == 0 and var == 2:
        print("\n\t----------------------------")
        print(f"\n\t\t{name} Wins!\n")
        print("\t----------------------------\n")
        P_score += 1
    elif var == 0 and choice == 2:
        print("\n\t----------------------------")
        print("\n\t\tComputer Wins!\n")
        print("\t----------------------------\n")
        C_score += 1
    elif choice > var:
        print("\n\t----------------------------")
        print(f"\n\t\t{name} Wins!\n")
        print("\t----------------------------\n")
        P_score += 1
    elif var > choice:
        print("\n\t----------------------------")
        print("\n\t\tComputer Wins!\n")
        print("\t----------------------------\n")
        C_score += 1
    elif choice == var:
        print("\n\t----------------------------")
        print("\n\t\tIt's A Tie!\n")
        print("\t----------------------------\n")
        P_score += 1
        C_score += 1

    print(f"\n\tScore Of {name} Is : {P_score}\n")
    print(f"\n\tScore Of Computer Is : {C_score}\n")
    print("\t---------------------------\n\n")
if P_score > C_score:
    print("\n\n\t----------------------------")
    print(f"\n\n\t\t{name} Wins The Match!\n\n")
    print("\t---------------------------\n\n")
elif C_score > P_score:
    print("\n\n\t----------------------------------")
    print("\n\n\t\tComputer Wins The Game!\n\n")
    print("\t---------------------------\n\n")
else:
    print("\n\n\t----------------------------")
    print("\n\n\t\tIt's A Tie!\n\n")
    print("\t---------------------------\n\n")
