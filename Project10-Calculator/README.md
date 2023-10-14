# Calculator

This is a basic Python calculator program that allows you to perform basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers.

## Features

Here's an overview of the Python language features used in this code:

### 1. Functions

The code defines four functions, each for a different arithmetic operation:

- `add(a, b)`: Adds two numbers.
- `subtract(a, b)`: Subtracts one number from another.
- `multiply(a, b)`: Multiplies two numbers.
- `divide(a, b)`: Divides one number by another.

### 2. Function Documentation

Each function is documented using docstrings, which provide a brief description of the function's purpose. For example:

```python
def add(a, b):
    """ Adds Two Numbers """
    return a + b
```
### 3. Dictionary
The operations dictionary is used to associate arithmetic symbols with their corresponding functions. For example:
```python
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
```
### 4. User Input
The input() function is used to get user input. The code prompts the user to enter numbers and select an operation to perform.

### 5. Conditional Statements
Conditional statements (if, elif, and else) are used to control the flow of the program.  
These statements handle the user's choice to continue, start a new calculation, or quit.

### 6. Recursion
The calculator() function uses recursion to allow the user to start a new calculation when they choose to do so.  
This means that the function calls itself within the "start a new calculation" branch.

### 7. String Formatting
String formatting (f strings) is used to display the calculation results in a user-friendly way. For example:
```python
print(f"{a} {s} {b} = {answer}")
```
## How to Use
- Run the script, and the program will ask you to enter the first number.

- You will be prompted to select an operation by entering one of the following symbols: "+", "-", "*", "/".

- You will be prompted to Enter the second number.

- The program will display the result and give you the option to continue the calculation, start a new calculation, or quit.

### Example
Here's an example of how the program works:
```mathematica
Enter the First Number : 10
+  -  *  /
Pick one operation : +
Enter the Next Number : 5
10.0 + 5.0 = 15.0
Type y to continue the calculation
Type n to start a new calculation
Type q to quit
Enter your choice: y
Enter the Next Number : 3
15.0 + 3.0 = 18.0
Type y to continue the calculation
Type n to start a new calculation
Type q to quit
Enter your choice: n
Enter the First Number : 8
+  -  *  /
Pick one operation : *
Enter the Next Number : 2
8.0 * 2.0 = 16.0
Type y to continue the calculation
Type n to start a new calculation
Type q to quit
Enter your choice: q
```