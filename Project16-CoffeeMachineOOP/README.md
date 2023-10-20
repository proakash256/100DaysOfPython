# Coffee Machine

**Introduction:**

The coffee machine software is a Python program that simulates the functionality of a coffee machine.  
It allows users to select drinks from a menu, make payments, and prepares the chosen drink if the required resources are available.  
The software is built using the concepts of object-oriented programming in Python.

**Logic:**

The coffee machine software consists of three main classes: `Menu`, `CoffeeMaker`, and `MoneyMachine`.  
The `Menu` class represents the menu of available drinks, the `CoffeeMaker` class models the coffee-making functionality, and the `MoneyMachine` class handles the money-related operations.

The program starts by initializing instances of the `CoffeeMaker`, `MoneyMachine`, and `Menu` classes. It then enters a loop that continues until the user turns off the coffee machine.  
Within the loop, the user is prompted to select an option from the menu or perform other actions like turning off the machine or generating a report.

Based on the user's choice, the program executes the corresponding logic.  
If the user selects a drink, the program checks if there are sufficient resources to make the chosen drink. If resources are sufficient,  
it prompts the user to insert coins and verifies if the payment is sufficient. If the payment is accepted, it deducts the required ingredients from the resources and prepares the drink.  
If the user selects the "report" option, the program generates a report showing the current status of resources and profits.

**Functions and Python Concepts:**

1. `MenuItem` class: Represents a menu item (drink) with its name, cost, and required ingredients. It uses the concept of a dictionary to store the ingredients.

2. `Menu` class: Models the menu of available drinks. It has functions:
   - `get_items()`: Returns a string containing the names of all available menu items.
   - `find_drink(order_name)`: Searches the menu for a drink with a specific name and returns that item if it exists.

3. `MoneyMachine` class: Handles money-related operations. It has functions:
   - `report()`: Prints the current profit.
   - `process_coins()`: Prompts the user to insert coins and calculates the total amount received.
   - `make_payment(cost)`: Verifies if the received payment is sufficient for the given cost and returns True or False accordingly.

4. `CoffeeMaker` class: Models the coffee-making functionality. It has functions:
   - `report()`: Prints a report of the current resources (water, milk, and coffee).
   - `is_resource_sufficient(drink)`: Checks if there are sufficient resources to make a specific drink.
   - `make_coffee(order)`: Deducts the required ingredients for a drink from the available resources.

Other Python concepts used in the code include loops, conditional statements, dictionaries, and object-oriented programming principles like class and object instantiation, attributes, and methods.

The code demonstrates the use of modularization by importing the `Menu`, `MenuItem`, `CoffeeMaker`, and `MoneyMachine` classes from separate modules (`menu.py`, `coffee_maker.py`, `money_machine.py`).  
This helps in organizing the code and separating concerns.

Overall, the coffee machine software provides a user-friendly interface to select and prepare various drinks while keeping track of resources and profits.  
It utilizes the principles of object-oriented programming in Python to achieve modularity and maintainability.