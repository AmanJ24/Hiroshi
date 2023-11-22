MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

def machine():
    money = 0
    should_continue = True   
    global resources
    while should_continue:     
        order = input("What would you like? (espresso/latte/cappuccino): ")                   

        if order == "latte" or order == "cappuccino" or order == "espresso":
            drink = MENU[order]
            drink_in = drink['ingredients']
            drink_water = drink_in['water']
            drink_coffee = drink_in['coffee']
            drink_milk = drink_in['milk']
            drink_cost = drink['cost']

            if resources['water'] >= drink_water:
                if resources['milk'] >= drink_milk:
                    if resources['coffee'] >= drink_coffee:
                        quarter = int(input("How many quarters?: "))
                        dime = int(input("How many dimes?: "))
                        nickel = int(input("How many nickels?: "))
                        pennies = int(input("How many pennies?: "))

                        quarter_1 = quarter * 0.25
                        dime_1 = dime * 0.10
                        nickel_1 = nickel * 0.05
                        pennies_1 = pennies * 0.01
                        total_inserted = quarter_1 + dime_1 + nickel_1 + pennies_1
                        if total_inserted >= drink_cost:
                            money += total_inserted
                            returned = total_inserted - drink_cost
                            returned = "{:.2f}".format(returned)
                            print(f"Here is ${returned} dollars in change.")
                            print(f"Here is your {order}. Enjoy!")

                            resources['water'] -= drink_water
                            resources['milk'] -= drink_milk
                            resources['coffee'] -= drink_coffee
                        else:
                            print("Sorry, that's not enough money. Money refunded.")
                    else:
                        print("Sorry, we are out of coffee.")
                else:
                    print("Sorry, We are out of milk.")
            else:
                print("Sorry, We are out of water.")                    

        if order == 'report':
            print(f"Water: {resources['water']}")
            print(f"Milk: {resources['milk']}")
            print(f"Coffee: {resources['coffee']}")
            print("Money: $" + "{0:.2f}".format(money))
        if order == 'off':
            should_continue = False    

machine()