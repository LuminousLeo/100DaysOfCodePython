def main():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
    |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    #1st if statement
    print("Your mission is to find the treasure.")
    print('The Treasure is in the castle and you are on the the road that leads to said castle.')
    print("You have reached a fork in the road, but you don't know which way the castle is")
    if input('Do you want to go Left or Right: ').lower() == 'left':
        print('You went left and reached a garden with the castle beyond it.')
        print('There are two knights with light armor guarding the garden.')
        print('You can either sneak your way in the castle or you try to run to the entrance')
    else:
        print('You went right and got lost in the enchanted forest!\n Game Over!')
        exit()

    #second if statement
    if input('Do you attempt Sneak or Run: ').lower() == 'sneak':
        print('You have successfully sneaked your way into the treasure chamber. The treasure is in a big chest.')
        print('Because you are an expert thief you opened the lock with ease. There are three thousand gold coins and one sword in the chest.')
    else:
        print('You tried to run all the way from the garden to the treasure chamber and were caught because the guards are wearing light armor.')
        print('You are thrown in the dungeons and are left to rot there')
        print('Game Over!')
        exit()

    #third if statement
    if input('Try to carry the three thousand gold coins out of the castle: Y or N ').lower() == 'n':
        print('you have decided not to carry the gold coins')
        print('But what about the sword, you think. You look at it and realize it is the legendary dragonslayer sword')

        if input('Attempt to carry the sword out of the castle: Y or N ').lower() == 'y':
            print('You have successfully carried the sword out of the castle and sold it for 20000 gold coins to a wealthy mercenary.')
            print('Congratulations, you have won the game!')
            exit()
        else:
            print('You also decided to not carry the sword out of the castle because you are too weak to carry it.')
            print('You leave the castle empty handed.')
            print('Game Over!')
            exit()
    else:
        print('You tried to carry all three thousand gold coins in your backpack and, because of it, made too much noise trying to sneak out of the castle.')
        print('You are thrown in the dungeons and are left to rot there')
        exit()


main()

