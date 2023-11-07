# Guess the USA States Quiz Game Documentation

## Introduction
The provided Python script represents a "Guess the USA States" quiz game using the Turtle graphics library. In this educational game, players are prompted to guess the names of U.S. states by typing their names. If a guess is correct, the state name is displayed on the map, and the player collects points. If all 50 states are guessed or the player chooses to exit, the game ends. This documentation explains the features, Python concepts used, and the structure of the code.

## Features

### Graphics and User Interface
- The game utilizes the Turtle graphics library to create a graphical interface for players to interact with.
- A background map of the U.S. states is displayed on the screen.

### Data Management
- A CSV file (`50_states.csv`) containing information about U.S. states, including their names and coordinates on the map, is used as a data source.

### User Interaction
- The game prompts the player to guess the names of U.S. states by typing them.
- The player's input is received through a dialog box using `screen.textinput()`.
- The player can exit the game at any time by typing "Exit."

### Score Tracking
- The game keeps track of the guessed states and displays the number of correct guesses in the game window's title.

### Displaying State Names
- When a state is correctly guessed, its name is displayed on the map at the corresponding geographical location.
- A Turtle object is used to render the state name.

### Game Completion
- The game continues until either all 50 states are guessed correctly or the player decides to exit.

### Missed States
- After the game ends, the script identifies and displays the names of the states that were not correctly guessed.

### Exporting Data
- The names of the missed states are saved to a CSV file (`states_to_learn.csv`) for further learning.

## Python Concepts Used

- **Turtle Graphics:** The game uses the Turtle graphics library to create a graphical user interface and display state names on the map.
- **Data Processing:** The `pandas` library is used to read and process data from a CSV file (`50_states.csv`) containing information about U.S. states.
- **Looping (`while` and `for`):** The game logic is implemented within a `while` loop to allow repeated player interactions. A `for` loop is used to display missed states.
- **User Input Handling:** The script receives and processes user input for guessing state names.
- **Conditional Statements (`if`):** Conditional statements are used to determine if a guessed state is correct or to exit the game.
- **Data Export:** The `pandas` library is used to create a new CSV file (`states_to_learn.csv`) containing the names of missed states.

## Code Structure

The code is divided into several sections:

1. **Constants:** Constants for the font, font size, and alignment of state names are defined.
2. **Setting up the Screen:** The game screen is initialized with the U.S. states map as the background.
3. **Data Loading:** Data about U.S. states is loaded from the CSV file into a list.
4. **Game Loop:** The primary game loop allows the player to guess state names and handles game progression.
5. **Missed States:** After the game ends, a `for` loop displays the names of missed states on the map.
6. **Data Export:** The names of missed states are saved to a CSV file.
7. **Game Exit:** The game window is closed when the player clicks anywhere on the screen.

## Conclusion

The "Guess the USA States" quiz game is an interactive and educational application that allows players to test their knowledge of U.S. states. The script utilizes Python's Turtle graphics library for creating an engaging user interface and `pandas` for data management. Players can guess state names, and the game provides feedback on their correctness. Missed states are displayed for further learning, and the names of these states are saved to a CSV file. This project demonstrates the use of Python for creating interactive educational games with graphical interfaces.
