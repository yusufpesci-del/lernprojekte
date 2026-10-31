# Mein Code, Zeile für Zeile

Mein eigener Code, kommentiert zum Nachlesen. Zwei Teile:

| Teil | Inhalt |
|---|---|
| **Teil 1** | die vier Wiederholungsaufgaben (Woche 0–2) |
| **Teil 2** | Problem Set 3 — fuel, taqueria, grocery, outdated (Woche 3) |
| **Teil 3** | Woche 4 — Mitschrieb aus der Vorlesung (Libraries) |
| **Teil 4** | Problem Set 4 — alle sechs Aufgaben (Woche 4) |

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

# Teil 1 — Die vier Wiederholungsaufgaben

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

## Was in allen vier aus Teil 1 vorkommt

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

---

# Teil 2 — Problem Set 3 (Woche 3)

Alle vier benutzen `try`/`except`. Das ist das Thema der Woche: **nicht
prüfen, ob etwas gutgehen wird, sondern es versuchen und den Fehler
auffangen.**

## Aufgabe 1 — fuel.py

```python
while True:
    # "wiederhole für immer". Der Ausstieg ist das break weiter unten.
    try:
        # "versuch das". Geht dabei etwas schief, springt Python sofort
        # nach unten ins except, statt abzustürzen.

        x, y = input("Fraction: ").split("/")
        #  ^^^^                    ^^^^^^^^^^
        #  |                       zerlegt "3/4" in die Liste ["3", "4"]
        #  |
        #  zwei Namen links verlangen GENAU zwei Teile. Bei "3/4/5" oder
        #  bei "3" gibt es hier einen ValueError.

        x = int(x)
        y = int(y)
        # "3" wird zu 3. Vorher ist es Text, mit Text kann man nicht
        # rechnen. Bei "drei" gibt es hier den ValueError.

        if x > y:
            continue
        # continue = "Rest überspringen, nächster Durchlauf".
        # Ein Tank kann nicht voller als voll sein. Das ist KEIN Fehler,
        # den Python melden würde — 5/4 rechnet sich sauber aus. Dass es
        # fachlich unmöglich ist, weiß nur ich. Also ein if.

        fuel =  round(x / y *100)
        # x / y ergibt 0.75, mal 100 sind 75.0, round() macht 75 daraus.
        # Bei y = 0 entsteht hier der ZeroDivisionError.

        if fuel <= 1:
            print("E")
        elif fuel >= 99:
            print("F")
        else:
            print(f"{fuel}%")
        # Sonderfälle zuerst, der Normalfall ins else.

        break
        # raus aus der Schleife. Steht INNERHALB des try — wird also nur
        # erreicht, wenn vorher nichts schiefgegangen ist.

    except (ValueError, ZeroDivisionError):
        pass
    # Die runde Klammer fasst zwei Fehlerarten zusammen: beide sollen
    # dasselbe bewirken. pass = "tu nichts" — es gibt auch nichts zu tun.
    # Das break wurde nicht erreicht, also fragt die Schleife von selbst
    # noch einmal.
```

**Die Einsicht aus dieser Aufgabe:** es gibt zwei Arten von schlechten
Eingaben. Die eine wirft einen Fehler (`except`), die andere rechnet sich
sauber aus und ist trotzdem falsch (`if` + `continue`).

## Aufgabe 2 — taqueria.py

```python
menu = {"Baja Taco": 4.25, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00,
        "Tortilla Salad": 8.00, "Quesadilla": 8.50, "Super Burrito": 8.50,
        "Super Quesadilla": 9.50, "Taco": 3.00}
# Ein Dictionary: links der Name (Schlüssel), rechts der Preis (Wert).
# Die Daten stehen HIER, nicht in neun if-Zweigen. Deshalb reicht unten
# eine einzige Zeile für alle neun Gerichte.

gesamt = 0
# Der Sammelbehälter. Muss VOR der Schleife stehen — sonst wäre er bei
# jedem Durchlauf wieder 0 und die Summe würde nie wachsen.

while True:
    try:
        item = input("Item: ").strip().title()
        #                      ^^^^^^^ ^^^^^^^
        #                      |       "baja taco" wird zu "Baja Taco":
        #                      |       jedes Wort groß, Rest klein. Genau
        #                      |       die Schreibweise der Schlüssel oben.
        #                      Leerzeichen außen weg
        #
        # Hier entsteht der EOFError, wenn der Benutzer Strg+Z drückt.

        if item in menu:
            # in fragt bei einem Dictionary die SCHLÜSSEL ab, nie die Werte.
            gesamt += menu[item]
            # menu[item] holt den Preis, += legt ihn auf gesamt drauf.
            print(f"Total: ${gesamt:.2f}")
            # :.2f = immer zwei Stellen nach dem Komma. Ohne das stünde
            # da "Total: $11.5" statt "$11.50".

        # Kein else: unbekannte Eingaben werden still ignoriert. So will
        # es die Aufgabe.

    except EOFError:
        break
    # EOFError ist hier KEINE Panne. Strg+Z heißt "ich bin fertig".
    # Exceptions melden ungewöhnliche Situationen, nicht nur Fehler.
```

