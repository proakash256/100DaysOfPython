# Quiz Game Documentation

**Introduction:**

The Quiz Game is a Python program that allows users to play a quiz by answering a series of True/False questions. The program utilizes the concepts of object-oriented programming to create questions, manage the quiz process, and keep track of the user's score.

**Logic:**

The quiz game program consists of three main classes: `Question`, `QuizBrain`, and the main program logic. The `Question` class represents a single question with its text and correct answer. The `QuizBrain` class manages the quiz process, including tracking the question number, the question list, and the user's score.

The program starts by importing the required modules: `Question` from `question_model`, `question_data` from `data`, and `QuizBrain` from `quiz_brain`.

The program then creates an empty list called `question_bank` to store the `Question` objects. It iterates over the `question_data` list and creates a `Question` object for each question, using the question text and correct answer from the data. The `Question` objects are appended to the `question_bank`.

Next, an instance of `QuizBrain` is created, passing the `question_bank` as an argument. The `QuizBrain` instance manages the quiz process.

The program enters a loop that continues until there are no more questions in the `question_bank`. Within the loop, the `next_question()` method of the `QuizBrain` class is called to present the next question to the user. The user's answer is obtained through user input, and the `check_answer()` method is called to compare the user's answer with the correct answer and update the score accordingly.

Once all the questions have been answered, the loop exits, and the program prints a completion message along with the user's final score.

**Functions and Python Concepts:**

1. `QuizBrain` class: Manages the quiz process. It has functions:
   - `__init__(self, question_list)`: Initializes the `QuizBrain` instance with the provided question list.
   - `still_has_questions(self)`: Checks if there are still questions remaining in the question list.
   - `next_question(self)`: Presents the next question to the user and obtains their answer.
   - `check_answer(self, user_answer, correct_answer)`: Compares the user's answer with the correct answer and updates the score.

2. `Question` class: Represents a single question with its text and correct answer. It has functions:
   - `__init__(self, text, answer)`: Initializes the `Question` instance with the provided question text and correct answer.

Other Python concepts used in the code include loops, conditional statements, user input, string formatting, and object-oriented programming principles like class and object instantiation, attributes, and methods.

The code demonstrates the use of modularization by importing the `Question`, `QuizBrain`, and `question_data` from separate modules (`question_model.py`, `quiz_brain.py`, `data.py`). This helps in organizing the code and separating concerns.

Overall, the Quiz Game program provides an interactive quiz experience by utilizing the principles of object-oriented programming in Python. It allows users to test their knowledge by answering a series of True/False questions and provides immediate feedback on their answers and final score.