# Coffee Machine

## Introduction
This Python script represents a software application for a coffee machine.  
The program allows users to select different coffee drinks, insert coins for payment, and dispense coffee.  
The software keeps track of available resources, profits, and provides options for generating reports.  
The program imports a logo from ASCII art and a menu containing coffee options and resources.  
The user interacts with the coffee machine through a command-line interface.  
The ASCII art used is taken from [here](https://ascii.co.uk/text).

## Features

### Functions
1. **`report()`**:
   - Function to print a report of available resources in the coffee machine, including water, milk, coffee, and profit.

2. **`is_resources_sufficient(ingredients)`**:
   - Function to check if there are sufficient resources to make a selected coffee drink.
   - Returns `True` if the resources are sufficient, and `False` if any resource is insufficient.

3. **`moneyInserted()`**:
   - Function to handle coin insertion and return the total value of coins inserted.
   - Prompts the user to input the number of coins in denominations of ₹1, ₹2, ₹5, and ₹10.
   
4. **`is_transaction_successful(money_received, drink_cost)`**:
   - Function to determine if a transaction is successful based on the money received and the cost of the selected drink.
   - Returns `True` if the transaction is successful (payment exceeds or equals the drink cost), and `False` otherwise.
   - Updates the profit.

5. **`make_coffee(drink_name, drink_ingredients)`**:
   - Function to prepare and dispense the selected coffee drink.
   - Deducts the required ingredients from the resources.
   - Notifies the user that their coffee is ready.

### Main Loop
- The script operates in a loop, allowing users to repeatedly select drinks or perform other actions.

### User Interaction
- Users can input commands to select coffee drinks (e.g., "espresso," "latte," "cappuccino"), request a report of available resources ("report"), or turn off the machine ("off").

### Data and Resources
- The script uses a `menu` dictionary containing coffee options (`coffee`) and available resources (`resources`).
- Each coffee option includes information about its ingredients and cost.

### Profits Tracking
- The `profit` variable keeps track of the total profit earned from coffee sales.

### ASCII Art
- The script displays a logo at the beginning of the program using ASCII art.

### Error Handling
- The software checks for resource availability and ensures that transactions are successful. It handles insufficient resources and returns change when the user inserts excess payment.

## Python Concepts Used
- **Functions:** The script defines multiple functions to encapsulate specific actions or operations.
- **Loops (`while`):** The program operates within a loop, allowing for repeated interactions with the coffee machine.
- **User Input and Type Conversion:** The software takes user input through the `input` function and converts it to lowercase for case-insensitive processing.
- **Dictionaries:** Data is stored and organized in dictionaries, such as `menu` for coffee options and `resources` for available resources.
- **Conditional Statements (`if`, `elif`, `else`):** Conditional statements are used to check user input and to determine whether resources are sufficient for making a coffee drink.
- **Global Variables:** The `profit` variable is declared as a global variable to track and update the total profit.
- **String Formatting (`print`):** The `print` function is used to display messages, reports, and notifications to the user.

## Conclusion
This coffee machine software is an interactive text-based application that allows users to select coffee drinks,  
insert coins, and receive their chosen beverage. It demonstrates the use of Python concepts, including functions, loops, user input handling,  
dictionaries, conditional statements, and global variables. The software provides a simulated experience of managing a coffee machine, including tracking resources and profits.