> **Stolperstein.** `.title` ohne Klammern tut nichts. Die Klammern sind
> das "wende es an". Ohne sie landet die *Methode selbst* in der Variablen,
> und `item in menu` findet dann nie etwas.

> **Auf Windows** ist es **Strg+Z und dann Enter**, nicht Strg+D wie in der
> englischen Aufgabe.

## Aufgabe 3 — grocery.py

```python
zaehler = {}
# Leeres Dictionary. Die Namen kennt das Programm vorher NICHT — anders
# als bei taqueria. Was eingetippt wird, kommt hinein.

while True:
    try:
        item = input().strip().upper()
        # input() ohne Beschriftung, weil die Aufgabe keine will.
        # .upper() macht "milk" und "MILK" zum gleichen Schlüssel.
    except EOFError:
        break
    # Wichtig: NUR das input() steht im try. Alles danach kann keinen
    # EOFError mehr werfen, also hat es dort nichts zu suchen.

    if item in zaehler:
        zaehler[item] += 1
        # schon gesehen: um eins hoch
    else:
        zaehler[item] = 1
        # zum ersten Mal: mit 1 anlegen
    # Dieses Muster — erst prüfen, dann hochzählen oder anlegen — IST der
    # Zähler. Ohne das else gäbe es beim ersten Mal einen KeyError, weil
    # man nichts hochzählen kann, was es noch nicht gibt.

for name in sorted(zaehler):
    # sorted() auf ein Dictionary liefert die SCHLÜSSEL alphabetisch,
    # als Liste. Die Werte sind darin nicht enthalten.
    print(f"{zaehler[name]} {name}")
    # Deshalb hier nachschlagen: zaehler[name] holt die Anzahl.
```

> **Stolperstein.** `sorted(zaehler).items()` geht nicht. `sorted()` gibt
> eine **Liste** zurück, und eine Liste hat kein `.items()` — das haben nur
> Dictionaries. Entweder durch die sortierten Schlüssel laufen und einzeln
> nachschlagen (so wie oben), oder `sorted(zaehler.items())`.

**Der Unterschied zu taqueria:** dort gibt es einen Katalog und nur was
darin steht zählt. Hier gibt es keinen — alles Eingetippte zählt. Die
Aufgabe entscheidet das, nicht die vorige Lösung.

## Aufgabe 4 — outdated.py

```python
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
# Die Reihenfolge ist die Information. Position 0 ist January, Position 8
# ist September — die Liste IST die Umrechnungstabelle.

while True:
    try:
        date = input("Date: ").strip()
        # Erst speichern. Der Text wird ZWEIMAL gebraucht: einmal für die
        # Frage nach dem Format, einmal zum Zerlegen.

        if "/" in date:
            # Kommt irgendwo ein Schrägstrich vor? Dann Zahlenformat.
            month, day, year = date.split("/")
            # date, nicht input(date) — der Text liegt schon da.
            # Monat zuerst: 8/9/1636 ist der 9. August, nicht der 8. September.

        else:
            # Kein Schrägstrich, also Wortformat: September 8, 1636
            monthday, year = date.split(", ")
            # Trennzeichen ", " MIT Leerzeichen, sonst klebt es am Jahr.
            # Ergebnis ["September 8", "1636"] — zwei Teile, zwei Namen.
            # "8 September 1636" hat kein Komma, gibt nur EIN Teil und
            # damit einen ValueError. Genau richtig: das Format ist falsch.

            month, day = monthday.split(" ")
            # "September 8" wird zu ["September", "8"]

            month = months.index(month) + 1
            # .index() liefert die Position: 8 für September. Gezählt wird
            # ab 0, Monate ab 1, also + 1.
            # Steht der Name nicht in der Liste ("Jan"), wirft .index()
            # einen ValueError — die Abkürzung wird dadurch von selbst
            # abgelehnt, ohne eine einzige zusätzliche Zeile.

        month = int(month)
        day = int(day)
        year = int(year)
        # Ab hier wieder GEMEINSAM. Beide Zweige haben dieselben drei
        # Namen gefüllt, deshalb steht der Rest nur einmal da.
        # int() auf eine Zahl ist harmlos: int(9) ist 9.

        if not 1 <= month <= 12 or not 1 <= day <= 31:
            continue
        # Wieder die Regel, die kein Fehler ist — wie x > y bei fuel.py.
        # 13/8/1636 rechnet sich sauber aus, es gibt den Monat nur nicht.
        # 1 <= month <= 12 ist die GUTE Aussage, not dreht sie um.

        print(f"{year}-{month:02}-{day:02}")
        # :02 = mindestens zwei Stellen, vorne mit Null auffüllen.
        # Aus 9 wird 09. Ohne das stünde da "1636-9-8".
        break

    except ValueError:
        pass
    # EIN except für fünf verschiedene Quellen:
    #   "neun/acht/1636"      int() auf keine Zahl
    #   "9/8"                 zwei Teile, drei Namen
    #   "8 September 1636"    fehlendes Komma, ein Teil statt zwei
    #   "Jan 1, 1970"         Monatsname nicht in der Liste
    #   "September 8 1636"    fehlendes Komma
    # Alle melden ValueError, alle sollen dasselbe bewirken: nochmal fragen.
```

