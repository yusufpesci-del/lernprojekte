
zaehler = {}

while True:
    material = input("Material: ").strip().lower()

    if material == "":
        break

    if material in zaehler:
            zaehler[material] += 1
    else:
            zaehler[material] = 1

for name, anzahl in zaehler.items():
    print(f"{name}: {anzahl}")