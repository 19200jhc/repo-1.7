'''
  Name: Alexander Scarlett
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
import random
f = open('boat.txt', 'r')
content = f.read()
print(content)
f.close()
print('\n')
ps = 0
rs = 0
g = 1
while True:
  print('------ Battleships ------\n')
  print(' ------- Game',g,'-------')
  pb = 0
  rb = 0
  Turn = 1
  end = 0
  while end == 0:
    print('\033[0;32m\n       - Turn',Turn,'-\n\033[0;37m')
    while True:
      p = input('\033[0;33mLoad(L)\033[0;37m, \033[0;31mFire(F)\033[0;37m, or \033[0;34mBlock(B)\033[0;37m? ')
      if p != 'L' and p != 'F' and p != 'B':
        print('\033[1;31m\nInvalid! Type L, F, or B!\n\033[0;37m')
      elif p == 'F' and pb < 1:
        print('\033[1;31m\nYou have no bullets!\n\033[0;37m')
      else:
        break
    r = random.randint(1,3)
    while True:
      if r == 2 and rb < 1:
        r = random.randint(1,3)
      else:
        break
    print()
    if p == 'L':
      pb = pb + 1
      print('You Loaded')
    if r == 1:
      rb = rb + 1
      print('The Enemy Loaded')
    if p == 'B':
      print('You Blocked')
    if r == 3:
      print('The Enemy Blocked')
    if p == 'F':
      print('You Fired')
      pb = pb - 1
      if r == 1:
        end = 1
    if r == 2:
      rb = rb - 1
      print('The Enemy Fired')
      if p == 'L':
        end = 2
      if p == 'F':
        end = 3
    if end > 0:
      break
    Turn = Turn + 1
    print('\nYou have',pb,'Bullets')
    print('The enemy has',rb,'Bullets')
  if end == 1:
    ps = ps + 1
    print('\033[0;32m\nYou Win\033[0;37m')
  if end == 2:
    print('\033[0;31m\nYou Lose\033[0;37m')
    rs = rs + 1
  if end == 3:
    print('\033[0;33m\nDraw\033[0;37m')
  print('\nThe score is:\nYou: ',ps,' Enemy: ',rs,'\n')
  while True:
    ag = input('Play Again(Y/N)? ')
    if ag == 'Y' or ag == 'N':
      break
    print('\nInvalid! Type Y or N!\n')
  if ag == 'Y':
    g = g + 1
    print('\n')
    continue
  else:
    break
print('\nGoodbye')