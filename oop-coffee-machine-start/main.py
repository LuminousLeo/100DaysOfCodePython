from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    #to help with the while loop
    machine_is_on = True

    #create coffee machine object
    coffe_machine = CoffeeMaker()

    #create menu object
    menu = Menu()

    #create money_machine object
    money_machine = MoneyMachine()

    while machine_is_on:
        user_input = input(f'What would you like? ({menu.get_items()}): ')

        #if user has inputted off
        if user_input == 'off':
            #turn of the machine
            machine_is_on = False
        #if user has inputted report
        elif user_input == 'report':
            #print the coffee machine's resources
            coffe_machine.report()
            money_machine.report()
        else:
            # find the drink
            item = menu.find_drink(user_input)

            #check if inputted item is in the menu
            if item is not None:
                #check if there are enough resources in the machine to make the drink
                if coffe_machine.is_resource_sufficient(item):
                    #call make_payment() method from money_machine object to check
                    #if user has inputted enough money to buy the drink
                    if money_machine.make_payment(item.cost):
                        #make the selected drink
                        coffe_machine.make_coffee(item)


main()

