import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a Random Card from the Deck."""
    return random.choice(cards)


def calculate_score(cards):
    """Returns the Sum of the Deck."""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Draw !!")
    elif computer_score == 0:
        print("You Lose !! Opponent has Blackjack")
    elif user_score == 0:
        print("You Win !! with a Blackjack")
    elif user_score > 21:
        print("You went over !! You lose")
    elif computer_score > 21:
        print("You Win !! Opponent went over")
    elif user_score > computer_score:
        print("You Win !!")
    else:
        print("You Lose !!")


def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards : {user_cards}\tCurrent Score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, Type 'n' to pass : ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your Final Cards : {user_cards}\tFinal Score : {user_score}")
    print(f"Computer's Final Cards : {computer_cards}\tFinal Score : {computer_score}")
    compare(user_score, computer_score)


while input("To play a game of Blackjack type 'y' else type 'n' : ") == 'y':
    play_game()
