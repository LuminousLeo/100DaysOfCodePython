import random

def main():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    #get user inpyt
    user_ipt = int(input('What do you chose. Pick 0 for Rock, 1 for Paper or 2 for Scissors: '))
    #get cpu input
    cpu_ipt = random.randint(0, 2)

    #draw user input
    if user_ipt == 0:
        print(rock)
    elif user_ipt == 1:
        print(paper)
    else:
        print(scissors)

    print('Computer chose:')
    #draw cpu input
    if cpu_ipt == 0:
        print(rock)
    elif cpu_ipt == 1:
        print(paper)
    else:
        print(scissors)

    #results
    #draw
    if user_ipt == cpu_ipt:
        print("it's a draw")
    #rock wins
    elif user_ipt == 0 and cpu_ipt == 2:
        print('User wins')
    #paper wins
    elif user_ipt == 1 and cpu_ipt == 0:
        print('User wins')
    #scissor wins
    elif user_ipt == 2 and cpu_ipt == 1:
        print('User wins')
    else:
        print('CPU wins')



main()