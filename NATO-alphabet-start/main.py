import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# read the csv file
nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

# create the dictionary containing all of the phonetic codes
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# get user input
user_input = input('Input a word to convert to phonetic code: ')

# convert the user input into phonetic code
converted_word = [nato_alphabet_dict[char.upper()] for char in user_input]
print(converted_word)

# list comprehension is cool