---

## Was in Teil 2 neu dazukam

| Baustein | wofür |
|---|---|
| `try:` / `except:` | versuchen statt vorher prüfen |
| `except (A, B):` | zwei Fehlerarten, dieselbe Reaktion |
| `pass` | "tu nichts" — hier: einfach nochmal fragen |
| `EOFError` | Strg+Z: der Benutzer ist fertig, keine Panne |
| `continue` | Rest überspringen, nächster Durchlauf |
| `.index()` | an welcher Stelle steht der Wert in der Liste? |
| `sorted(...)` | Schlüssel alphabetisch, als **Liste** |
| `:.2f` / `:02` | Nachkommastellen / führende Null |
| `if … else` als Weiche | zwei Eingabeformen, ein gemeinsamer Schluss |

**Der Kerngedanke der Woche:** vorher jede Möglichkeit abzufragen wird bei
mehr als zwei Fällen unübersichtlich. Stattdessen macht man es einfach —
und fängt auf, wenn es schiefgeht. Auf Englisch heißt das *easier to ask
for forgiveness than permission*: lieber um Verzeihung bitten als um
Erlaubnis fragen.

**Und der Gegenpunkt, der genauso wichtig ist:** nicht jede falsche Eingabe
ist ein Fehler. `5/4` und `13/8/1636` rechnen sich sauber aus. Dass ein
Tank nicht überlaufen und ein Jahr nicht dreizehn Monate haben kann, ist
Fachwissen — das prüft man selbst, mit einem `if`.

---

# Teil 3 — Woche 4, Mitschrieb (Libraries)

Anders als Teil 1 und 2: das sind **keine** eigenen Lösungen, sondern die
Beispiele aus der Vorlesung, mitgetippt. Problem Set 4 kommt danach.

In den Dateien stehen die Zwischenstufen als Kommentar, mit `----` getrennt.
Unten steht jeweils die Endfassung — die ist hier erklärt.

## generate.py — random

```python
import random
# Holt die Bibliothek. Ab jetzt steht random.* zur Verfügung.
# random ist mitgeliefert, braucht also kein pip install.

cards = ["Jack", "Queen", "King"]

random.shuffle(cards)
# Mischt die Liste AN IHREM PLATZ und gibt NICHTS zurück.
# Deshalb kein "cards = random.shuffle(cards)" - daraus wuerde None.

for card in cards:
    print(cards)       # <-- HIER STECKT EIN FEHLER
```

> **Der Fehler.** `print(cards)` gibt die **ganze Liste** aus, und zwar
> dreimal, weil die Schleife dreimal läuft:
>
> ```
> ['Queen', 'Jack', 'King']
> ['Queen', 'Jack', 'King']
> ['Queen', 'Jack', 'King']
> ```
>
> Gemeint war `print(card)` — das einzelne Element dieses Durchlaufs:
>
> ```
> Queen
> Jack
> King
> ```
>
> `card` ist die Schleifenvariable, `cards` die Liste. Ein Buchstabe
> Unterschied. Das macht jeder einmal.

Die drei Werkzeuge aus `random`, die im Video vorkamen:

| | |
|---|---|
| `random.choice(liste)` | **ein** Element zufällig herausziehen |
| `random.randint(1, 10)` | ganze Zahl von 1 bis 10, beide Grenzen dabei |
| `random.shuffle(liste)` | Liste mischen, an ihrem Platz |

## average.py — statistics

```python
import statistics

print(statistics.mean([100, 90]))
# mean = Mittelwert. (100 + 90) / 2 = 95.0
# Kommt IMMER als Kommazahl zurueck, auch wenn es glatt aufgeht.
```

Dasselbe Muster wie bei `random`: Bibliothek, Punkt, Werkzeug, Klammern.
Wer das einmal sieht, kann jede Bibliothek benutzen.

## name.py — sys.argv

```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# sys.argv ist eine LISTE mit dem, was im Terminal stand.
# Position 0 ist IMMER die Datei selbst, ab 1 kommen die Argumente.
#
#   python name.py            -> ["name.py"]              Laenge 1
#   python name.py Yusuf      -> ["name.py", "Yusuf"]     Laenge 2
#
# Weniger als 2 heisst also: es wurde kein Name mitgegeben.
#
# sys.exit("...") gibt die Meldung aus UND beendet das Programm.
# Ein print allein wuerde weiterlaufen - und dann unten auf argv[1]
# zugreifen, das es nicht gibt. IndexError.

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
# [1:] ist ein AUSSCHNITT ab Position 1 - alles ausser dem Dateinamen.
# Damit funktioniert es fuer beliebig viele Namen:
#   python name.py Yusuf Frances   -> zwei Zeilen Ausgabe
```

**Warum `if` und nicht `try`?** Beides wäre richtig. Bei `argv` ist das `if`
üblicher, weil man die Länge einer Liste gefahrlos abfragen kann — dafür
braucht man kein `try`. Umgekehrt bei `int()`: da *muss* man es versuchen,
weil es keine Frage gibt, die vorher sicher antwortet.

