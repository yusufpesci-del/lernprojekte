# match
#name = input("What's your name? ")

#if name == "Harry":
#    print("Gryffindor")
#elif name == "Hermione":
#    print("Gryffindor")
#elif name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")
#------------------------------------------------------------------------------
# version 2
#name = input("What's your name? ")

#if name == "Harry" or name == "Hermione" or name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")
#------------------------------------------------------------------------------
# version 3 match-case

#name = input("What's your name? ")

#match name:
 #   case "Harry":
 #       print("Gryffindor")
 #   case "Hermione":
 #       print("Gryffindor")
 #   case "Ron":
 #       print("Gryffindor")
 #   case "Draco":
  #      print("Slytherin")
 #   case _:
 #       print("Who?")
 #------------------------------------------------------------------------------
# version 4 match-case with multiple cases

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
