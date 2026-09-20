def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    amount = d.replace("$", "")
    return float(amount)


def percent_to_float(p):
    value = p.replace("%", "")
    return float(value) / 100


main()