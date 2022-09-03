MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

account_balance = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 50,
}


def checkResources(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def collectCoins():
    print("Please insert coins: ")
    try:
        total = int(input("no of quarters: "))*0.25
        total += int(input("no of dimes: "))*0.10
        total += int(input("no of nickles: "))*0.05
        total += int(input("no of pennies: "))*0.01
        return total
    except:
        return 0


def initiateTransaction(money, ordered_coffee):
    global account_balance
    coffee = MENU[ordered_coffee]

    if coffee["cost"] > money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif coffee["cost"] < money:
        change = round(money - coffee["cost"], 2)
        print(f"Here is ${change} change.")
        account_balance += money-change
        return True
    elif coffee["cost"] == money:
        account_balance += money
        return True


def makeCoffee(ordered_coffee):
    coffee = MENU[ordered_coffee]
    for ingredient in coffee["ingredients"]:
        resources[ingredient] -= coffee["ingredients"][ingredient]

    print(f"Here is your {ordered_coffee} ☕ enjoy.")


def processCoffee(ordered_coffee):
    if checkResources(MENU[ordered_coffee]["ingredients"]):
        money = collectCoins()
        if initiateTransaction(money, ordered_coffee):
            makeCoffee(ordered_coffee)


isMachineOn = True

while isMachineOn:

    print("Please choose your coffee:")
    print("Press 1 for Espresso :")
    print("Press 2 for Latte :")
    print("Press 3 for Cappuccino :")

    choice = input().lower()

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {round(account_balance,2)}")

    elif choice == "off":
        isMachineOn = False

    elif (choice == "1"):
        ordered_coffee = "espresso"
        processCoffee(ordered_coffee)

    elif (choice == "2"):
        ordered_coffee = "latte"
        processCoffee(ordered_coffee)

    elif (choice == "3"):
        ordered_coffee = "cappuccino"
        processCoffee(ordered_coffee)

    else:
        print("Please press valid button")
