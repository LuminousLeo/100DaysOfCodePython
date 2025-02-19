import random
def main():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #empty password
    password = ''

    #Easy Version
    #add letters to the password
    for i in range(nr_letters):
        password += letters[random.randint(0, len(letters) - 1)]

    #add symbols to the password
    for j in range(nr_symbols):
        password += symbols[random.randint(0, len(symbols) - 1)]

    #add numbers to the password
    for l in range(nr_numbers):
        password += numbers[random.randint(0, len(numbers) - 1)]

    print(password)

    #Hard Version
    #letter, numbers and symbols to be in the password
    pass_list = []
    #getting the letters
    if nr_letters > 0:
        for a in range(nr_letters):
            pass_list.append(letters[random.randint(0, len(letters) - 1)])

    #getting symbols
    if nr_symbols > 0:
        for b in range(nr_symbols):
            pass_list.append(symbols[random.randint(0, len(symbols) - 1)])

    #getting numbers
    if nr_numbers > 0:
        for c in range(nr_numbers):
            pass_list.append(numbers[random.randint(0, len(numbers) - 1)])


    #shuffle the list
    random.shuffle(pass_list)
    #turn the list into a string
    actual_password = ''
    for char in pass_list:
        actual_password += str(char)

    #print the password
    print(actual_password)


main()