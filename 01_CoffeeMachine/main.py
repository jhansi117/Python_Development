MENU = {"espresso": {"ingredients": {"water": 50,"coffee": 18,},"cost": 1.5,},
        "latte": {"ingredients": {"water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
        "cappuccino": {"ingredients": {"water": 250,"milk": 100,"coffee": 24,},"cost": 3.0,}
        }

resources = {"water": 300,"milk": 200,"coffee": 100,"money":0}

def coin_tracker(cost):
    print('Please insert the coins:')
    quarters = float(input('How many quarters: '))
    dimes = float(input('How many dimes: '))
    nickles = float(input('How many nickles: '))
    pennies = float(input('How many pennies: '))
    total = quarters + dimes + nickles + pennies
    if total > cost:
        change = total - cost
        return change
    elif total < cost:
        return -1

def stock_checker(order):
    if order=='espresso':
        if resources["water"]<MENU[order]["ingredients"]["water"]:
            return f"sorry we don't have enough water"
        elif resources["coffee"]<MENU[order]["ingredients"]["coffee"]:
            return f"sorry we don't have enough coffee"
    elif order=='latter' or order=='cappuccino':
        if resources["water"]<MENU[order]["ingredients"]["water"]:
            return f"sorry we don't have enough water"
        elif resources["coffee"]<MENU[order]["ingredients"]["coffee"]:
            return f"sorry we don't have enough coffee"
        elif resources["milk"]<MENU[order]["ingredients"]["milk"]:
            return f"sorry we don't have enough milk"
    return "available"

end = False
while end==False:

    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order=='espresso':
        if stock_checker(order) != "available":
            print(stock_checker(order))
        else:
            change = coin_tracker(MENU["espresso"]["cost"])
            
            if change == -1:
                print("Sorry there is no enough money, Money refunded.")
            else:
                if change>0:
                    print(f"Here is ${change} in change.")
                resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                resources["money"] = resources["money"] + MENU["espresso"]["cost"]
                print(f"Enjoy your {order}!")
            
        
    elif order=='latte':
        if stock_checker(order) != "available":
            print(stock_checker(order))
        else:
            change = coin_tracker(MENU["latte"]["cost"])
            
            if change == -1:
                print("Sorry there is no enough money, Money refunded.")
            else:
                if change>0:
                    print(f"Here is ${change} in change.")
                resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                resources["money"] = resources["money"] + MENU["latte"]["cost"]
                print(f"Enjoy your {order}!")

    elif order=='cappuccino':
        if stock_checker(order) != "available":
            print(stock_checker(order))
        else:
            change = coin_tracker(MENU["cappuccino"]["cost"])
            
            if change == -1:
                print("Sorry there is no enough money, Money refunded.")
            else:
                if change>0:
                    print(f"Here is ${change} in change.")
                resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                resources["money"] = resources["money"] + MENU["cappuccino"]["cost"]
                print(f"Enjoy your {order}!")
            print(f"Enjoy your {order}!")
    else:
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
