# Flash Card App Documentation

## Introduction

The Flash Card App is a Python program that helps users learn new words or concepts through flashcards. The app presents a word or concept in one language and asks the user to recall its translation or meaning in another language. It provides a simple and interactive interface for users to practice and test their knowledge.

## Dependencies

The program requires the following dependencies:

- `random`: A module for generating random numbers and selecting random elements from a sequence.
- `tkinter`: A Python interface to the Tk GUI toolkit for creating graphical user interfaces.
- `pandas`: A library for data manipulation and analysis.

## Constants

The program uses the following constants:

- `BACKGROUND_COLOR`: A string representing the background color of the application.

## User Interface Setup

The program creates a graphical user interface (GUI) using the Tkinter library. The GUI consists of a main window with a canvas, two buttons, and two text elements representing the flashcard.

The canvas is used to display the front and back of the flashcard. It initially shows the front side with a title and the word or concept in one language. The canvas is configured with the appropriate dimensions and background color.

The buttons are used to navigate to the next flashcard and mark a flashcard as known. They are represented by images and placed in a grid layout within the main window.

The text elements represent the title and word or concept on the flashcard. They are created using the `create_text()` method of the canvas and positioned accordingly.

## Flashcard Data

The program reads flashcard data from a CSV file. It first tries to read from a file named "words_to_learn.csv". If the file is not found, it falls back to reading from a file named "french_words.csv". The flashcard data is stored in a Pandas DataFrame and converted to a dictionary using the `to_dict()` method.

## Flashcard Navigation

The program provides a function `next_card()` to navigate to the next flashcard. When called, it updates the canvas to show the front side of the flashcard with the word or concept in one language. It selects a random flashcard from the available flashcards and updates the canvas with the corresponding word or concept in the other language.

After a delay of 3 seconds (3000 milliseconds), the function calls `flip_card()` to flip the flashcard and display the back side with the translation or meaning.

## Flashcard Flipping

The program provides a function `flip_card()` to flip the flashcard and show the back side. When called, it updates the canvas to show the back side of the flashcard with the translation or meaning. It also updates the title text to "English" and sets the text color to white.

## Flashcard Marking

The program provides a function `is_known()` to mark a flashcard as known. When called, it removes the current flashcard from the list of flashcards to learn. It then updates the flashcard data in the CSV file by creating a new DataFrame and saving it to "words_to_learn.csv". Finally, it calls `next_card()` to navigate to the next flashcard.

## Conclusion

The Flash Card App program provides an interactive and engaging way for users to learn new words or concepts through flashcards. By displaying a word or concept in one language and asking for its translation or meaning in another language, users can practice and test their knowledge. The program's graphical user interface allows for easy navigation between flashcards and provides visual feedback on the user's progress.

This documentation serves as a reference for understanding the functionality and structure of the Flash Card App program.