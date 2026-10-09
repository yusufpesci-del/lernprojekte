# camelCase

#firstName
#preferredFirstName
#meinErstesProjekt

#first_name
#preferred_first_name
#mein_erstes_projekt

#camelCase: firstName
#snake_case: first_name


#   for zeichen in "firstName":
#    print(zeichen)

#camel = input("camelCase: ")
#print("snake_case: ", end="")
#for zeichen in camel:
 #   if zeichen.isupper():
#        print("_" + zeichen.lower(), end="")
 #   else:
 #       print(zeichen, end="")
#print()

#----------------------------------------------------------------
#2. variante
def main():
    camel = input("camelCase: ")
    print("snake_case:", convert(camel))


def convert(camel):
    ergebnis = ""
    for zeichen in camel:
        if zeichen.isupper():
            ergebnis += "_" + zeichen.lower()
        else:
            ergebnis += zeichen
    return ergebnis


main()
