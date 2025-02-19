import art
from random import randint


def main():
    #ask user if they want to play the blackjack
    play = input("Do you want to play of blackjack? Type 'y' or 'n': ")
    #if no then quit game
    if play.lower() == 'n':
        return
    # print the logo of the blackjack game
    print(art.logo)
    #create the cards, player_cards and dealer_cards lists
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    dealer_cards = []
    #variable to help with the while loop
    draw_boolean = True
    while draw_boolean:
        #draw cards for the player and the dealer
        draw(cards, player_cards, dealer_cards)
        #calculate the score for the player and the dealer
        player_score, dealer_score = score(player_cards, dealer_cards)
        #see if player withdrew a blackjack in first round
        if player_score == 21 and len(player_cards) == 2:
            break
        #print player cards and score
        print(f"Your cards: {player_cards}, current score: {player_score}")
        #print dealer's 1st card
        print(f"Dealer's first card: {dealer_cards[0]}")
        #check if player wants to draw another cards
        draw_card = input("Do you want to draw another card? Type 'y' or 'n': ")
        #if not then exit while loop
        if draw_card.lower() == 'n':
            draw_boolean = False

    #compare the scores to see who won the game
    game_over(player_score, dealer_score, player_cards, dealer_cards)

    #restart to check if the player wants to play a new game of blackjack
    main()


def draw(cards, player_cards, dealers_cards):
    """draw(cards, player_cards, dealers_cards)
    draws the cards for the player and the dealer"""

    #draw cards for the player and the dealer
    cards_len = len(cards)
    #if player and dealer have no cards (beginning of the game), then draw 2 cards
    if len(player_cards) == 0 and len(dealers_cards) == 0:
        for i in range(2):
            player_cards.append(cards[randint(0, cards_len - 1)])
            dealers_cards.append(cards[randint(0, cards_len - 1)])
    #else (not the beginning of the game), draw 1 card
    else:
        for i in range(1):
            player_cards.append(cards[randint(0, cards_len - 1)])
            dealers_cards.append(cards[randint(0, cards_len - 1)])


def score(player_cards, dealer_cards):
    """score(player_cards, dealer_cards)
    returns player and dealer's score"""

    #calculate player score
    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)

    return player_score, dealer_score


def game_over(player_score, dealer_score, player_cards, dealer_cards):
    """game_over(player_score, dealer_score, player_cards, dealer_cards)"""

    #check for a draw
    if player_score == dealer_score:
        print(f"Your final hand: {player_cards}, Final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("It´s a draw")
    elif player_score > 21 and dealer_score > 21:
        print(f"Your final hand: {player_cards}, Final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("It´s a draw. Both the dealer and player went over 21")
    #check if player has hit 21
    elif player_score == 21:
        print(f"Your final hand: {player_cards}, Final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        print('You win with blackjack. Congrats!')
    #check if dealer has hit 21
    elif dealer_score == 21:
        print(f"Your final hand: {player_cards}, Final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        print('Dealer wins with blackjack!')
    #check if player's score is higher than dealer's score (while being lesser than 21)
    elif player_score > dealer_score and player_score < 21:
        print(f"Your final hand: {player_cards}, Final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        print('You win. Congrats!')
    #if dealer's score is bigger than the player's score
    else:
        print(f"Your final hand: {player_cards}, Final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        print('Dealer wins!')

main()