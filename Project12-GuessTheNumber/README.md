# Guess the Number

## Introduction
This Python script is a "Guess the Number" game in which the player has to guess a randomly generated number between 1 and 100.  
The game provides the player with a limited number of chances based on the chosen difficulty level, and the player must try to guess the correct number within these chances.  
The game offers an entertaining and interactive experience through the command line interface.  
The ASCII art used is taken from [here](https://ascii.co.uk/text).

## Features

### Logic
The game's logic can be summarized in the following steps:

1. **Import Required Modules:**
   - `random`: Used to generate a random number for the player to guess.
   - `art`: Used to display a text-based logo.

2. **Display Game Logo:**
   - The "Guess the Number Game" logo is displayed at the beginning of the game for visual appeal.

3. **Welcome Message and Difficulty Selection:**
   - The game welcomes the player and asks them to choose a difficulty level - 'easy' or 'hard'. The chosen difficulty level determines the number of chances the player gets.

4. **Set the Number of Chances Based on Difficulty:**
   - If the player selects 'hard', they have 5 chances to guess the number.
   - If the player selects 'easy', they have 10 chances to guess the number (the default).

5. **Generate a Random Number:**
   - A random integer between 1 and 100 is generated as the target number for the player to guess.

6. **Main Game Loop:**
   - The game runs a loop as long as the player has remaining chances (`chances > 0`).
   - In each iteration, the game:
     - Informs the player of the remaining chances.
     - Accepts the player's guess as input.
     - Compares the guess with the random number.
     - Provides feedback to the player, indicating whether the guess is too high or too low.
     - Reduces the remaining chances.

7. **Game Outcomes:**
   - If the player guesses the number correctly, they win, and the game congratulates them.
   - If the player uses up all their chances without guessing the number, the game informs them that they have lost.

### Python Concepts Used
- **Importing Modules:** The code uses the `import` statement to bring in the `random` module and the `art` module for generating random numbers and displaying the game logo, respectively.

- **Conditional Statements (`if`, `elif`, `else`):** The game uses conditional statements to determine the number of chances based on the chosen difficulty level and to provide feedback to the player based on their guesses.

- **Loops (`while`):** The game employs a `while` loop to allow the player to keep guessing until they run out of chances or guess the number correctly.

- **User Input and Type Conversion:** The game takes user input using the `input` function and converts it to an integer using the `int` function to compare the player's guess with the random number.

- **Random Number Generation:** The `random.randint()` function is used to generate a random number within the specified range.

- **String Formatting:** The game uses `f-strings` to dynamically display messages and values, making the output more informative and user-friendly.

- **Basic I/O:** The game uses `print` statements to display messages and information to the player through the command line.

## Conclusion
This Python "Guess the Number" game is a simple yet engaging text-based game that allows the player to test their guessing skills  
while also demonstrating the use of various Python concepts and modules. Players can enjoy the challenge of guessing the correct number  
within a limited number of chances, making it an entertaining and interactive coding project.
