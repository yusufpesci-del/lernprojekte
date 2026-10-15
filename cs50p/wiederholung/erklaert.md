# Die vier Wiederholungsaufgaben, Zeile für Zeile

Mein eigener Code, kommentiert zum Nachlesen.

**Achtung:** So dicht kommentiert man echten Code **nicht**. Das hier ist
Lernmaterial. In den richtigen `.py`-Dateien erklären Kommentare nur das
*Warum*, nicht das *Was* — steht so im Spickzettel unter Stil.

---

## Erst die Schreibweisen

Die drei Klammerarten bedeuten verschiedene Dinge. Das ist die häufigste
Verwechslung am Anfang:

| Schreibweise | heißt | Beispiel |
|---|---|---|
| `name(...)` | **etwas tun** — eine Funktion aufrufen | `int("5")`, `len(teile)` |
| `name[...]` | **etwas herausholen** — Position oder Schlüssel | `teile[1]`, `zaehler["Rohr"]` |
| `{...}` | ein **Dictionary** anlegen | `zaehler = {}` ist ein leeres |
| `[...]` allein | eine **Liste** anlegen | `["a", "e", "i"]` |

Und die drei Gleichheitszeichen:

| | heißt |
|---|---|
| `=` | **festlegen**: links bekommt den Wert von rechts |
| `==` | **fragen**: sind die beiden gleich? Antwort True oder False |
| `+=` | **dazuaddieren**: `x += 3` ist dasselbe wie `x = x + 3` |

---

## Aufgabe 1 — druck.py

```python
# Druck in psi umrechnen, 1 bar = 14.5038 psi

def main():                                    # legt die Funktion main an;
                                               # ausgeführt wird sie erst unten
    psi = convert(input("Geben Sie den Druck in bar ein: "))
    #     ^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #     |       input() fragt den Benutzer und gibt dessen
    #     |       Eingabe als TEXT zurück, z.B. "5 bar"
    #     |
    #     convert() bekommt diesen Text, rechnet, und gibt
    #     eine Zahl zurück. Die landet links in psi.

    print(f"{psi:.2f} psi")
    #       ^^^^^^^^^^
    #       f-String: {psi} wird durch den Wert ersetzt.
    #       :.2f heißt "als Kommazahl mit 2 Nachkommastellen"
    #       Aus 72.519 wird so 72.52


def convert(druck):                # druck ist der PARAMETER:
                                   # das, was von außen hereinkommt.
                                   # Innerhalb dieser Funktion heißt
                                   # die Eingabe eben druck.

    bar = druck.split(" ")[0]
    #         ^^^^^^^^^^^^ ^^^
    #         |            [0] holt den ERSTEN Eintrag heraus.
    #         |            Gezählt wird ab 0, nicht ab 1.
    #         |
    #         .split(" ") zerschneidet den Text an jedem Leerzeichen
    #         und gibt eine LISTE zurück:
    #         "5 bar"  ->  ["5", "bar"]
    #         Zusammen also: bar = "5"   (noch Text!)

    return float(bar) * 14.5038
    #      ^^^^^^ ^^^^^^^^^^^^^^
    #      |      float() macht aus dem Text "5" die Zahl 5.0.
    #      |      Ohne das ginge die Multiplikation nicht.
    #      |
    #      return beendet die Funktion und reicht das Ergebnis
    #      dorthin zurück, wo convert() aufgerufen wurde.


main()                             # DAS startet das Programm.
                                   # Ohne diese Zeile passiert gar nichts -
                                   # def legt nur an, ruft nicht auf.
```

**Der Kern dieser Aufgabe:** Wie zwei Funktionen zusammenarbeiten. `main`
reicht etwas hinein, `convert` rechnet und reicht ein Ergebnis zurück.
Was in `convert` an Variablen entsteht, sieht `main` **nicht** — nur das,
was `return` herausgibt.

---

## Aufgabe 2 — klasse.py

```python
hoehe = float(input("Lagerguthoehe in m: "))
#       ^^^^^ ^^^^^
#       |     input() liefert IMMER Text, auch bei "2.5"
#       |
#       float() macht daraus die Kommazahl 2.5.
#       Mit Text könnte man nicht vergleichen.

if hoehe > 9:                      # Python prüft von OBEN nach UNTEN
    print("Sonderfall")            # und nimmt den ERSTEN Zweig, der zutrifft

elif hoehe >= 6:                   # hier ist schon klar: hoehe ist NICHT > 9,
    print("Klasse 3")              # sonst wäre Python gar nicht hier.
                                   # Die obere Grenze ist also geschenkt.

elif hoehe >= 3:                   # und hier: nicht > 9 und nicht >= 6,
    print("Klasse 2")              # also automatisch unter 6

else:                              # else nimmt KEINE Bedingung.
    print("Klasse 1")              # Alles, was übrig bleibt, landet hier
```

