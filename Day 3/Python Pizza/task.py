def main():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M or L: ")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")

    #my code
    bill = 0
    if size.upper() == 'S':
        bill += 15
        if pepperoni.upper() == 'Y':
            bill += 2
        if extra_cheese.upper() == 'Y':
            bill += 1
    elif size.upper() == 'M':
        bill += 20
        if pepperoni.upper() == 'Y':
            bill += 3
        if extra_cheese.upper() == 'Y':
            bill += 1
    else:
        bill += 25
        if pepperoni.upper() == 'Y':
            bill += 3
        if extra_cheese.upper() == 'Y':
            bill += 1

    print(f'Your final bill is: ${bill}.')


main()
