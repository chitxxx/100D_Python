from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def run_coffee_machine():

    # intialize coffee machine
    is_on = True
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu_items = menu.get_items().split("/")

    while is_on:
        request = input("What would you like? (espresso/latte/cappuccino)")

        if request == "off":
            is_on = False

        elif request == "report":
            coffee_maker.report()
            money_machine.report()

        elif request in menu_items:
            order = menu.find_drink(request)
            sufficient_ingredient = coffee_maker.is_resource_sufficient(order)
            print(sufficient_ingredient)
            if sufficient_ingredient:
                cost = order.cost
                sufficient_money = money_machine.make_payment(cost)
                if sufficient_money:
                    coffee_maker.make_coffee(order)
        else:
            print(f"'{request}' is not a valid request, try again.")

if __name__ == "__main__":
    run_coffee_machine()
