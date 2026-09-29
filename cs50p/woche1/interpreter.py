x, o, y = input("Expression: ").split(" ")

if o == "+":
    result = float(x) + float(y)
elif o == "-":
    result = float(x) - float(y)
elif o == "*":
    result = float(x) * float(y)
elif o == "/":
    result = float(x) / float(y)
print(f"{result:.1f}")

