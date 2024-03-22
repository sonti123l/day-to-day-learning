import coffee_data as cf

user_choice = input("What would you like? (espresso/latte/cappuccino): ")


# function for taking user_input proceed further step
def take_user(choice):
    if choice.lower() == 'espresso':
        if (cf.resources['water'] >= cf.MENU['espresso']["ingredients"]["water"]) and \
                (cf.resources["coffee"] >= cf.MENU['espresso']["ingredients"]["coffee"]):
            remaining_water = cf.resources["water"] - cf.MENU['espresso']["ingredients"]["water"]
            remaining_coffee = cf.resources["coffee"] - cf.MENU['espresso']["ingredients"]["coffee"]
            cf.resources["water"] = remaining_water
            cf.resources["coffee"] = remaining_coffee
            total_money = cf.MENU['espresso']["cost"]
            print("Please insert coins.")
            quarter_coins = int(input("How many quarter?: "))
            dimes_coins = int(input("How many dimes?: "))
            nickles_coins = int(input("How many nickles?: "))
            pennies_coins = int(input("How many pennies?: "))
            calculate_money(Q=quarter_coins, D=dimes_coins, P=pennies_coins, N=nickles_coins, money=total_money)
            print("Here is your espresso Enjoy!")
            return choice
        else:
            print("Resources are less sorry for the inconvenience.Money Refunded.")
    elif choice.lower() == 'latte':
        if (cf.resources['water'] >= cf.MENU['latte']["ingredients"]["water"]) and (
                cf.resources["milk"] >= cf.MENU['latte']["ingredients"]["milk"]) and (
                cf.resources["coffee"] >= cf.MENU['latte']["ingredients"]["coffee"]):
            remaining_water = cf.resources["water"] - cf.MENU['latte']["ingredients"]["water"]
            remaining_milk = cf.resources["milk"] - cf.MENU['latte']["ingredients"]["milk"]
            remaining_coffee = cf.resources["coffee"] - cf.MENU['latte']["ingredients"]["coffee"]
            cf.resources["water"] = remaining_water
            cf.resources["milk"] = remaining_milk
            cf.resources["coffee"] = remaining_coffee
            total_money = cf.MENU['latte']["cost"]
            print("Please insert coins.")
            quarter_coins = int(input("How many quarter?: "))
            dimes_coins = int(input("How many dimes?: "))
            nickles_coins = int(input("How many nickles?: "))
            pennies_coins = int(input("How many pennies?: "))
            calculate_money(Q=quarter_coins, D=dimes_coins, P=pennies_coins, N=nickles_coins, money=total_money)
            print("Here is your latte Enjoy!")
            return choice
        else:
            print("Resources are less sorry for the inconvenience.Money Refunded.")
    elif choice.lower() == 'cappuccino':
        if (cf.resources['water'] >= cf.MENU['cappuccino']["ingredients"]["water"]) and (
                cf.resources["milk"] >= cf.MENU['cappuccino']["ingredients"]["milk"]) and (
                cf.resources["coffee"] >= cf.MENU['cappuccino']["ingredients"]["coffee"]):
            remaining_water = cf.resources["water"] - cf.MENU['cappuccino']["ingredients"]["water"]
            remaining_milk = cf.resources["milk"] - cf.MENU['cappuccino']["ingredients"]["milk"]
            remaining_coffee = cf.resources["coffee"] - cf.MENU['cappuccino']["ingredients"]["coffee"]
            cf.resources["water"] = remaining_water
            cf.resources["milk"] = remaining_milk
            cf.resources["coffee"] = remaining_coffee
            total_money = cf.MENU['cappuccino']["cost"]
            print("Please insert coins.")
            quarter_coins = int(input("How many quarter?: "))
            dimes_coins = int(input("How many dimes?: "))
            nickles_coins = int(input("How many nickles?: "))
            pennies_coins = int(input("How many pennies?: "))
            calculate_money(Q=quarter_coins, D=dimes_coins, P=pennies_coins, N=nickles_coins, money=total_money)
            print("Here is your cappuccino Enjoy!")
            return choice
        else:
            print("Resources are less sorry for the inconvenience.Money Refunded.")

    elif choice.lower() == "report":
        print(f"water: {cf.resources['water']}\nmilk: {cf.resources['milk']}\ncoffee: {cf.resources['coffee']}")
    else:
        print("given input is Wrong.")


# function for change giving and calculation of the money
def calculate_money(Q, D, N, P, money):
    new_Q = Q * 0.25
    new_P = P * 0.01
    new_N = N * 0.05
    new_D = D * 0.10
    total_sum = (new_D + new_N + new_P + new_Q) - money
    print(f"Here is ${total_sum} in change")


# calling the function take_user
take_user(choice=user_choice)
is_game = True
while is_game:
    new_user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    take_user(choice=new_user_choice)
