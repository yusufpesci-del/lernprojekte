
hoehe = float(input("Lagerguthoehe in m: "))

if hoehe > 9:
    print("Sonderfall")
elif hoehe >= 6:
    print("Klasse 3")
elif hoehe >= 3:
    print("Klasse 2")
else:
    print("Klasse 1")
