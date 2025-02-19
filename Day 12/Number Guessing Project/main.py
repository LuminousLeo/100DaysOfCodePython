import art
from random import randint
print(art.logo)

#main function
def main():
    print('Welcome to the number guessing game!')
    #generate correct number between 1 and 100
    correct_number = randint(1, 100)
    print("I'm thinking of a number from 0 to 100")
    #let user choose the difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or hard: ")
    #set the number of lives based on the chosen difficulty
    if difficulty.lower() == 'easy':
        lives = 10
    else:
        lives = 5

    #loop to keep the game going until the user is out of lives
    while lives > 0:
        print(f'You have {lives} attempts left to guess the number')
        guess_number = int(input('Make a guess: '))
        # check if player has won the game
        game_win = guess_compare(correct_number, guess_number)
        if game_win:
            break
        lives -= 1

    #check if player has lost the game
    if not game_win:
        print("You have no lives left. You lose!")


def guess_compare(correct_number, guess_number):
    """guess_compare(correct_number, guess_number)
    function used  to compare the correct number and the user's guess"""
    if guess_number == correct_number:
        print(f"You guessed the right number. The right number is {guess_number} You win!")
        return True
    elif guess_number < correct_number:
        print("Too low.")
        print("Guess again")
        return False
    else:
        print("Too high.")
        print("Guess again")
        return False



main()
