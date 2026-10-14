
def main():
    zaehler  = {}

    while True:
        position = input("Position: ").strip()
   
        if position == "fertig":
            break
        artikel, menge = position.split(" ")
        menge = int(menge)
        if artikel in zaehler:
            zaehler[artikel] += menge
        else: 
            zaehler[artikel] = menge

    gesamt = 0

    print()

    for artikel, menge in zaehler.items():
        print(f"{artikel}: {menge}")
        gesamt += menge

    print(f"Gesamt: {gesamt}")

def ist_brauchbar(zeile):
    if len(zeile) > 0:
        return False

    if not zeile[" "].isalpha():
        return False
    if not zeile.isalnum():
        return False

    return True


main()