**Und der Sinn der ganzen Sache:** das Programm fragt nicht mehr nach, es
bekommt alles beim Start mitgeliefert. `git commit -m "..."` ist genau
dasselbe Prinzip — `-m` und der Text sind `argv`.

## itunes.py — requests und JSON

```python
import json
import requests
import sys
# requests ist NICHT mitgeliefert: pip install requests war noetig.

if len(sys.argv) != 2:
    sys.exit()
# != 2 heisst: genau ein Suchbegriff, nicht null und nicht zwei.
# sys.exit() ohne Text beendet still.

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# Das + klebt den Suchbegriff hinten an die Adresse.
# requests.get(adresse) tut genau das, was der Browser tut:
# Adresse hin, Antwort zurueck. Es wird NICHTS runtergeladen,
# es gibt KEINE Datei - die Antwort ist Text.
# limit=50 heisst: bis zu 50 Treffer statt nur einem.

o = response.json()
# Macht aus dem Antwort-Text echte Python-Dictionaries und -Listen.
# Erst damit kann man einzelne Werte herausholen.

for result in o["results"]:
    print(result["trackName"])
```

Die letzten zwei Zeilen sind der schwierigste Teil der Woche, deshalb
ausführlich. Die Antwort von Apple ist **verschachtelt**:

```
o                      ein Dictionary
o["results"]           eine LISTE von Treffern
o["results"][0]        ein Dictionary - der erste Treffer
o["results"][0]["trackName"]   der Songtitel darin
```

Also: über die Liste laufen, und in jedem Durchlauf aus dem Dictionary den
einen Wert holen.

```python
for result in o["results"]:       # result ist jeweils EIN Treffer-Dictionary
    print(result["trackName"])    # daraus nur der Titel
```

**Das Vorgehen, wenn man eine fremde Antwort auswerten will:** erst mit
`json.dumps(o, indent=2)` ausgeben und **anschauen**, dann den Weg zum
gewünschten Wert heraussuchen. Blind raten geht schief, weil jeder Dienst
seine Antwort anders aufbaut.

## sayings.py und say.py — eigene Module

Zwei Dateien, die zusammenarbeiten. **sayings.py** ist die Werkzeugkiste:

```python
def main():
    hello("world")
    goodbye("world")
# Das ist, was passieren soll, wenn man DIESE Datei direkt startet.


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":
    main()
# Hier steckt der ganze Trick, siehe unten.
```

**say.py** benutzt sie:

```python
import sys

from sayings import hello
# Holt NUR hello aus der Datei sayings.py.
# Jede .py-Datei ist ein Modul und kann importiert werden -
# da ist kein Unterschied zu random oder requests.

if len(sys.argv) == 2:
    hello(sys.argv[1])
# Ohne das "sayings." davor, weil wir mit "from ... import" geholt haben.
```

### Warum das `if __name__` nötig ist

`import` heißt **nicht** "schau rein". Python **führt die Datei aus**, von
oben nach unten. Ohne das `if` sähe es so aus:

```python
# sayings.py OHNE das if
def hello(name): ...
def goodbye(name): ...

main()          # laeuft auch beim Importieren mit
```

Dann würde `python say.py` ausgeben:

```
hello, world        <- wollte keiner, kam durchs Importieren
goodbye, world      <- auch nicht
hello, Yusuf        <- das war gewollt
```

Python legt in jeder Datei automatisch eine Variable `__name__` an, und ihr
Inhalt hängt davon ab, **wie** die Datei ins Spiel kam:

| gestartet mit | `__name__` in `sayings.py` |
|---|---|
| `python sayings.py` | `"__main__"` |
| `import sayings` (aus `say.py`) | `"sayings"` |

Also fragt man einfach nach. Keine Zauberei — ein `if` auf eine Variable,
die Python für dich füllt.

Die zwei Unterstriche auf jeder Seite sind Absicht: so heißt bei Python
alles, was die Sprache selbst verwaltet und was man nicht aus Versehen
überschreiben soll.

> **Der Zusammenhang zu meinem eigenen Code:** in `stueckliste.py` steht
> unten `main()`. Solange nur ich die Datei starte, ist das in Ordnung.
> Sobald jemand `import stueckliste` schreibt, würde das Stücklisten-
> Programm mitten in einem fremden Programm anlaufen. Deshalb gehört die
> Startzeile in dieses `if`, sobald eine Datei auch nur vielleicht
> importiert wird.

> **Stolperstein.** Eine eigene Datei nie wie eine Bibliothek benennen.
> Heißt deine Datei `random.py`, importiert Python ab dann *deine* Datei
> statt der Bibliothek — und `random.choice` gibt es darin nicht.

---

## Was in Teil 3 neu dazukam

| Baustein | wofür |
|---|---|
| `import x` | fremden Code mitbenutzen, danach `x.werkzeug(...)` |
| `from x import y` | nur ein Werkzeug holen, danach `y(...)` ohne Punkt |
| `pip install x` | Bibliothek aus dem Internet nachladen |
| `random.choice` / `randint` / `shuffle` | Zufall |
| `statistics.mean` | Mittelwert |
| `sys.argv` | Liste der Argumente beim Start, `[0]` ist die Datei |
| `sys.exit("...")` | Meldung ausgeben und beenden |
| `liste[1:]` | Ausschnitt ab Position 1 |
| `requests.get(adresse)` | einen Dienst im Netz fragen |
| `.json()` | Antwort-Text → Python |
| `json.dumps(x, indent=2)` | Python → eingerückter Text |
| `if __name__ == "__main__"` | nur starten, wenn direkt gestartet |

