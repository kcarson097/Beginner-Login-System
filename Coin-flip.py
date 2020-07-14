#**Coin Flip Simulation** - Write some code that simulates flipping a single coin however many times the user decides. 
#The code should record the outcomes and count the number of tails and heads

import random
#n = number of coinflips
def coin_flip(n):
    count = 0
    heads = 0
    tails = 0
    while count != n:
        head_tail = random.randint(0,1)
        if head_tail == 1:
            heads += 1
            print('Its Heads')
            count += 1
        else:
            tails += 1
            print('Its Tails')
            count += 1
        
    print('Tails count : ' +  str(tails))
    print('Heads count : ' +  str(heads))

flips = int(input('ENTER how many times you want to flip'))
coin_flip(flips)

#to prevent window closing
user = input('Thanks for playing')
