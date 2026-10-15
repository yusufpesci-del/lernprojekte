
def main():
    zaehler  = {}

    while True:
        position = input("Position: ").strip()
   
        if position == "fertig":
            break
        
        if not ist_brauchbar2(position):
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

def ist_brauchbar2(zeile):
    try:
        artikel, menge = zeile.split(" ")
        int(menge)
    except ValueError:
        return False
    return True


main()
