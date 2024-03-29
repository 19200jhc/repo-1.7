'''
  Name: Alexander Scarlett
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023

  TIP: Use assessment guide to help guide you through this Internal
'''

# libraries
import random
import os
import time


# function to input action for turn and check if valid
def chooseaction():
    while True:
        print(
          '\033[0;33mLoad(L)\033[0;37m, \033[0;32mFire(F)\033[0;37m,', end=''
        )
        print(' or \033[0;34mBlock(B)\033[0;37m', end='')
        p = input('? ').upper()
        if p != 'L' and p != 'F' and p != 'B':
            print('\033[1;31m\n❌ Invalid! Type L, F, or B!\n\033[0;37m')
        elif p == 'F' and bte[0] < 1:
            print('\033[1;31m\n❌ You have no bullets!\n\033[0;37m')
        else:
            break
    print()
    return p


# ascii art function
def art():
    f = open('boat.txt', 'r')
    content = f.read()
    print(content)
    f.close()
    print('\n')


# initializing list for storing score and game
scg = [0, 0, 1]

# print ascii art
art()

# instructional blurb
print("\033[1;37mInstructions:\033[0;37m\n")
print("Battleships is a game in which you face off", end=" ")
print("against an enemy in a battle of wits and strategy.")
print("Your goal is to outsmart your opponent and defeat them.")
print("Each turn, you and your opponent choose one of", end=" ")
print("three actions: Load, Block, or Fire. \n")
print("\033[1;37mTo Load, press 'L'.\033[0;37m")
print("This will load one round into your cannon, ready to fire. \n")
print("\033[1;37mTo Block, press 'B'.\033[0;37m")
print("This will block a bullet if your opponent attempts to", end=" ")
print("shoot you, \npreventing your battleship from being sunk. \n")
print("\033[1;37mTo Fire, press 'F'.\033[0;37m")
print("This will fire a round at the opponent.")
print("You can only fire your cannon if it has at least one round in it.\n")
print("Your opponent can perform these same actions. \n")
print("If you fire at the opponent while they are loading, you win.")
print("If they shoot you while you are loading, they win.")
print("If you both shoot at the same time, the game ends in a draw. \n")
print("After the game is ended, type 'Y' to play again or 'N'", end=" ")
print("to end the program.\n\n")

input('\033[0;33mPress ENTER to start!\033[0;37m')
print('\n')

# main game loop
while True:
    os.system('clear')
    # header
    print('⭐ ⭐ ⭐ Battleships ⭐ ⭐ ⭐\n')
    print(' --------- Game', scg[2], '---------')

    # initializing ammo, turn and end variables
    Turn = 1
    bte = [0, 0, 0]

    # single turn loop
    while bte[2] == 0:
        # print turn number
        print('\033[0;31m\n         - Turn', Turn, '-\n\033[0;37m')

        # choose action
        p = chooseaction()

        # random number for enemy turn and check if valid
        while True:
            r = random.randint(1, 3)
            if r == 2 and bte[1] < 1:
                continue
            break

        # print actions taken on turn
        if p == 'L':
            bte[0] = bte[0] + 1
            print('You \033[0;33mLoaded\033[0;37m')
        if p == 'B':
            print('You \033[0;34mBlocked\033[0;37m')
        if p == 'F':
            print('You \033[0;32mFired\033[0;37m')
            bte[0] = bte[0] - 1
            if r == 1:
                bte[2] = 1
        if r == 1:
            bte[1] = bte[1] + 1
            print('The Enemy \033[0;33mLoaded\033[0;37m')
        if r == 3:
            print('The Enemy \033[0;34mBlocked\033[0;37m')
        if r == 2:
            bte[1] = bte[1] - 1
            print('The Enemy \033[0;32mFired\033[0;37m')
            if p == 'L':
                bte[2] = 2
            if p == 'F':
                bte[2] = 3

        # check if game ended
        if bte[2] > 0:
            break

        # new turn, print amount of ammo
        Turn = Turn + 1
        print('\nYour \033[0;33mammunition\033[0;37m:\033[0;36m', bte[0])
        print('\033[0;37mThe enemy\'s \033[0;33mammunition', end='')
        print('\033[0;37m:\033[0;36m', bte[1])

    # display ending, change score
    if bte[2] == 1:
        scg[0] = scg[0] + 1
        print('\033[0;32m\nYou Win!\033[0;37m')
    if bte[2] == 2:
        print('\033[0;31m\nYou Lose!\033[0;37m')
        scg[1] = scg[1] + 1
    if bte[2] == 3:
        print('\033[0;33m\nDraw!\033[0;37m')

    # print score
    print('\nThe \033[0;34mscore\033[0;37m is:')
    print('You: \033[0;32m', scg[0], '\033[0;37m', end=' ')
    print('Enemy: \033[0;31m', scg[1], '\033[0;37m\n')

    # input new game, check if valid
    while True:
        ag = input(
            'Play Again(\033[0;32mY\033[0;37m/\033[0;31mN\033[0;37m)? '
        ).upper()
        if ag == 'Y' or ag == 'N':
            break
        print('\n\033[1;31m❌ Invalid! Type Y or N!\033[0;37m\n')

    # repeat loop if yes, new game
    if ag == 'Y':
        scg[2] = scg[2] + 1
        print('\n')
        continue

    # else break loop, say goodbye
    else:
        break

os.system('clear')
print('\nOkay, maybe next time!')
time.sleep(4)
os.system('clear')
print('\033[1;34mBattleships\033[0;37m\n')
time.sleep(1.5)
print('By \033[0;33mAlex Scarlett\033[0;37m\n')
time.sleep(1.5)
print('Made with Replit\n')
time.sleep(2)
print('\n\033[1;32mThanks for Playing')
