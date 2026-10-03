# This is a list of students in Hogwarts
#students = ["Hermione", "Harry", "Ron"]

#print(students [0]) # Ausgabe: Hermione
#print(students [1]) # Ausgabe: Harry
#print(students [2]) # Ausgabe: Ron

#students = ["Hermione", "Harry", "Ron"]

#for student in students:
 #   print(student)

#students = ["Hermione", "Harry", "Ron"]

#for i in students:
#    print(i)

#students = ["Hermione", "Harry", "Ron"]

#for i in range(len(students)):
 #   print(students[i])

#----------------------------------------------------------
#students = ["Hermione", "Harry", "Ron"]

#for i in range(len(students)):
#    print(i + 1, students[i])

#students = ["Hermione", "Harry", "Ron","Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
#for i in range(len(students)):
#    print(i + 1, students[i], houses[i])


#----------------------------------------------------------
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor ",
    "Draco": "Slytherin",
    }

for student in students:
    print(student, students[student], sep=", ")
