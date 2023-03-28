'''
  Name: Alexander Scarlett
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
#library for picking random numbers
import random

#function to input action for turn and check if valid
def chooseaction():
  while True:
    p = input('\033[0;33mLoad(L)\033[0;37m, \033[0;31mFire(F)\033[0;37m, or \033[0;34mBlock(B)\033[0;37m? ').upper()
    if p != 'L' and p != 'F' and p != 'B':
      print('\033[1;31m\nInvalid! Type L, F, or B!\n\033[0;37m')
    elif p == 'F' and bte[0] < 1:
      print('\033[1;31m\nYou have no bullets!\n\033[0;37m')
    else:
      break
  return p

#ascii art function
def art():
  f = open('boat.txt', 'r')
  content = f.read()
  print(content)
  f.close()
  print('\n')

#initializing list for storing score and game
scg = [0,0,1]

#print ascii art
art()

#instructional blurb
print("Instructions:\n\nBattleships is a game in which you face off against an enemy in a battle of wits and strategy. \nYour goal is to outsmart your opponent and defeat them. \nEach turn, you and your opponent choose one of three actions: Load, Block, or Fire. \n\nTo Load, press 'L'. \nThis will load one round into your cannons, ready to fire. \n\nTo Block, press 'B'. \nThis will block a bullet if your opponent attempts to shoot you, \npreventing your battleship from being sunk. \n\nTo Fire, press 'F'. \nThis will fire a round at the opponent. \nYou can only fire your cannons if they have at least one round in them. \n\nYour opponent can perform these same actions. \n\nIf you fire at the opponent while they are loading, you win. \nIf they shoot you while you are loading, they win. \nIf you both shoot at the same time, the game ends in a draw. \n\nAfter the game is ended, type 'Y' to play again or 'N' to end the program.\n\n")


#main game loop
while True:
  #header
  print('------ Battleships ------\n')
  print(' ------- Game',scg[2],'-------')
  
  #initializing ammo, turn and end variables
  Turn = 1
  bte = [0,0,0]
  
  #single turn loop
  while bte[2] == 0:
    #print turn number
    print('\033[0;32m\n       - Turn',Turn,'-\n\033[0;37m')
    
    #choose action
    p = chooseaction()
    
    #random number for enemy turn
    r = random.randint(1,3)
    
    #check if valid
    while True:
      if r == 2 and bte[1] < 1:
        r = random.randint(1,3)
      else:
        break
    print()
    
    #print actions taken on turn
    if p == 'L':
      bte[0] = bte[0] + 1
      print('You \033[0;33mLoaded\033[0;37m')
    if r == 1:
      bte[1] = bte[1] + 1
      print('The Enemy \033[0;33mLoaded\033[0;37m')
    if p == 'B':
      print('You \033[0;34mBlocked\033[0;37m')
    if r == 3:
      print('The Enemy \033[0;34mBlocked\033[0;37m')
    if p == 'F':
      print('You \033[0;31mFired\033[0;37m')
      bte[0] = bte[0] - 1
      if r == 1:
        bte[2] = 1
    if r == 2:
      bte[1] = bte[1] - 1
      print('The Enemy \033[0;31mFired\033[0;37m')
      if p == 'L':
        bte[2] = 2
      if p == 'F':
        bte[2] = 3
        
    #check if game ended
    if bte[2] > 0:
      break
      
    #new turn, print amount of ammo
    Turn = Turn + 1
    print('\nYour \033[0;33mammunition\033[0;37m:\033[0;36m',bte[0])
    print('\033[0;37mThe enemy\'s \033[0;33mammunition\033[0;37m:\033[0;36m',bte[1])
    
  #display ending, change score
  if bte[2] == 1:
    scg[0] = scg[0] + 1
    print('\033[0;32m\nYou Win\033[0;37m')
  if bte[2] == 2:
    print('\033[0;31m\nYou Lose\033[0;37m')
    scg[1] = scg[1] + 1
  if bte[2] == 3:
    print('\033[0;33m\nDraw\033[0;37m')
    
  #print score
  print('\nThe \033[0;34mscore\033[0;37m is:\nYou: \033[0;32m',scg[0],'\033[0;37m Enemy: \033[0;31m',scg[1],'\033[0;37m\n')
  
  #input new game, check if valid
  while True:
    ag = input('Play Again(\033[0;32mY\033[0;37m/\033[0;31mN\033[0;37m)? ').upper()
    if ag == 'Y' or ag == 'N':
      break
    print('\n\033[1;31mInvalid! Type Y or N!\033[0;37m\n')
    
  #repeat loop if yes, new game
  if ag == 'Y':
    scg[2] = scg[2] + 1
    print('\n')
    continue
    
  #else break loop, say goodbye
  else:
    break

print('\nOkay, maybe next time!')