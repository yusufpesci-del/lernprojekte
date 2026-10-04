

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
    for _ in range(size):
        for j in range(size):
            print("#", end="")
        print()



main()


