# Modules

# Variables

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

resource_dict = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
    "money": 30
    }


# Function

def check_resources(ingredients):
    check_condition=0
    for n in ingredients:
        resources_needed=(ingredients[n])
        resources_exists=(resource_dict[n])
        if resources_needed > resources_exists:
            check_condition += 1
    if check_condition == 0:
        return True
    else:
        return False


def debt_resource(ingredients):
    for n in ingredients:
        resource_dict[n] -= ingredients[n]


def update_wallet(customer_order):
    resource_dict["money"] += (MENU[customer_order]["cost"])


def entry_coins():
    quarters = int(input("how many quarters?: "))
    dimes    = int(input("how many dimes?: "))
    nickles  = int(input("how many nickles?: "))
    pennies  = int(input("how many pennies?: "))
    total_quarters = quarters * 0.25
    total_dimes = dimes * 0.1
    total_nickles = nickles * 0.05
    total_pennies = pennies * 0.01
    total_entry = (total_quarters + total_dimes + total_nickles + total_pennies)
    return(total_entry)


def got_drink(customer_order):
    debt_resource(ingredients)
    update_wallet(customer_order)
    print(f"Here your {customer_order}, ☕️☕️, enjoy it!")


# Main

# print(MENU["espresso"])
# print(MENU["espresso"]["cost"])
# print(MENU["espresso"]["ingredients"])
# print(MENU["espresso"]["ingredients"]["water"])

print (resource_dict)
should_end = False
while not should_end:
    customer_order = input("What would you like? (espresso/latte/cappuccino):").lower()
    ingredients=(MENU[customer_order]["ingredients"])
    
    if check_resources(ingredients) == True:
        print("Good to go")
        print("Please insert coins.")
        money_inserted=(entry_coins())
        drink_cost=float((MENU[customer_order]["cost"]))
        if money_inserted == drink_cost:
            got_drink(customer_order)
        elif money_inserted > drink_cost:
            change=money_inserted-drink_cost
            print(f"Your change is {change}")
            got_drink(customer_order)
        else:
            print(f"Not enough money, total entry {money_inserted}")
            more_coins=input("Would you like to insert more coins? (y/n):").lower()
            if more_coins == "y":
                while (money_inserted < drink_cost) and (more_coins == "y") :
                    money_inserted = money_inserted + (entry_coins())
                    if money_inserted < drink_cost:
                        more_coins=input(f"Not enough money, total entry: {money_inserted}, would like to insert more coins? (y/n)").lower()
                        if more_coins == "n":
                            print(f"Here your money back: {money_inserted}")
                    elif money_inserted > drink_cost:
                        print(f"your change is {money_inserted-drink_cost}")
                        got_drink(customer_order)
                    else:
                        print("Your Drink")
                        got_drink(customer_order)
            else:
                print(f"Here your money back : {money_inserted}")
                should_end=True
    else:
        print("Not engouht resources")
        should_end=True
        
    if customer_order == "report":
        print(resource_dict)
    should_end=True