**Der Kerngedanke der Woche:** bis Woche 3 war jedes Programm vollständig
selbst geschrieben. Ab hier nicht mehr. `import random` heißt: jemand anders
hat Zufallszahlen schon gelöst, ich benutze das.

Das ist der Punkt, an dem Programmieren vom Selbermachen zum Zusammensetzen
wird — und der Grund, warum das FM-Werkzeug überhaupt baubar ist. Eine
Oberfläche, PDF-Ausgabe, Daten speichern: alles schon geschrieben, von
anderen. Meine Arbeit daran ist die Fachlogik, nicht die Technik darunter.

---

# Teil 4 — Problem Set 4 (Libraries)

Wieder eigene Lösungen, wie in Teil 1 und 2. Alle drei benutzen fremde
Bibliotheken — das ist das Thema der Woche.

## Aufgabe 1 — emojize.py

```python
import emoji
# Die BIBLIOTHEK heisst emoji. Nicht emojize - das ist die Funktion darin,
# und auch der Name meiner Datei. Drei aehnliche Namen:
#   emoji       die Bibliothek, die man importiert
#   emojize     die Funktion darin
#   emojize.py  meine Datei
# "import emojize" wuerde die eigene Datei importieren.

text = input("Input: ")
# Fragen und MERKEN. Der Text muss vom Benutzer kommen, nicht im Code stehen.

smiley = emoji.emojize(text, language="alias")
#                      ^^^^  ^^^^^^^^^^^^^^^
#                      |     benannter Parameter - wie indent=2 bei
#                      |     json.dumps. Ohne ihn funktionieren nur die
#                      |     offiziellen Codes, nicht die Spitznamen.
#                      text OHNE Anfuehrungszeichen: der Inhalt,
#                      nicht das Wort "text".

print(f"Output: {smiley}")
```

**Warum `language="alias"` nicht optional ist.** Es gibt zwei Schreibweisen
pro Emoji — den offiziellen Code (`:thumbs_up:`) und den Spitznamen
(`:thumbsup:`). Nachgemessen:

| Eingabe | ohne `language` | mit `language="alias"` |
|---|---|---|
| `:1st_place_medal:` | 🥇 | 🥇 |
| `:money_bag:` | 💰 | 💰 |
| `:smile_cat:` | **nichts** | 😸 |
| `:thumbsup:` | **nichts** | 👍 |

`:smile_cat:` ist eines der drei Beispiele der Aufgabenstellung — ohne den
Parameter fällt die Aufgabe durch.

> **Stolperstein, zweimal passiert.** `text = print(...)`. `print` legt etwas
> auf den Bildschirm und gibt **nichts** zurück — in `text` landet `None`.
> **`print` steht nie rechts vom `=`.** Fragen, umwandeln und ausgeben sind
> drei getrennte Zeilen.

## Aufgabe 2 — figlet.py

```python
from pyfiglet import Figlet
# Die Bibliothek heisst pyfiglet, meine Datei figlet.py. Waeren sie gleich
# benannt, koennte Python sie nicht auseinanderhalten.
import random
import sys

figlet = Figlet()
# Hier entsteht das DING. Es merkt sich, welche Schriftart eingestellt ist.
# Muss VOR die Weiche, weil getFonts() unten von ihm kommt.

fonts = figlet.getFonts()
# Die Liste aller verfuegbaren Schriftarten. Wird zweimal gebraucht:
# zum Zufallsziehen und zum Pruefen.

if len(sys.argv) == 1:
    font = random.choice(fonts)
    # Keine Argumente -> zufaellige Schrift. random.choice zieht EIN
    # Element aus einer Liste, genau wie bei ["heads", "tails"].

elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    #   ^^^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #   genau drei Argumente    erstes ist -f ODER --font
    #
    # python figlet.py -f slant
    #        ^^^^^^^^^ ^^ ^^^^^
    #        argv[0]   [1]  [2]     -> Laenge 3
    #
    # "in" mit einer Liste/Tupel statt zwei == mit or - kuerzer und
    # leichter zu erweitern.

    font = sys.argv[2]
    if font not in fonts:
        sys.exit("Invalid usage")
    # Die dritte Pruefung als eigenes if IM Zweig, nicht in der
    # elif-Bedingung. Meine eigene Entscheidung - die Bedingung bleibt
    # kurz, und die Pruefung steht direkt bei der Variablen um die es geht.

else:
    sys.exit("Invalid usage")
    # Alles andere. sys.exit gibt die Meldung aus UND beendet.
    # Der einzige Ausgang OHNE gemeinsamen Schluss.

figlet.setFont(font=font)
text = input("Input: ")
output = figlet.renderText(text=text)
print(output)
# Ab hier gemeinsam. Beide guten Zweige haben EINE Variable gefuellt -
# font. Deshalb steht der Rest nur einmal da. Genau wie bei outdated.py,
# wo beide Zweige month, day und year gefuellt haben.
```

