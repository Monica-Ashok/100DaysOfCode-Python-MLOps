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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

report = {
    "water": 0,
    "milk": 0,
    "coffee": 0,
    "money": 0
}


def update_report(drink_name):
    ingredients = MENU.get(drink_name, {}).get('ingredients')

    for item in ingredients:
        resources[item] -= ingredients[item]

    report['water'] = resources['water']
    report['milk'] = resources['milk']  # some drinks have no milk
    report['coffee'] = resources['coffee']
    report['money'] += MENU.get(drink_name, {}).get('cost')


def get_cost(drink_name):
    return MENU.get(drink_name, {}).get('cost')


def insert_coins():
    coins = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}
    total = 0

    for coin, value in coins.items():
        while True:
            try:
                count = int(input(f'How many {coin}?: '))
                total += count * value
                break
            except ValueError:
                print("Invalid input! Enter a number.")
    return total


def print_report():
    """Display the current resource report."""
    print(f"Water: {report['water']}ml\n"
          f"Milk: {report['milk']}ml\n"
          f"Coffee: {report['coffee']}g\n"
          f"Money: ${report['money']:.2f}")


def check_resources(drink_name):
    """Check if there are enough resources to make the drink."""
    ingredients = MENU.get(drink_name, {}).get('ingredients')

    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False  # Not enough resources
        return True  # Enough resources


# MAIN LOOP
while True:
    user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_selection == 'off':
        print("Turning off the coffee machine. Bye!")
        break

    if user_selection == 'report':
        print_report()
        break

    if user_selection not in MENU:
        print('Please enter a valid drink!')
        continue

    # Check if there are enough resources
    if not check_resources(user_selection):
        continue  # Go back to the beginning of the loop

    cost = get_cost(user_selection)
    print("Please insert coins.")

    total = insert_coins()

    if total < cost:
        print("Sorry that's not enough money. Money Refunded")
        continue

    change = abs(total - cost)
    if change > 0:
        print(f'Here is your ${change:.2f} in change. Enjoy your {user_selection}')

    print(f"Enjoy your {user_selection} ☕!")

    update_report(user_selection)