# Mein Code, Zeile für Zeile

Mein eigener Code, kommentiert zum Nachlesen. Zwei Teile:

| Teil | Inhalt |
|---|---|
| **Teil 1** | die vier Wiederholungsaufgaben (Woche 0–2) |
| **Teil 2** | Problem Set 3 — fuel, taqueria, grocery, outdated (Woche 3) |
| **Teil 3** | Woche 4 — Mitschrieb aus der Vorlesung (Libraries) |

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
