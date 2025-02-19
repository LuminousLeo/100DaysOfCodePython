#MENU is a global variable
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

#resources is also a global variable (but this one can be changed)
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 50.00
}


def main():
    #machine is on by default
    turn_off = False

    #while loop to keep the machine running and asking user input
    while not turn_off:
        #get user input
        order = input("What would you like? (espresso/latte/cappuccino): ")
        #check if user input is in the MENU dict
        if order.lower() not in MENU.keys() and order.lower() != 'off' and order.lower() != 'report':
            print('We do not have the product that you have inputted')
        # if user input is off than the machine turns off
        elif order.lower() == 'off':
            turn_off = True
        # if user wants to check the amount of resources in the coffee machine
        elif order.lower() == 'report':
            resources_report()
        #if user input is in the menu
        else:
            #check if machine has enough resources to fulfill the user's order
            enough_resources = resource_check(order)

            #if resource_check() has returned true
            if enough_resources:
                #check the amount of each coin that the user is going to input
                quarters = int(input('How many quarters? '))
                dimes = int(input('How many dimes? '))
                nickels = int(input('How many nickels? '))
                pennies = int(input('How many pennies? '))

                #calculate the amount of money that the user has inserted
                money_inserted = round(0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies, 2)

                #check that the user has inserted enough money to purchase the drink they selected
                check_transaction(order, money_inserted)


def resources_report():
    """resources_report()
    prints the amount of water, milk, coffee and money
    that the coffee machine has"""
    for resource, amount in resources.items():
        if resource == 'water' or resource == 'milk':
            print(f"{resource}: {amount}ml")
        elif resource == 'coffee':
            print(f"{resource}: {amount}g")
        else:
            print(f"{resource}: {round(amount, 2)}$")


def resource_check(order):
    """resource_check(order)
    checks if machine has enough resources to fulfill user's request
    (by comparing amount needed and the amount of resources available).
    returns True if it has or False if it has not"""

    #loop through the nested ingredients dict in the dict in question (the one that the user chose)
    for ingredient, required_amount in MENU[order]['ingredients'].items():
        #if machine does not have enough resources to fulfill the user's request
        if resources[ingredient] < required_amount:
            #print the resource that is lacking
            print(f'Sorry, there is not enough {ingredient}.')
            #return false
            return False
        #if machine does have enough resources to fulfill the user's request
        else:
            #subtract the resources needed from the machine
            resources[ingredient] -= required_amount

    #return true if machine has enough resources
    return True


def check_transaction(order, money_inserted):
    """check_transaction(order, money_inserted)
    checks if user inserted enough money to buy the drink he selected, if needed, offers change and makes the user the selected drink"""

    #if user has not inserted enough money to buy the selected drink
    if money_inserted < MENU[order]['cost']:
        #refund the user their money
        print('You did not insert enough money to complete the purchase. Refunded money.')
    #if user has inserted the exact amount of money that the drink costs
    elif money_inserted == MENU[order]['cost']:
        #add the inserted money to the machine's resources
        resources['money'] += money_inserted
        #make the user the selected drink
        print(f'Here is your {order}, enjoy!')
    #if user has inputted more money than the cost of the drink
    else:
        #calculate the amount of change that the machine has to give to the user
        change = round(money_inserted - MENU[order]['cost'], 2)
        #add the rest of money to the machine's resources
        resources['money'] += (money_inserted - change)
        #give the user their change
        print(f'Here is your change: {change}$')
        #make the user their selected drink
        print(f'Here is your {order}, enjoy!')


main()