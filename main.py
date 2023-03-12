'''
  Name: Alexander Scarlett
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
import random
print('---Battleships---')
ps = 0
rs = 0
while True:
  pb = 0
  rb = 0
  Turn = 1
  end = 0
  while end == 0:
    print('\nTurn',Turn,'\n')
    while True:
      p = input('Load(L), Fire(F), or Block(B)? ')
      if p != 'L' and p != 'F' and p != 'B':
        print('Invalid')
      elif p == 'F' and pb < 1:
        print('You have no bullets!')
      else:
        break
    r = random.randint(1,3)
    while True:
      if r == 2 and rb < 1:
        r = random.randint(1,3)
      else:
        break
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
    print('You have',pb,'Bullets')
    print('The enemy has',rb,'Bullets')
  if end == 1:
    ps = ps + 1
    print('You Win')
  if end == 2:
    print('You Lose')
    rs = rs + 1
  if end == 3:
    print('Draw')
  print('\nThe score is:\nYou: ',ps,' Enemy: ',rs,'\n')
  while True:
    ag = input('Play Again(Y/N)? ')
    if ag == 'Y' or ag == 'N':
      break
    print('Invalid')
  if ag == 'Y':
    continue
  else:
    break
print('\nGoodbye')