**Der Kern:** In einer `elif`-Kette weiß jeder Zweig schon, dass alle
vorherigen nicht zutrafen. Von groß nach klein geprüft braucht man deshalb
nur die **untere** Grenze je Zweig.

> **Mein Fehler dabei:** Ich hatte erst `hoehe == 6` statt `hoehe >= 6`
> geschrieben. `==` trifft nur bei **exakt** 6 zu — 7, 8 und 9 fielen
> durch bis zum `else` und landeten in Klasse 1.

---

## Aufgabe 3 — material.py

```python
zaehler = {}                       # leeres Dictionary. Die geschweiften
                                   # Klammern machen es zum Dictionary.
                                   # Es steht VOR der Schleife, damit es
                                   # alle Durchläufe überlebt.

while True:                        # läuft endlos - nur sinnvoll mit break
    material = input("Material: ").strip().lower()
    #                              ^^^^^^^ ^^^^^^^
    #                              |       .lower() macht alles klein,
    #                              |       damit "Rohr" und "rohr" als
    #                              |       dasselbe gezählt werden
    #                              |
    #                              .strip() entfernt Leerzeichen am Anfang
    #                              und Ende. "  Rohr  " wird zu "Rohr"

    if material == "":             # "" ist LEERER Text (zwei Anführungs-
        break                      # zeichen, nichts dazwischen).
                                   # break verlässt die Schleife sofort.

    if material in zaehler:        # in fragt bei einem Dictionary die
                                   # SCHLÜSSEL ab: "kommt dieses Material
                                   # schon als Schlüssel vor?"

        zaehler[material] += 1     # ja -> den vorhandenen Wert um 1 erhöhen
        #       ^^^^^^^^
        #       in den eckigen Klammern steht der SCHLÜSSEL

    else:
        zaehler[material] = 1      # nein -> neu anlegen, Startwert 1.
                                   # Ohne diesen Zweig bliebe das Dictionary
                                   # ewig leer: += 1 bräuchte ja einen Wert,
                                   # zu dem es addieren kann.

for name, anzahl in zaehler.items():
#   ^^^^  ^^^^^^          ^^^^^^^^
#   |     |               .items() liefert pro Durchlauf ZWEI Dinge
#   |     |
#   |     der zweite Name bekommt den WERT
#   |
#   der erste Name bekommt den SCHLÜSSEL - immer in dieser Reihenfolge,
#   egal wie man die beiden nennt

    print(f"{name}: {anzahl}")
```

So sieht das Dictionary nach drei Eingaben aus:

```
Eingaben: Sprinklerkopf, Rohr, Sprinklerkopf

zaehler = {"sprinklerkopf": 2, "rohr": 1}
            ^^^^^^^^^^^^^   ^   ^^^^   ^
            Schlüssel    Wert   Schlüssel  Wert
```

**Der Kern:** Das Zählmuster — prüfen ob bekannt, erhöhen oder neu anlegen.
Das steckt in jedem Programm, das etwas zusammenzählt.

---

## Aufgabe 4 — stueckliste.py

Die Kür. Alles aus Woche 0 bis 2 zusammen.

