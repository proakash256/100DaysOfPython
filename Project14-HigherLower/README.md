# Higher or Lower

## Introduction
This Python script is a "Higher or Lower" game where the player compares the number of followers of two randomly selected celebrities  
and tries to guess which celebrity has more followers. The player's score increases with each correct guess.  
The game imports an ASCII art logo and a list of dictionaries containing celebrity data. The player interacts with the game through the command line.  
The ASCII art used is taken from [here](https://ascii.co.uk/text).

## Features

### Logic
The game's logic can be summarized in the following steps:

1. **Import Required Modules and Data:**
   - `art`: Used to display an ASCII art logo.
   - `data`: Contains a list of dictionaries, each representing a celebrity with attributes such as name, follower count, description, and country.
   - `random`: Used to randomly select two celebrities from the data.

2. **Initialize Score:**
   - The player's score is initialized to 0.

3. **Generate Random Celebrities:**
   - Two celebrities (A and B) are randomly selected from the data list using the `generateRandom` function.

4. **Display Celebrity Data:**
   - The names and descriptions of the two celebrities are displayed, allowing the player to compare them.

5. **Compare Followers:**
   - The script checks which of the two celebrities (A or B) has more followers and assigns 'a' or 'b' to the variable `correct` accordingly.

6. **Player's Guess:**
   - The player is prompted to guess which celebrity has more followers by typing 'A' or 'B'.

7. **Main Game Loop:**
   - The game runs a loop as long as the player's guess is correct (`correct == guess`).
   - In each correct guess:
     - The player's score is increased.
     - A message is displayed with the current score.
     - New celebrities are selected for comparison.
     - The comparison variable `correct` is reset.
     - The player is prompted to make a new guess.

8. **Game Outcome:**
   - If the player's guess is incorrect, the game informs the player of their final score.

### Python Concepts Used
- **Importing Modules:** The code uses the `import` statement to bring in the `art` module and the `data` list.

- **Functions:** The script defines two functions, `generateRandom` to select random celebrities from the data and `format_data` to format celebrity data as a string.

- **Conditional Statements (`if`, `while`):** The game uses conditional statements to determine the correct guess, control the main game loop, and check if the player's guess is correct.

- **Lists and Dictionaries:** The game uses a list of dictionaries to store celebrity data. Dictionaries are used to represent individual celebrities with their attributes.

- **Loops (`while`):** The main game logic is implemented using a `while` loop that continues as long as the player guesses correctly.

- **User Input and Type Conversion:** The game takes user input using the `input` function and converts it to lowercase using the `lower()` method to ensure consistent input handling.

- **String Formatting (`print`):** The `print` function is used to display the game's messages, celebrity data, and the player's score.

## Conclusion
This "Higher or Lower" game is an engaging text-based game that challenges the player to compare the number of followers of two celebrities and make correct guesses.  
It incorporates various Python concepts, including modules, functions, conditional statements, loops, lists, dictionaries, and user input handling.  
Players can enjoy testing their knowledge of celebrity follower counts while striving to achieve a higher score.
