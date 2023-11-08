## NATO Alphabet

### Introduction

This program converts words into their corresponding NATO phonetic alphabet codes. The program reads the NATO phonetic alphabet data from a CSV file and stores it in a dictionary. The user is then prompted to enter a word, and the program returns the NATO phonetic alphabet code for each letter in the word.

### Logic of the Code

The code is divided into two main parts:

1. **Data Preparation:** The program reads the NATO phonetic alphabet data from a CSV file named `nato_phonetic_alphabet.csv`. The CSV file contains two columns: `letter` and `code`. The `letter` column contains the standard alphabet letters, and the `code` column contains the corresponding NATO phonetic alphabet codes. The program reads the CSV file into a pandas DataFrame and then creates a dictionary named `letter_dict` that maps each letter to its corresponding code.

2. **Word Conversion:** The program prompts the user to enter a word. The user's input is converted to uppercase using the `upper()` method. The code then iterates over each character in the word and uses the `letter_dict` dictionary to retrieve the corresponding NATO phonetic alphabet code for each character. The codes are then stored in a list named `res`. Finally, the list `res` is printed to the console.

### Functions and Python Concepts Used

The code uses the following functions and Python concepts:

* `pandas.read_csv()` : This function reads a CSV file into a pandas DataFrame. 
* `iterrows()` : This method iterates over the rows of a pandas DataFrame. 
* `upper()` : This method converts a string to uppercase.
* `KeyError` : This exception is raised when a key is not found in a dictionary. 
* `try-except` : This block of code is used to handle exceptions. The `try` block contains the code that might raise an exception, and the `except` block contains the code that is executed when the exception is raised.

### Additional Details

* The program only accepts letters from the standard alphabet. If the user enters a character that is not a letter, the program will print an error message. 
* The program is case-sensitive. The user must enter the word in uppercase for the program to work correctly.

### Example Usage
```
Enter the Word: Hello
['HOTEL', 'ECHO', 'LIMA', 'LIMA', 'OSCAR']
```
