from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#Show a menu.
is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#Take orders.
while is_on:
    drinks = menu.get_items()
    user_selection = input(f"What would you like? ({drinks}): ").lower()

#Check if there are enough ingredients.
#Process payment.
#Make the coffee.

    if user_selection == 'off':
        is_on = False
    elif user_selection == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drinks = menu.find_drink(user_selection)
        if drinks:
            if coffee_maker.is_resource_sufficient(drinks):
                if money_machine.make_payment(drinks.cost):
                    coffee_maker.make_coffee(drinks)