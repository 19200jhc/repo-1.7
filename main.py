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
    elif p == 'F' and pb < 1:
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

#initializing score and game variables
ps = 0
rs = 0
g = 1

#main game loop
art()
while True:
  #header
  print('------ Battleships ------\n')
  print(' ------- Game',g,'-------')
  
  #initializing ammo, turn and end variables
  pb = 0
  rb = 0
  Turn = 1
  end = 0
  
  #single turn loop
  while end == 0:
    #print turn number
    print('\033[0;32m\n       - Turn',Turn,'-\n\033[0;37m')
    
    #choose action
    p = chooseaction()
    
    #random number for enemy turn
    r = random.randint(1,3)
    
    #check if valid
    while True:
      if r == 2 and rb < 1:
        r = random.randint(1,3)
      else:
        break
    print()
    
    #print actions taken on turn
    if p == 'L':
      pb = pb + 1
      print('You \033[0;33mLoaded\033[0;37m')
    if r == 1:
      rb = rb + 1
      print('The Enemy \033[0;33mLoaded\033[0;37m')
    if p == 'B':
      print('You \033[0;34mBlocked\033[0;37m')
    if r == 3:
      print('The Enemy \033[0;34mBlocked\033[0;37m')
    if p == 'F':
      print('You \033[0;31mFired\033[0;37m')
      pb = pb - 1
      if r == 1:
        end = 1
    if r == 2:
      rb = rb - 1
      print('The Enemy \033[0;31mFired\033[0;37m')
      if p == 'L':
        end = 2
      if p == 'F':
        end = 3
        
    #check if game ended
    if end > 0:
      break
      
    #new turn, print amount of ammo
    Turn = Turn + 1
    print('\nYour \033[0;33mammunition\033[0;37m:\033[0;36m',pb)
    print('\033[0;37mThe enemy\'s \033[0;33mammunition\033[0;37m:\033[0;36m',rb)
    
  #display ending, change score
  if end == 1:
    ps = ps + 1
    print('\033[0;32m\nYou Win\033[0;37m')
  if end == 2:
    print('\033[0;31m\nYou Lose\033[0;37m')
    rs = rs + 1
  if end == 3:
    print('\033[0;33m\nDraw\033[0;37m')
    
  #print score
  print('\nThe \033[0;34mscore\033[0;37m is:\nYou: \033[0;32m',ps,'\033[0;37m Enemy: \033[0;31m',rs,'\033[0;37m\n')
  
  #input new game, check if valid
  while True:
    ag = input('Play Again(\033[0;32mY\033[0;37m/\033[0;31mN\033[0;37m)? ').upper()
    if ag == 'Y' or ag == 'N':
      break
    print('\n\033[1;31mInvalid! Type Y, N, or R!\033[0;37m\n')
    
  #repeat loop if yes, new game
  if ag == 'Y':
    g = g + 1
    print('\n')
    continue
    
  #else break loop, say goodbye
  else:
    break

print('\nGoodbye')