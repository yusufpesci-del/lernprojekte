#Modulo operator
#even = gerade, odd = ungerade
#x = int(input("What's x? "))

#if x % 2 == 0:
 #   print("Even")
#else:
#    print("Odd")

#-----------------------------------------------------------------------------
# boolean function that returns True if n is even, and False if n is odd
#def main():
 # x = int(input("What's x? "))
  #if is_even(x):
   #   print("Even")
#  else:
     # print("Odd")


#def is_even(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False
    
#main()

#-----------------------------------------------------------------------------
#pythonic expressions

#def main():
#    x = int(input("What's x? "))
#    if is_even(x):
#        print("Even")
#    else:
#        print("Odd")


#def is_even(n):
#    return True if n % 2 == 0 else False

#main()

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0

main()
