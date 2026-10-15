
def main():
    zaehler  = {}

    while True:
        position = input("Position: ").strip()
   
        if position == "fertig":
            break
        if not ist_brauchbar(position):
            continue
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
    teile = zeile.split(" ")
    if len(teile) != 2:
        return False
    if not teile[1].isdigit():
        return False
    return True


main()