**Die Weiche mit drei Ausgängen:**

```
         ┌─ keine Argumente ────→ font = eine zufällige
         │
Weiche ──┼─ -f slant (geprüft) ─→ font = sys.argv[2]
         │
         └─ alles andere ───────→ sys.exit("Invalid usage")
                                       ↑ Ende

dann gemeinsam:  einstellen → fragen → zeichnen → ausgeben
```

**Was ist die Schriftart, was ist der Text?** Das war die erste
Verwechslung:

| | kommt aus |
|---|---|
| Schriftart (`slant`) | `sys.argv[2]` — beim Start mitgegeben |
| der Text (`CS50`) | `input()` — tippt der Benutzer danach |

> **Stolperstein.** Hier **kein** `Output: ` davor, anders als bei emojize.
> Das verschiebt die erste Zeile der Buchstabengrafik um acht Zeichen, das
> `C` bricht ab, und check50 fällt durch. Die Aufgabe zeigt nur die Grafik
> allein.

> **Stolperstein.** Tabs und Leerzeichen gemischt → `IndentationError`.
> In VS Code: Statusleiste unten rechts, `Spaces: 4` anklicken,
> „Convert Indentation to Spaces".

## Aufgabe 3 — adieu.py

```python
import inflect

p = inflect.engine()
# Wieder ein Ding, dasselbe Muster wie Figlet(). Zweites Mal am selben Tag.

persons = []
# Eine LISTE, keine {}. Bei grocery habe ich gezaehlt (Name -> Anzahl),
# hier sammle ich nur, in Reihenfolge. .append() und join wollen Listen.
# Muss VOR die Schleife, sonst ist sie bei jedem Durchlauf wieder leer.

while True:
    try:
        item = input().strip()
        # Nur die riskante Zeile steht im try. Hier entsteht der EOFError,
        # wenn der Benutzer Strg+Z drueckt.
    except EOFError:
        break

    persons.append(item)
    # AUSSERHALB des try, aber INNERHALB der Schleife.
    # Durchgespielt: input klappt -> anhaengen -> naechste Runde.
    #                input wirft EOFError -> break -> append laeuft nicht.

print("Adieu, adieu, to", p.join(persons))
# NACH der Schleife, am linken Rand - sonst kaeme die Ausgabe bei jedem
# Namen. Erstes Wort gross, zweites klein: "Adieu, adieu".
```

**Was `join` allein erledigt.** Das ist der Punkt der ganzen Aufgabe:

| Namen | Ausgabe |
|---|---|
| 1 | `Adieu, adieu, to Liesl` |
| 2 | `Adieu, adieu, to Liesl and Friedrich` |
| 3 | `Adieu, adieu, to Liesl, Friedrich, and Louisa` |
| 4 | `Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt` |

Kein Komma bei einem Namen. Nur „and" bei zwei. Kommas **und** „and" bei
drei oder mehr. Ein Anfänger baut dafür eine `if`-Kette mit Sonderfällen —
`join` macht alle sieben Fälle der Aufgabenseite mit einem Argument und
ohne jede Zusatzeinstellung.

**Wie ich `join` gefunden habe** — zum ersten Mal selbst Doku gelesen. Erst
`plural` geraten, das ist aber ein Wort rein, ein Wort raus (`name` →
`names`). Dann durch Eingrenzen: *was geht rein, was kommt raus?* Eine
Liste rein, ein fertiger Satzteil raus. Das war die Methode, nicht das
Finden eines Beispiels.

> **Stolperstein.** `.title()` aus taqueria mitgeschleppt. Dort war es
> nötig, weil die Eingabe zu den Schlüsseln der Speisekarte passen musste.
> Hier gibt es nichts zu vergleichen — aus `von Trapp` würde `Von Trapp`.

## Aufgabe 4 — game.py

```python
import random


def main():
    level = get_positive("Level: ")
    # Statt int(input(...)) der Aufruf der eigenen Prueffunktion.
    # Danach steht in level garantiert eine positive ganze Zahl -
    # diese Zeile kann nicht mehr abstuerzen.

    number = random.randint(1, level)
    # randint nimmt BEIDE Grenzen mit: bei Level 10 also auch die 10.

    while True:
        guess = get_positive("Guess: ")
        # Dieselbe Funktion, andere Beschriftung. DAS ist der Grund,
        # warum es Funktionen gibt.

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
        # Drei Faelle, und nur einer bricht ab. Die ersten zwei geben
        # etwas aus und lassen die Schleife weiterlaufen - ohne continue,
        # weil danach sowieso nichts mehr kommt.
        # else statt "elif guess == number": wenn weder kleiner noch
        # groesser, bleibt nur gleich.


def get_positive(prompt):
    # prompt ist die Beschriftung - "Level: " oder "Guess: ".
    # Dadurch taugt dieselbe Funktion fuer beide Stellen.
    while True:
        try:
            n = int(input(prompt))
            # Hier entsteht der ValueError bei "cat".
            if n > 0:
                return n
            # return verlaesst die GANZE Funktion und bringt n mit.
            # Nicht break - break wuerde nur die Schleife verlassen und
            # die Funktion wuerde ohne Wert weiterlaufen.
        except ValueError:
            pass
    # Was bei schlechter Eingabe passieren soll, steht NICHT da.
    # Wird return nicht erreicht, dreht die Schleife von selbst noch eine
    # Runde. Kein else, kein continue.


main()
# Muss HINTER beide def stehen. Python liest von oben nach unten -
# steht der Aufruf darueber, kennt es get_positive noch nicht: NameError.
```

