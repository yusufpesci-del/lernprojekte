#import cowsay
#import sys

#if len(sys.argv) == 2:
#    cowsay.cow("hello, " + sys.argv[1])
#-------------------------------------------
#hier nehmen wir aus dem sayings.py code hinein
#import sys

#from sayings import hello

#if len(sys.argv) == 2:
   # hello(sys.argv[1])

import emoji

text = input("Input: ")
smiley = emoji.emojize(text, language="alias")
print(f"Output: {smiley}")

