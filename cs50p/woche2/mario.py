

#for _ in range(3):
#    print("#")

#def main():
  #  print_columns(3)

#def print_columns(height):
 #   for _ in range(height):
 #       print("#")
    ##print("#\n" * height, end="")

#main()

#def main():
 #   print_row(4)


#def print_row(width):
 #   print("?" * width)
#main()


def main():
    print_square(6)


def print_square(size):

    #For each row in the square
    for i in range(size):

        #for each brick in the row
        for j in range(size):
            #Print a brick
            print("#", end="")
        print() #why do we need this print() here? because it moves the cursor to the next line after printing a row of bricks



main()
#weitere variante:

#Def print_square(size):
    #for i in range(size):
        #print("#" * size)
#main()