# Fraction: 1/4
#25%

while True:
    try:
        x, y = input("Fraction: ").split("/")    
        x = int(x)
        y = int(y)

        if x > y:
            continue

        fuel =  round(x / y *100)
        if fuel <= 1:
            print("E")
        elif fuel >= 99:
            print("F")
        else:
            print(f"{fuel}%")
        break
    except (ValueError, ZeroDivisionError):
        pass


