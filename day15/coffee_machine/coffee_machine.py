from menu import MENU, resources

# TODO: 1
def serve_user():
    request = input("What would you like? (espresso/latte/cappuccino)")
    return request

# TODO: 2
def turn_off(status):
    status["on"] = False
    return status

# TODO: 3
def print_report(status):
    report = f"""
    Water: {status["water"]}ml
    Milk: {status["milk"]}ml
    Coffee: {status["coffee"]}ml
    Money: ${status["money"]}
"""
    print(report)
    return status

# TODO 4
def check_resources(status, drink):
    sufficient_ingredient = True
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if status[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            sufficient_ingredient = False
    return sufficient_ingredient

## TODO 5
def process_coins():
    quarters = int(input(f"How many quarters to insert?"))
    dimes = int(input(f"How many dimes to insert?"))
    nickles = int(input(f"How many nickles to insert?"))
    pennies = int(input(f"How many pennies to insert?"))
    value_inserted = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    print(f"${value_inserted} inserted.")
    return value_inserted

## TODO 6
def check_enough_coins(value, drink):
    if value < MENU[drink]['cost']:
        print(f"Sorry that is not enough money. ${value} refunded.")
        sufficient_money = False
    else:
        sufficient_money = True
    return sufficient_money

def prepare_coffee(status, drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        status[ingredient] -= amount
    status["money"] += MENU[drink]['cost']
    print(f"Here is your {drink}.")
    return status

def process_change(value_inserted, drink):
    drink_cost = MENU[drink]['cost']
    change = round(value_inserted - drink_cost, 2)
    print(f"Please take ${change} change.")

def run_machine():
    status = resources
    status["on"] = True
    status["money"] = 0

    while status["on"]:
        request = serve_user()

        if request == "off":
            status = turn_off(status)

        elif request == "report":
            status = print_report(status)

        elif request in MENU.keys():
            drink = request
            sufficient_ingredient = check_resources(status, drink)
            if sufficient_ingredient:
                value_inserted = process_coins()
                sufficient_money = check_enough_coins(value_inserted, drink)
                if sufficient_money:
                    status = prepare_coffee(status, drink)
                    process_change(value_inserted, drink)

        else:
            print(f"'{request}' is not a valid request, try again.")

if __name__ == "__main__":
    run_machine()
