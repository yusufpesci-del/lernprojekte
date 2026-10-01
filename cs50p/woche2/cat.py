
#3 Varianten für eine while Schleife, die 3 mal "wara" ausgibt

#i = 3
#while i != 0:
 #   print("wara")
 #   i = i - 1

#i = 1
#while i <= 3:
#    print("wara")
#    i = i + 1

#i = 0
#while i < 3:
#    print("wara")
#    i = i + 1

# for loop Varianten, die 3 mal "wara" ausgeben

#for i in [0, 1, 2]:
#    print("wara")

#for i in range(3):
 #   print("wara")

#for _ in range(3): #pythonic way
   # print("wara")

#----------------------------------------------------------
#print("wara\n" * 3) #pythonic way

#print("wara\n" * 3, end="") #pythonic way

#n = int(input("What´s n? "))
#if n < 0:
 #   n = int(input("What´s n? "))
  #  if n < 0:
   #     n = int(input("What´s n? "))
    #    if n < 0:
     #           print("n is negative")

#while True:
 #   n = int(input("What´s n? "))
  #  if n <= 0:
   #     continue
    #else:
     #   break

while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("wara")
