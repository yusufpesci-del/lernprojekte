import inflect

p = inflect.engine()

persons = []


while True:
    try:
        item = input().strip()
       
    except EOFError:
        break

    persons.append(item)
print("Adieu, adieu, to", p.join(persons))




  



    