import random
import pyperclip


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.sample(letters, random.randint(a=4, b=8))
    nr_symbols = random.sample(numbers, random.randint(a=2, b=4))
    nr_numbers = random.sample(symbols, random.randint(a=2, b=4))

    #empty password
    password = []

    #add letters to the password
    for i in range(len(nr_letters)):
        password.append(nr_letters[i])

    #add symbols to the password
    for j in range(len(nr_symbols)):
        password.append(nr_symbols[j])

    #add numbers to the password
    for l in range(len(nr_numbers)):
        password.append(nr_numbers[l])

    random.shuffle(password)
    new_password = ''.join(password)
    pyperclip.copy(new_password)
    return new_password