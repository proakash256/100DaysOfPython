from art import logo
import menu

print(logo)
profit = 0
is_machine_on = True


def report():
    """Prints the Report of Resources available in the Machine"""
    print("----------------------REPORT----------------------------")
    print(f"Water : {menu.resources['water']}")
    print(f"Milk : {menu.resources['milk']}")
    print(f"Coffee : {menu.resources['coffee']}")
    print(f"Profit : {profit}")
    print("--------------------------------------------------------")


def is_resources_sufficient(ingredients):
    """Returns True if the Resources are sufficient else False"""
    for item in ingredients:
        if ingredients[item] >= menu.resources[item]:
            print(f"Sorry!! There is not enough {item}")
            return False
    return True


def moneyInserted():
    """Returns the total value of coins inserted into the machine"""
    print("--------------------------------------------------------")
    print("Please Insert the Coins : ")
    total = int(input("How many ₹ 1 Coins ? : "))
    total += int(input("How many ₹ 2 Coins ? : ")) * 2
    total += int(input("How many ₹ 5 Coins ? : ")) * 5
    total += int(input("How many ₹ 10 Coins ? : ")) * 10
    print("--------------------------------------------------------")
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if the Transaction is Successful else False"""
    if money_received >= drink_cost:
        print(f"You have ₹ {round(payment - drink['cost'], 2)} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry!! That's not enough money. Money Returned.")
        return False


def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        menu.resources[item] -= drink_ingredients[item]
    print("--------------------------------------------------------")
    print(f"Here's your {drink_name} ☕. Enjoy!!")
    print("--------------------------------------------------------")


while is_machine_on:
    choice = input("What would you like ? (espresso/latte/cappuccino) : ").lower()
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        print(report())
    else:
        drink = menu.coffee[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = moneyInserted()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
