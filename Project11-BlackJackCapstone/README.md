# Blackjack

### Introduction:

This Python project is a text-based implementation of the classic card game, Blackjack.  
It follows a set of simplified house rules and allows the player to enjoy a game of Blackjack against a computer-controlled dealer.  
The game is built using Python and demonstrates the use of fundamental programming concepts like functions, loops, conditionals, and random number generation.  
The ASCII art used is taken from [here](https://ascii.co.uk/text).

### Blackjack House Rules:

- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards:
  - `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`

## Features

Here's an overview of the Python language features used in this code:

1. **Import Statements**:
   - The `random` module is imported to generate random cards.
   - The `art` module is imported, which contains the game's logo.

2. **Card Deck**:
   - A list named `cards` is defined to represent a deck of cards for the game.
   - The deck contains 13 values: 11 (Ace), 2-10, and 4 cards with a value of 10 (representing Jack, Queen, King).

3. **`deal_card()` Function**:
   - This function selects a random card from the `cards` list and returns it as an integer.

4. **`calculate_score()` Function**:
   - Calculates the score of a hand based on the values of the cards.
   - Handles scenarios like Blackjack and the Ace's value (11 or 1).

5. **`compare()` Function**:
   - Compares user and computer scores to determine the game's outcome.

6. **`play_game()` Function**:
   - Manages the gameplay, dealing cards to the user and computer, and allowing the user to draw additional cards or pass.
   - Calculates and displays scores and manages the computer's moves.

7. **Main Game Loop**:
   - Allows the user to restart the game or quit.

This code demonstrates the use of functions, conditional statements, loops, and simulates a simplified version of the Blackjack game.  
It follows basic Blackjack rules and uses the `art` module to display the game's logo, enhancing the user experience.
