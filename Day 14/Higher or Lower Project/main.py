import art
import game_data
from random import choice


def main():
    #print the logo of the game
    print(art.logo)
    #boolean for while loop
    winning = True
    #get the length game data list
    game_data_length = len(game_data.data)
    score = 0

    #do what is inside the loop until user loses
    while winning:
        #if it's th beginning of the game, select random dictionary from list for compare a
        if score == 0:
            compare_a = choice(game_data.data)
        #if it's not the beginning of the game then print logo and score
        else:
            for i in range(20):
                print("")

            print(art.logo)
            print(f"You're right! Current score: {score}")

            #if last round the user input was B then compare a becomes that option
            if user_input.upper() == 'B':
                compare_a = compare_b

        #display the A option
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
        #print vs art
        print(art.vs)
        # select random dictionary from list for compare b
        compare_b = choice(game_data.data)
        #if both options are the same then randomize option b again
        if compare_b == compare_a:
            compare_b = choice(game_data.data)
        #display b option
        print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
        #get user input
        user_input = input("Who has more followers? Type 'A' or 'B': ")
        #compare the number of followers
        winning, score = higher_or_lower(compare_a, compare_b, user_input, score)

    #if user has lost
    if not winning:
        print(f'You lost with a score of {score}')


def higher_or_lower(compare_a, compare_b, user_input, score):
    """higher_or_lower(compare_a, compare_b, user_input, score)
    compares the number of followers and checks if the one that the user choose has more
    followers than the other one"""

    #if user choose option A
    if user_input.upper() == 'A':
        #if a has more followers than b than user guessed right
        if compare_a['follower_count'] >= compare_b['follower_count']:
            score += 1
            return True, score
        else:
            return False, score

    #if user choose option b
    if user_input.upper() == 'B':
        # if b has more followers than a than user guessed right
        if compare_b['follower_count'] >= compare_a['follower_count']:
            score += 1
            return True, score
        else:
            return False, score



main()