
#plates

#def main():
 #   plate = input("Plate: ")
 #   if len(plate) < 2 or len(plate) > 6:
 #       print("Invalid")
#
 #   else:
  #      print("Valid")
        

#main()


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")        


def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False
    
    if not plate[:2].isalpha():
        return False
    if not plate.isalnum():
        return False 

    for  zeichen in plate:
        if zeichen.isdigit():
            if zeichen == "0":
                return False
            break
    zahl_gekommen = False          # vor der Schleife
    for zeichen in plate:
        if zeichen.isdigit():
            zahl_gekommen = True
        elif zahl_gekommen:
            return False
    return True
      
main()



