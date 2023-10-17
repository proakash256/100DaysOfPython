# Hangman

## Introduction
This Python script is a "Hangman" game that challenges the player to guess a hidden word by guessing individual letters.  
The player has a limited number of lives, and with each incorrect guess, a part of a hangman figure is drawn.  
The goal is to guess the word before running out of lives. The game imports a text-based ASCII art logo, a word list,  
and a random module to make the game visually appealing and to choose a word for the player to guess.  
The player interacts with the game through the command line.  
The ASCII art used is taken from [here](https://ascii.co.uk/art/hangman).

## Features

### Logic
The game's logic can be summarized in the following steps:

1. **Import Required Modules:**
   - `art`: Used to display a text-based hangman logo.
   - `wordList`: Contains a list of words from which one is randomly selected for the game.
   - `random`: Used to choose a random word from the list.

2. **Display Game Logo:**
   - The Hangman game's logo is displayed at the beginning of the game to provide a visually appealing start to the player.

3. **Choose a Word:**
   - A word is randomly selected from the word list for the player to guess.

4. **Initialize Game Variables:**
   - The player is given a certain number of lives (7 in this case).
   - A list `l1` is created, which represents the current state of the word to guess. It contains underscores (`_`) initially, indicating unguessed letters.

5. **Display Initial Word State:**
   - The initial state of the word is displayed with underscores, providing the player with an idea of the word's length.

6. **Main Game Loop:**
   - The game runs a loop until the player either wins or runs out of lives (`lives == 0`).

7. **Guessing a Letter:**
   - The player is prompted to guess a letter. The input is converted to lowercase for consistency.

8. **Incorrect Guess Handling:**
   - If the guessed letter is not in the chosen word, the player loses a life and a part of the hangman figure is displayed. The number of lives left is shown.

9. **Win or Lose Condition:**
   - If the player runs out of lives (`lives == 0`), the game ends, and the player loses.
   - If the player successfully guesses all the letters in the word (`l1` has no underscores left), the game ends, and the player wins.

10. **Correct Guess Handling:**
    - If the guessed letter is in the word, the script updates the `l1` list to reveal the correct position(s) of the guessed letter(s).

11. **Display Updated Word State:**
    - The current state of the word, with correctly guessed letters filled in, is displayed.

### Python Concepts Used
- **Importing Modules:** The code uses the `import` statement to bring in the `art`, `wordList`, and `random` modules.

- **Conditional Statements (`if`, `while`):** The game uses conditional statements to control the flow of the game, such as checking for correct or incorrect guesses and determining when the game ends.

- **Lists:** Lists are used to store the state of the word (`l1`) and the word to guess (`chosen_word`). The script iterates through lists to update and display the game state.

- **Loops (`for`, `while`):** The main game logic is implemented using a `while` loop that continues until the game ends. A `for` loop is used to iterate over the chosen word to check for correctly guessed letters.

- **User Input and Type Conversion:** The game takes user input using the `input` function and converts it to lowercase using the `lower()` method to ensure consistent letter case.

- **Randomization (`random.choice()`):** The script uses the `random.choice()` function to randomly select a word from the word list.

- **String Formatting (`print`):** The `print` function is used to display the game's messages, hangman art, and the current state of the word with correct letters filled in.

## Conclusion
This Hangman game is an interactive and challenging text-based game that tests the player's word-guessing skills.  
It incorporates various Python concepts, including modules, conditional statements, loops, and lists,  
to provide an engaging gaming experience through the command line interface. Players can enjoy the thrill of trying to guess the word while avoiding losing all their lives.