```python
def main():
    zaehler = {}                   # leeres Dictionary für Artikel -> Menge

    while True:
        position = input("Position: ").strip()
        #          Beispiel-Eingabe: "Sprinklerkopf 12"

        if position == "fertig":
            break                  # Abbruchwort -> raus aus der Schleife

        if not ist_brauchbar(position):
        #  ^^^ ^^^^^^^^^^^^^^^^^^^^^^^
        #  |   ruft die Prüffunktion auf. Die gibt True oder False zurück.
        #  |
        #  not dreht die Antwort um: "wenn sie NICHT brauchbar ist"
            continue
        #   continue überspringt den Rest dieses Durchlaufs und fragt
        #   gleich wieder. Der Gegenspieler von break:
        #   break = Schleife beenden, continue = diesen Durchlauf beenden

        artikel, menge = position.split(" ")
        #       ^^^^^^   ^^^^^^^^^^^^^^^^^^^
        #       |        split liefert eine Liste mit zwei Teilen
        #       |
        #       ZWEI Namen links: der erste Teil geht in artikel,
        #       der zweite in menge. Die Anzahl muss passen,
        #       sonst gibt es einen ValueError.
        #       -> "Sprinklerkopf 12" wird zu artikel="Sprinklerkopf"
        #          und menge="12"   (menge ist noch TEXT!)

        menge = int(menge)         # aus dem Text "12" die Zahl 12 machen.
                                   # Ohne das würde += Texte aneinander-
                                   # hängen statt zu addieren.

        if artikel in zaehler:     # schon bekannt? Gefragt wird nach
                                   # ARTIKEL - demselben, das auch als
                                   # Schlüssel hineingelegt wird
            zaehler[artikel] += menge      # ja  -> Menge dazuaddieren
        else:
            zaehler[artikel] = menge       # nein -> mit dieser Menge anfangen

    # ---- ab hier ist die Schleife vorbei, die Eingabe ist durch ----

    gesamt = 0                     # Zähler für die Summe, startet bei 0.
                                   # VOR der Schleife, damit er mitwächst.

    print()                        # print ohne Inhalt = nur eine Leerzeile

    for artikel, menge in zaehler.items():
        print(f"{artikel}: {menge}")       # eine Zeile je Artikel
        gesamt += menge                    # und die Menge zur Summe addieren

    print(f"Gesamt: {gesamt}")
    # Diese Zeile steht NICHT eingerückt - sie gehört nicht mehr zur
    # Schleife. Eingerückt käme sie nach jedem Artikel.


def ist_brauchbar(zeile):          # beantwortet eine Ja/Nein-Frage.
                                   # Namen mit is_/ist_ sind dafür üblich.

    teile = zeile.split(" ")       # "Rohr 40"      -> ["Rohr", "40"]
                                   # "Rohr"         -> ["Rohr"]
                                   # "Rohr 3 Stueck"-> ["Rohr", "3", "Stueck"]
                                   # Diese Zeile scheitert NIE.

    if len(teile) != 2:            # len() zählt hier die TEILE der Liste,
        return False               # nicht die Zeichen.
                                   # != heißt "ungleich".
                                   # return False beendet die Funktion sofort.

    if not teile[1].isdigit():     # teile[1] ist der ZWEITE Eintrag
        return False               # (ab 0 gezählt).
                                   # .isdigit() fragt: nur Ziffern drin?

    return True                    # wird nur erreicht, wenn KEINE der
                                   # beiden Prüfungen zugeschlagen hat


main()
```

**Der Kern:** Die Ausgabe steht nur an **einer** Stelle, in `main`. Die
Prüffunktion entscheidet nur und gibt True oder False zurück. Kommt eine
dritte Regel dazu, fasst man die anderen nicht an.

---

## Aufgabe 4, zweite Fassung — stueckliste2.py

`main` ist identisch, nur die Prüffunktion ist anders — mit den Mitteln
aus Woche 3:

```python
def ist_brauchbar2(zeile):
    try:                           # "versuch das hier, es kann schiefgehen"

        artikel, menge = zeile.split(" ")
        # genau die Zeile aus main. Sie wirft von selbst einen ValueError,
        # wenn NICHT genau zwei Teile herauskommen:
        #   "Rohr"          -> not enough values to unpack
        #   "Rohr 3 Stueck" -> too many values to unpack

        int(menge)
        # auch die aus main. Wirft ValueError bei "zwei" oder "40.5".
        # Kein "=" davor: das Ergebnis interessiert hier nicht,
        # nur OB es klappt.

    except ValueError:             # fängt BEIDE Fälle ab - beide sind
        return False               # ValueError, obwohl sie an verschiedenen
                                   # Zeilen entstehen

    return True                    # kein Fehler aufgetreten -> brauchbar
```

**Der Unterschied zur ersten Fassung:** Die `if`-Variante baut die
Bedingungen von Hand nach. Die `try`-Variante prüft mit **genau den
Operationen**, die `main` danach ausführt — sie kann also nicht
auseinanderlaufen, wenn `main` sich ändert.

**Und ein echter Unterschied im Ergebnis:**

| Eingabe | mit `if` | mit `try` |
|---|---|---|
| `Rohr -5` | False | True |

`"-5".isdigit()` ist `False` (das Minus ist keine Ziffer), `int("-5")`
funktioniert aber. Beide Fassungen sind richtig — sie beantworten nur
leicht verschiedene Fragen. Welche man will, ist eine fachliche
Entscheidung: darf eine Menge negativ sein?

---

## Was in allen vier vorkommt

| Baustein | wofür |
|---|---|
| `input()` | fragt den Benutzer, liefert **immer** Text |
| `int()` / `float()` | macht aus Text eine Zahl |
| `.strip()` | Leerzeichen außen weg |
| `.split(" ")` | zerlegt Text in eine **Liste** |
| `f"...{x}..."` | setzt Werte in Text ein |
| `while True` + `break` | wiederholen bis zum Abbruchwort |
| `in` | kommt das vor? (Liste: Einträge, Dictionary: Schlüssel) |
| `{}` + `[schlüssel]` | Dictionary anlegen und darauf zugreifen |
| `.items()` | Schlüssel **und** Wert durchlaufen |
| `def` + `return` | Arbeit auslagern und Ergebnis zurückgeben |

Wer diese zehn Zeilen versteht, kann die vier Programme lesen — und die
meisten kleinen Programme überhaupt.