**Zwei Hürden hintereinander, auf zwei verschiedenen Wegen abgewiesen:**

| Eingabe | wo sie scheitert |
|---|---|
| `cat` | am `int()` → `ValueError` → `except` |
| `-1` | **nicht** am `int()` — `int("-1")` ist in Ordnung — sondern am `if n > 0` |
| `0` | ebenfalls am `if` |

### Die wichtigste Einsicht der Aufgabe

Vor der Prüfung sah der Absturz bei `Level: -1` so aus:

```
ValueError: empty range in randrange(1, 0)
```

Die Fehlermeldung zeigte auf `random.randint(1, level)` — eine Zeile, die
nichts dafür konnte. Der schlechte Wert war durch die Tür gekommen und erst
zwei Schritte weiter explodiert.

**Deshalb: prüfen, wo der Wert hereinkommt — nicht dort, wo er später
Schaden anrichtet.** Mit `get_positive` erreicht `-1` das `randint` gar
nicht mehr.

### Der Unterschied zu `ist_brauchbar` aus der Stückliste

Beides sind Funktionen mit `return`, aber sie tun Verschiedenes:

| | gibt zurück | wer fragt |
|---|---|---|
| `ist_brauchbar(zeile)` | `True` / `False` | der Aufrufer entscheidet dann selbst |
| `get_positive(prompt)` | **die Zahl** | die Funktion fragt selbst, so lange es dauert |

Die zweite Form ist mächtiger: der Aufrufer bekommt garantiert etwas
Brauchbares und muss sich um den Fehlerfall nicht mehr kümmern. Aus zwei
absturzgefährdeten Zeilen in `main()` sind zwei geworden, die nicht mehr
abstürzen können.

## Aufgabe 5 — professor.py

```python
import random


def main():
    level = get_level()
    score = 0
    # Der Punktezaehler steht VOR der aeusseren Schleife - er soll ueber
    # alle zehn Aufgaben mitwachsen.

    for _ in range(10):
        # Genau zehn Aufgaben. for statt while, weil die Anzahl feststeht.
        # Der Unterstrich heisst "diesen Wert brauche ich nicht".

        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        solved = False
        # Das Merker-bool steht IN der aeusseren Schleife - es muss bei
        # jeder Aufgabe wieder auf False stehen. Stuende es oben, waere es
        # nach der ersten richtigen Antwort fuer immer True und die Loesung
        # wuerde nie mehr gezeigt.

        for _ in range(3):
            # Hoechstens drei Versuche. Danach ist die Schleife von selbst
            # zu Ende - kein Abbruch noetig.
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue
                # Keine Zahl zaehlt wie eine falsche Antwort: EEE, und der
                # Versuch ist verbraucht.

            if guess == answer:
                solved = True      # merken, dass es geklappt hat
                score += 1         # und einen Punkt dazu
                break
            print("EEE")

        if not solved:
            print(f"{x} + {y} = {answer}")
        # NACH der inneren Schleife. Von aussen sieht man nicht, ob sie
        # durch einen Treffer oder durch Erschoepfung geendet hat -
        # deshalb der Merker. Dasselbe Muster wie bei plates.py.

    print(f"Score: {score}")


def get_level():
    # Kein Parameter: die Beschriftung ist immer "Level: " und wird nur an
    # einer Stelle gebraucht. Anders als get_positive in game.py, wo mal
    # "Level: " und mal "Guess: " noetig war.
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)      # einstellig
    elif level == 2:
        return random.randint(10, 99)    # zweistellig
    elif level == 3:
        return random.randint(100, 999)  # dreistellig
    else:
        raise ValueError
        # Selbst einen Fehler werfen. Ohne diese Zeile faellt die Funktion
        # bei level=7 unten heraus und gibt stillschweigend None zurueck -
        # und in main() knallt es dann bei x + y, an einer Zeile die nichts
        # dafuer kann.


if __name__ == "__main__":
    main()
```

### Die eigentliche Schwierigkeit: wer wird zurückgesetzt, wer wächst mit?

| | wo es steht | warum |
|---|---|---|
| `score = 0` | **vor** der äußeren Schleife | soll über alle zehn Aufgaben mitwachsen |
| `solved = False` | **in** der äußeren Schleife | muss bei jeder Aufgabe neu bei Null anfangen |

Das ist die ganze Buchhaltung. Ein Fehler an dieser Stelle fällt nicht
sofort auf — das Programm läuft, es verhält sich nur falsch.

### Zwei Schleifen, zwei verschiedene Gründe

| | |
|---|---|
| `for _ in range(10)` | die **Anzahl** steht fest: zehn Aufgaben |
| `for _ in range(3)` | die **Obergrenze** steht fest: höchstens drei Versuche, `break` bei Treffer |

