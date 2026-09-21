#boolean expressions true or false
#indentation'Einrückung' is important in python, if you don't indent the code correctly, it will not work
#x = int(input("What's x? "))
#y = int(input("What's y? ")) 

#if x < y:
   # print("x is less than y")
#if x > y:
  #  print("x is greater than y")
#if x == y:
 #   print("x is equal to y")

#--------------------------------------------------------------------------------------------------------
#jetzt wird anstell von if elif else verwendet, um die Bedingungen zu überprüfen

#x = int(input("What's x? "))
#y = int(input("What's y? ")) 

#if x < y:
 #   print("x is less than y")
#elif x > y:
 #   print("x is greater than y")
#else: #logische Bedingung, wenn x nicht kleiner oder größer als y ist, dann muss es gleich sein
 #   print("x is equal to y")
#--------------------------------------------------------------------------------------------------------

#x = int(input("What's x? "))
#y = int(input("What's y? ")) 

#if x < y or x > y:
#    print("x is not equal to y")
#else:
#    print("x is equal to y")

#----------------------------------------------------------------------------------------------------------
#Bedingung umgedreht: direkt auf Gleichheit prüfen statt auf kleiner/größer.
x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")