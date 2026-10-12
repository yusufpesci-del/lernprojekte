#Druck in psi umrechnen 1 bar = 14.5038 psi



def main():
    psi = convert(input("Geben Sie den Druck in bar ein: "))
    print(f"{psi:.2f} psi")



def convert(druck):
    bar = druck.split(" ")[0]
    return float(bar) * 14.5038


main()