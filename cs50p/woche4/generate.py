#choice ist nich Neu, es kommt nicht von dir — es steckt in random, 
# deshalb der Punkt dazwischen.

#import random

#coin = random.choice(["heads", "tails"])
#print(coin)
#----------------------------------------------------
#from random import choice

#coin = choice(["heads", "tails"])
#print(coin)
#----------------------------------------------------
#import random

#number = random.randint(1, 10)
#print(number)

import random

cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(cards)