Bei `while True` wäre beides unbegrenzt. `range` begrenzt von selbst.

## Aufgabe 6 — bitcoin.py

```python
import sys
import requests
from secret import API_KEY
# secret.py enthaelt nur eine Zeile: API_KEY = "...".
# Sie steht in .gitignore und wird NICHT committet - sonst waere der
# Schluessel im oeffentlichen Repo und bliebe auch in der Historie stehen.


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
# Laengenpruefung wie in name.py. sys.exit gibt die Meldung aus UND beendet.

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
# float, nicht int - "2.5" Bitcoin muss gehen.
# Hier kann NUR ein ValueError entstehen.

try:
    response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}")
except requests.RequestException:
    sys.exit("Request failed")
# Zweites, GETRENNTES try - weil hier ein anderer Fehler moeglich ist.
# requests.RequestException gehoert zur Bibliothek, nicht zu Python.
# Der f-String setzt den Schluessel ein, ohne dass er im Code steht.

data = response.json()
price = float(data["data"]["priceUsd"])
# Die Antwort ist ein Dictionary im Dictionary:
#   { "data": { "id": "bitcoin", "priceUsd": "38761.0833" } }
# Also zwei eckige Klammerpaare hintereinander, eins pro Ebene.
# float() drum, weil der Preis als TEXT kommt - mit Anfuehrungszeichen.

print(f"${bitcoins * price:,.4f}")
# Das Komma ist das Tausendertrennzeichen: 38761.0833 wird zu 38,761.0833.
# .4f sind vier Nachkommastellen.
```

### Welches `except` gehört wohin?

Das war der Stolperstein: zuerst stand `except requests.RequestException`
beim `float()`. Die Frage ist immer, **was an dieser Stelle überhaupt
schiefgehen kann**:

| Stelle | möglicher Fehler |
|---|---|
| `float(sys.argv[1])` | `ValueError` |
| `requests.get(...)` | `requests.RequestException` |

Zwei Stellen, zwei Fehlertypen, zwei getrennte `try`-Blöcke. Ein falsch
gewähltes `except` fängt nicht nur das Falsche — es kann beim Prüfen selbst
abstürzen, hier mit `NameError: name 'requests' is not defined`.

### Der Schlüssel und das öffentliche Repo

Die Aufgabenstellung sagt schlicht „schreib den Schlüssel in die URL". Das
geht für Leute, deren Lösung nicht öffentlich im Netz steht. Bei einem
öffentlichen Repo ist ein committeter Schlüssel sofort für jeden lesbar —
und bleibt in der Git-Historie, auch wenn man ihn später herausnimmt.

Deshalb `secret.py` plus `.gitignore`: dieselbe Technik wie bei
`sayings.py` und `say.py`, eine eigene Datei zum Importieren. Nur dass
diese eine das Repo nie verlässt.

---

## Was in Teil 4 neu dazukam

| Baustein | wofür |
|---|---|
| benannter Parameter | `emojize(text, language="alias")`, wie `indent=2` |
| `Figlet()` / `inflect.engine()` | ein **Ding** erzeugen, das sich etwas merkt |
| `.setFont()` / `.renderText()` | Fähigkeiten dieses Dings — erst einstellen, dann benutzen |
| `getFonts()` | Liste der Möglichkeiten, zum Ziehen und zum Prüfen |
| `x in ("-f", "--font")` | eine von mehreren erlaubten Schreibweisen |
| `.append()` | an eine Liste hinten anhängen |
| `p.join(liste)` | Liste → lesbare Aufzählung mit Kommas und „and" |
| `random.randint(1, n)` | ganze Zahl von 1 bis n, **beide** Grenzen dabei |
| Funktion mit `return` in der Schleife | fragt, bis es passt, und **bringt den Wert mit** |
| `raise ValueError` | selbst einen Fehler werfen, statt `None` zurückzugeben |
| `daten["a"]["b"]` | verschachtelt nachschlagen, ein Klammerpaar pro Ebene |
| `requests.RequestException` | Fehlertyp **aus einer Bibliothek**, nicht aus Python |
| `:,.4f` | Tausenderkomma und vier Nachkommastellen |
| `from secret import API_KEY` | Geheimnisse in eine eigene, ignorierte Datei |

**Das Muster des Tages, dreimal passiert:** Werkzeug aus der vorigen Aufgabe
mitgeschleppt. `import sys` und `import json` bei emojize, weil sie im Video
vorkamen. `Output: ` bei figlet, weil emojize es wollte. `{}` und `.title()`
bei adieu, weil grocery und taqueria es brauchten.

Die Frage gehört an den Anfang jeder Aufgabe: **brauche ich das hier, oder
habe ich es nur zuletzt benutzt?**

**Und der Kerngedanke:** die schwierigste Logik in allen drei Aufgaben —
zwei Emoji-Schreibweisen, Buchstabengrafik aus ASCII, Kommaregeln für
Aufzählungen — habe ich nicht geschrieben. Das hat jemand anders schon
gelöst. Meine Arbeit war, das richtige Werkzeug zu finden und die Teile
richtig zusammenzustecken.
