# Spickzettel — Python Grundlagen

Alles aus CS50P Woche 0 bis 2, in der Reihenfolge, in der es Sinn ergibt.
Nicht zum Auswendiglernen, sondern zum Nachschlagen.

Die Kästen **Stolperstein** sind Fehler, die mir selbst passiert sind.
Die lohnen sich am meisten.

---

## Das Grundgerüst

Fast jedes kleine Programm hat dieselbe Form:

```python
text = input("Frage? ")        # 1. etwas hereinholen
ergebnis = text.upper()        # 2. damit etwas machen
print(ergebnis)                # 3. etwas ausgeben
```

Hereinholen, verarbeiten, ausgeben. Wenn du bei einer Aufgabe nicht
weiterkommst, frag dich zuerst: Was kommt rein? Was soll rauskommen?
Der Weg dazwischen ergibt sich meistens von selbst.

**Python macht nur, was dasteht.** Eine Rechnung wird nicht angezeigt,
nur weil sie gerechnet wurde — dafür braucht es `print`. Nur im
interaktiven Modus (`>>>`) wird jedes Ergebnis automatisch gezeigt.

### Von oben nach unten

Python liest die Datei Zeile für Zeile, von oben nach unten. Daraus folgt
eine Regel ohne Ausnahme:

> Eine Variable muss **angelegt** sein, bevor eine andere Zeile sie benutzt.

```python
fruits = {"apple": 130}        # erst anlegen
item = input("Item: ")
if item in fruits:             # dann benutzen
    print(fruits[item])
```

> **Stolperstein.** Steht die Prüfung über dem Dictionary, bricht Python
> mit `NameError` ab und kommt nie bis zur Zeile, in der das Dictionary
> entsteht. Die Reihenfolge im Editor **ist** die Reihenfolge der
> Ausführung.

Der interaktive Modus verhält sich anders: dort gilt alles, was man schon
getippt hat. Zeilen, die man zum Ausprobieren ins `>>>` eingibt, gehören
deshalb **nicht** in die Datei — ohne `print` passiert dort nichts
Sichtbares.

---

## Variablen

```python
x = 1
name = "Yusuf"
```

**Ein Variablenname ist ein Etikett, das du frei wählst.** Er hat nichts
damit zu tun, was der Benutzer eintippt. Bei `name = input()` landet die
Eingabe zur Laufzeit im Behälter mit dem Etikett `name` — im Code steht
sie nirgends.

> **Stolperstein.** `HELLO, WORLD = input()` — das legt zwei Behälter
> namens HELLO und WORLD an und scheitert. Was der Benutzer tippt, darf
> im Code nicht vorkommen.

Namen werden **klein** geschrieben, mit Unterstrichen:
`first_name`, `meal_time`. Großbuchstaben am Anfang sind für Klassen
reserviert (Woche 8).

---

## Datentypen

| Typ | Bedeutung | Beispiel |
|---|---|---|
| `int` | ganze Zahl | `42` |
| `float` | Kommazahl | `3.14` |
| `str` | Text (string) | `"hallo"` |
| `list` | Liste | `["a", "b"]` |
| `dict` | Zuordnung | `{"a": 1}` |

```python
int("1")        # Text -> ganze Zahl
float("1.5")    # Text -> Kommazahl
str(42)         # Zahl -> Text
type("1")       # zeigt den Typ an: str
```

**Warum das zählt:** `1 + 2` ergibt `3`, aber `"1" + "2"` ergibt `"12"`.
Bei Zahlen addiert `+`, bei Texten hängt es aneinander.

`input()` liefert **immer Text**, auch wenn Ziffern eingetippt werden.
Deshalb gleich beim Einlesen umwandeln:

```python
x = int(input("Was ist x? "))      # erst fragen, dann umwandeln
```

> **Stolperstein.** `int("7:30")` bricht ab — der Doppelpunkt ist keine
> Ziffer. Solche Eingaben muss man erst zerlegen (siehe `split`).

`int()` und `float()` brechen mit `ValueError` ab, wenn der Text keine
Zahl ist. Das Abfangen kommt in Woche 3.

### Kommazahlen sind ungenau

```
>>> 0.1 + 0.2
0.30000000000000004
```

Kein Python-Problem: der Computer rechnet binär, und viele Dezimalzahlen
sind dort nicht exakt darstellbar — wie 1/3 im Zehnersystem.

Zwei Konsequenzen für die Praxis:

- Kommazahlen **nie** mit `==` vergleichen. Stattdessen prüfen, ob die
  Differenz klein genug ist.
- Für Geld keine floats. `Decimal` nehmen oder in Cent als ganze Zahlen
  rechnen — sonst fehlt am Jahresende ein Cent.

---

## Text bearbeiten

```python
name.strip()                # Leerzeichen NUR am Anfang und Ende weg
name.strip("$")             # dieses Zeichen am Anfang und Ende weg
name.lower()                # alles klein
name.upper()                # alles groß
name.title()                # Erster Buchstabe jedes Wortes groß
name.replace(" ", "...")    # jedes Vorkommen ersetzen
name.split(" ")             # zerlegt an Leerzeichen -> Liste
name.split(":")             # zerlegt an einem anderen Trennzeichen
name.startswith("hello")    # fängt der Text damit an?
name.endswith(".pdf")       # hört er damit auf?
```

```
>>> "   hallo welt   ".strip()
'hallo welt'
>>> "Yusuf Ogul".split(" ")
['Yusuf', 'Ogul']
>>> "7:30".split(":")
['7', '30']
```

`.strip()` zerlegt nichts, es räumt nur außen auf. Zerlegen ist `.split()`.

### len() — wie viele?

`len()` gibt die **Anzahl** zurück. Es steht vorne, mit dem Wert in
Klammern — es ist kein `.befehl` hinten dran.

| Aufruf | zählt | Ergebnis |
|---|---|---|
| `len("CS50")` | Zeichen | `4` |
| `len(["a", "b", "c"])` | Einträge der Liste | `3` |
| `len(fruits)` | Schlüssel im Dictionary | `20` |

Typisch in einer Bedingung, als verketteter Vergleich:

```python
if 2 <= len(plate) <= 6:
```

### Welche Zeichen stecken drin?

Fragen, die ein Zeichen oder einen ganzen Text prüfen. Alle geben `True`
oder `False` zurück:

```python
"N".isupper()        # Großbuchstabe?
"n".islower()        # Kleinbuchstabe?
"5".isdigit()        # Ziffer?
"abc".isalpha()      # nur Buchstaben?
"ab12".isalnum()     # nur Buchstaben und Ziffern, kein . , - Leerzeichen?
```

Bei mehreren Zeichen gilt die Frage für **alle**: `"CS50".isdigit()` ist
`False`, weil nicht jedes Zeichen eine Ziffer ist.

> **Stolperstein.** `text.isalpha().isdigit()` — solche Fragen lassen sich
> **nicht aneinanderhängen**. Die erste liefert `True` oder `False`, und ein
> `True` kann man nicht nochmal fragen, ob es eine Ziffer ist:
> `AttributeError: 'bool' object has no attribute 'isdigit'`.
> Zwei Fragen heißt zwei getrennte Prüfungen, verbunden mit `and`.

`isdigit()` ist strenger als `int()`: `"-5".isdigit()` ist `False`, weil das
Minus keine Ziffer ist — `int("-5")` funktioniert aber. Bei negativen Zahlen
geben die beiden also verschiedene Antworten. Welche man will, hängt von der
Sache ab, nicht von Python.

> **Stolperstein.** Bei **leerem** Text ist jede dieser Fragen `False` —
> `"".isdigit()`, `"".isalpha()`, alle. Es ist ja nichts da, was eine
> Ziffer sein könnte. Gefährlich wird das zusammen mit Slicing: bei
> `"CS"[2:]` kommt ein leeres Stück heraus, und `"CS"[2:].isdigit()` ist
> `False`, obwohl nichts verkehrt ist.

**Es gibt kein `isvowel()`.** "Großbuchstabe" und "Ziffer" sind
Eigenschaften, die im Zeichensatz stehen und die Python kennt. "Vokal"
ist eine menschliche Kategorie und hängt von der Sprache ab — die Liste
schreibt man selbst hin. Je weiter man kommt, desto öfter ist es so: beim
FM-Tool weiß Python auch nicht, welche Lagerguthöhe welche Schutzklasse
auslöst.

Verketten ist üblich, und die **Reihenfolge zählt**:

```python
name = input("Name? ").strip().title()
text.strip().replace(" ", "...")   # erst außen aufräumen, dann ersetzen
```

Andersherum wären die äußeren Leerzeichen schon zu Punkten geworden,
bevor `strip` sie wegnehmen könnte.

Faustregel: zwei bis drei Aufrufe verketten, darüber hinaus aufteilen.
Sonst kommt man beim Fehlersuchen an die Zwischenergebnisse nicht heran.

### Mehrere Werte auf einmal

```python
first_name, last_name = name.split(" ")
x, o, y = "1 + 1".split(" ")
```

Die Anzahl links muss zur Anzahl rechts passen, sonst `ValueError`.

**Das ist der Unterschied, der leicht übersehen wird:**

```python
teile = zeile.split(" ")             # klappt IMMER, egal wie viele Teile
artikel, menge = zeile.split(" ")    # verlangt GENAU zwei
```

```
"Rohr 40"        →  ["Rohr", "40"]              beide Formen gehen
"Rohr"           →  ["Rohr"]                    ValueError: not enough values
"Rohr 3 Stueck"  →  ["Rohr", "3", "Stueck"]     ValueError: too many values
```

Wer links zwei Namen hinschreibt, stellt damit eine **Bedingung**. Das ist
nützlich: man kann sie mit `try` abfangen, statt die Anzahl selbst zu
prüfen.

### Slicing — Zeichen herausschneiden

```
>>> "hello, newman"[:5]
'hello'
>>> "hello"[0]
'h'
>>> "hello"[1:3]
'el'
```

Die Zählung beginnt bei **0**, und die Zahl hinter dem Doppelpunkt ist die
Stelle, **bis zu der** geschnitten wird (ohne sie selbst).

`startswith` / `endswith` sind robuster: bei leerer Eingabe geben sie
`False` zurück, während `text[0]` mit `IndexError` abbricht.

---

## Ausgabe formatieren

> **Stolperstein.** `print` steht **nie** rechts vom `=`. `text =
> print(...)` heißt: *gib etwas aus und merk dir das Nichts danach* — in
> `text` landet `None`. `print` legt etwas auf den Bildschirm und gibt
> nichts zurück. Fragen, rechnen und ausgeben sind getrennte Zeilen.

```python
print("hallo")
print("a", "b")              # a b  — Komma fügt ein Leerzeichen ein
print("meow" * 3)            # meowmeowmeow
print("meow", end="")        # ohne Zeilenumbruch am Ende
```

> **Stolperstein.** `print("E: ", wert)` ergibt `E:  180` mit Doppellücke —
> das Komma fügt zusätzlich zum Leerzeichen im Text noch eines ein.

### f-Strings

```python
print(f"hallo, {name}")
```

Das `f` vor dem Anführungszeichen nicht vergessen, sonst steht wörtlich
`{name}` da.

Der Doppelpunkt trennt: links **was**, rechts **wie**:

| Angabe | Wirkung | `1234.5678` wird zu |
|---|---|---|
| `.1f` | eine Nachkommastelle | `1234.6` |
| `.2f` | zwei Nachkommastellen | `1234.57` |
| `,` | Tausendertrennzeichen | `1,234.5678` |
| `,.2f` | beides kombiniert | `1,234.57` |

Achtung: Python nimmt das englische Format (Komma = Tausender,
Punkt = Dezimal). `1,234.57` heißt bei uns `1.234,57`.

### Sonderzeichen

```python
"\n"                            # Zeilenumbruch
"🙂"                            # Emoji sind normale Zeichen
"\N{SLIGHTLY SMILING FACE}"     # dasselbe, ohne das Zeichen zu tippen
```

Windows-Taste + Punkt öffnet die Emoji-Auswahl.

---

## Bedingungen

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")
```

Was **eingerückt** unter `if` steht, läuft nur, wenn die Bedingung stimmt.
Einrücken mit der **Tab-Taste** (= 4 Leerzeichen, Python-Standard).

> **Stolperstein.** **Tabs und Leerzeichen nicht mischen.** Für dich sehen
> beide gleich aus, für Python nicht. Eine Datei, in der ein Teil der Zeilen
> mit Tab und ein Teil mit Leerzeichen eingerückt ist, bricht ab:
>
> `IndentationError: unindent does not match any outer indentation level`
>
> In VS Code für die ganze Datei reparieren: unten rechts in der Statusleiste
> auf `Spaces: 4` bzw. `Tab Size: 4` klicken, dann
> **„Convert Indentation to Spaces"**.

**Die Reihenfolge macht die Arbeit.** Kommt Python beim `elif` an, ist der
erste Zweig ja schon fehlgeschlagen — die Obergrenze braucht man dann nicht
mehr zu prüfen. Deshalb: das Speziellste zuerst, das Allgemeinste zuletzt.

```python
if greeting.startswith("hello"):   # muss zuerst stehen
    print("$0")
elif greeting.startswith("h"):     # sonst fängt dieser Zweig alles ab
    print("$20")
```

> **Stolperstein.** `else x == y:` ist ein Syntaxfehler. `else` nimmt
> **keine** Bedingung — das ist sein Sinn: "in allen anderen Fällen".
> Braucht man eine Bedingung, heißt es `elif`.

### Eine Weiche mit gemeinsamem Schluss

Wenn zwei verschiedene Eingabeformen zum selben Ergebnis führen sollen,
teilt man nur den Anfang auf:

```python
date = input("Date: ").strip()          # erst speichern

if "/" in date:                         # 9/8/1636
    month, day, year = date.split("/")
else:                                   # September 8, 1636
    monthday, year = date.split(", ")
    month, day = monthday.split(" ")
    month = months.index(month) + 1

month = int(month)                      # ab hier wieder gemeinsam
day = int(day)
year = int(year)
```

Beide Zweige füllen **dieselben Namen**. Alles danach — umwandeln, prüfen,
ausgeben — steht deshalb nur **einmal** da, nicht zweimal.

Damit das geht, muss die Eingabe vorher in eine Variable: man braucht sie
**zweimal**, einmal für die Frage `"/" in date` und einmal zum Zerlegen.

> **Stolperstein.** `input(date)` fragt **noch einmal**. Was in den
> Klammern von `input()` steht, ist nur die **Beschriftung**, die vor der
> Eingabe angezeigt wird — niemals die Quelle. Liegt der Text schon in
> `date`, arbeitet man direkt daran: `date.split("/")`.

### Vergleichen

```python
==   gleich          !=   ungleich
<    kleiner         <=   kleiner oder gleich
>    größer          >=   größer oder gleich
```

`=` legt einen Wert ab, `==` vergleicht. Zwei verschiedene Dinge.

### Verkettete Vergleiche

```python
if 7 <= time <= 8:         # richtig: Variable in der Mitte
```

Python liest `a <= b <= c` als `a <= b and b <= c`.

> **Stolperstein.** `score <= 90 <= 100` heißt `score <= 90 and 90 <= 100`.
> Der zweite Teil ist immer wahr, übrig bleibt `score <= 90` — und schon
> bekommt eine 88 die Note A. Die Variable gehört in die **Mitte**,
> Unter- und Obergrenze außen.

> **Stolperstein.** `1 < month > 12` sieht aus wie "zwischen 1 und 12",
> heißt aber `1 < month and month > 12` — *größer als 1 **und** größer als
> 12*. Wahr erst ab 13; die `0` kommt ungeprüft durch. Beim Verketten
> zeigen **beide** Zeichen in dieselbe Richtung: `1 <= month <= 12`.

Soll die Bedingung zuschlagen, wenn der Wert **nicht** im Bereich liegt,
schreibt man die gute Aussage hin und dreht sie mit `not` um:

```python
if not 1 <= month <= 12 or not 1 <= day <= 31:
    continue
```

Das liest sich wie der deutsche Satz: *wenn der Monat nicht zwischen 1 und
12 liegt, oder der Tag nicht zwischen 1 und 31.* Ausgeschrieben
(`month < 1 or month > 12 or day < 1 or day > 31`) ist es dasselbe, nur
doppelt so lang und doppelt so leicht falsch zu tippen.

### and, or, not

```python
if x > 0 and y > 0:
if name == "Harry" or name == "Ron":
if not done:
```

> **Stolperstein.** `x == "42" or "forty-two"` ist falsch. Jeder Vergleich
> braucht `x ==` davor — auch wenn man es im Kopf anders formuliert.

### match-case

```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

`case _:` ist das Gegenstück zu `else`. Das `|` heißt hier "oder", gilt
aber nur innerhalb von `case` — außerhalb schreibt man `or`.

---

## Rechnen

```python
+    -    *    /        # die üblichen
**   Potenz             # 2 ** 3 = 8
//   ganzzahlige Division
%    Rest (Modulo)
```

```
>>> 17 // 5     # wie oft passt 5 rein
3
>>> 17 % 5      # was bleibt übrig
2
```

`//` und `%` gehören zusammen: das eine gibt den ganzen Teil, das andere
den Rest.

**Wofür man Modulo braucht:**

```python
x % 2 == 0           # gerade (even), sonst ungerade (odd)
jahr % 4 == 0        # durch 4 teilbar (Schaltjahr, erster Schritt)
200 // 60, 200 % 60  # 3 Stunden und 20 Minuten
i % 3                # 0,1,2,0,1,2,... — reihum verteilen
```

Kurzformen beim Zuweisen:

```python
i += 1      # dasselbe wie i = i + 1
i -= 1      i *= 2      i /= 2
```

---

## Schleifen

### while — wiederholen, solange etwas gilt

```python
i = 0
while i < 3:
    print("meow")
    i += 1
```

Drei Teile, und alle drei braucht es:

1. **Startwert** vor der Schleife
2. **Bedingung** im `while`
3. etwas im Rumpf, das die Bedingung irgendwann falsch macht

> **Stolperstein.** Fehlt das `i += 1`, läuft die Schleife ewig.
> Abbrechen mit **Strg + C**.

### for — für jedes Element aus einer Sammlung

```python
for i in [0, 1, 2]:
    print("meow")
```

Kein Zähler nötig, kein Hochzählen, kein Endlosschleifen-Risiko.
Deshalb nimmt man `for`, wann immer die Anzahl vorher feststeht.

### range — Zahlen erzeugen

```python
for i in range(3):        # 0, 1, 2
    print("meow")
```

`range(3)` zählt **ab 0** und hört **vor** der 3 auf — also drei Durchläufe.
Dieselbe Logik wie beim Slicing.

```python
range(3)          # 0, 1, 2
range(1, 4)       # 1, 2, 3
range(0, 10, 2)   # 0, 2, 4, 6, 8
```

Wird die Zählvariable nicht gebraucht, schreibt man einen Unterstrich —
das Zeichen für "interessiert mich nicht":

```python
for _ in range(3):
    print("meow")
```

### Verschachtelte Schleifen

```python
for i in range(3):
    for j in range(3):
        print("#", end="")
    print()
```

Die innere Schleife läuft **komplett durch**, bevor die äußere einen
Schritt weitergeht. Ergebnis: drei Zeilen mit je drei `#`.

Das leere `print()` am Ende der äußeren Schleife macht den Zeilenumbruch,
den `end=""` innen unterdrückt hat.

### break und continue

```python
while True:
    n = int(input("n: "))
    if n > 0:
        break           # Schleife sofort verlassen
```

`break` bricht ab, `continue` springt zum nächsten Durchlauf.
`while True:` läuft endlos — nur sinnvoll **mit** einem `break` darin.

Das ist das Muster, um auf eine gültige Eingabe zu warten.

**`break` und `return` machen verschieden große Sprünge:**

| | verlässt |
|---|---|
| `break` | nur die Schleife — der Code darunter läuft weiter |
| `return` | die ganze Funktion — alles danach fällt weg |

> **Stolperstein.** `break` außerhalb einer Schleife ist ein `SyntaxError`.
> Es heißt "spring aus der Schleife" — ohne Schleife gibt es nichts, wo man
> herausspringen könnte.

### Sich etwas merken beim Durchlaufen

Manche Prüfungen lassen sich **nicht** an einem einzelnen Element
entscheiden. Beispiel: in `CS50P` ist am `P` nichts falsch — falsch ist,
dass **vorher schon Ziffern kamen**.

Dafür legt man eine Variable **vor** der Schleife an, die den Zustand
festhält:

```python
zahl_gekommen = False
for zeichen in plate:
    if zeichen.isdigit():
        zahl_gekommen = True
    elif zahl_gekommen:
        return False
```

Zwei Dinge sind entscheidend:

**Die Variable muss vor die Schleife.** Innerhalb würde sie bei jedem
Durchlauf neu angelegt — dann merkt sie sich nichts.

**`elif`, nicht `else`.** `else` nimmt keine Bedingung und würde bei jedem
Zeichen zuschlagen, das keine Ziffer ist — also auch bei den Buchstaben
*vor* der ersten Ziffer. Verboten sind Buchstaben aber nur **danach**, und
genau diese Einschränkung trägt das `elif`.

Dasselbe Muster braucht man für "war schon mal", "gab es bisher",
"alles bisher in Ordnung". Es ist der Schritt von *jedes Element einzeln
beurteilen* zu *den Verlauf beurteilen*.

---

## Listen

```python
students = ["Hermione", "Harry", "Ron"]

students[0]              # "Hermione" — Zählung beginnt bei 0
students[-1]             # "Ron" — von hinten
len(students)            # 3
students.append("Draco") # hinten anhängen
```

Durchlaufen geht direkt, ohne Index:

```python
for student in students:
    print(student)
```

Das ist der übliche Weg. Den Index braucht man nur, wenn man ihn
wirklich benutzt — dann:

```python
for i in range(len(students)):
    print(i + 1, students[i])
```

### in und not in

Prüfen, ob etwas drin ist:

```python
if "Harry" in students:
    print("gefunden")

if "Voldemort" not in students:
    print("nicht dabei")
```

`not in` ist das Gegenteil von `in`. Es spart oft ein `else`:

```python
for zeichen in wort:                      # so
    if zeichen not in "aeiouAEIOU":
        ergebnis += zeichen

for zeichen in wort:                      # nicht so
    if zeichen in "aeiouAEIOU":
        ergebnis += ""                    # tut nichts
    else:
        ergebnis += zeichen
```

**Achtung — `in` bedeutet bei Text etwas anderes als bei einer Liste:**

```python
zeichen in ["a", "e", "i"]     # Liste: ist es EINER DIESER Einträge?
zeichen in "aei"               # Text:  kommt es IRGENDWO darin vor?
```

Bei einzelnen Buchstaben läuft beides aufs Gleiche hinaus, und die
Textvariante ist kürzer. Das gilt aber nur, weil jedes "Element" genau
ein Zeichen lang ist.

> **Stolperstein.** `zeichen in "a,e,i,o,u"` — die Kommas sind Teil des
> Textes und zählen mit. Ein Komma in der Eingabe wird dann als Vokal
> behandelt und verschwindet: `Hello, World` wurde zu `Hll Wrld` statt
> `Hll, Wrld`. Entweder echte Liste mit eckigen Klammern, oder Text
> **ohne** Trennzeichen: `"aeiouAEIOU"`.

### .index() — an welcher Stelle steht es?

`in` fragt **ob** etwas drin ist, `.index()` fragt **wo**:

```python
months = ["January", "February", "March", ... , "December"]

months.index("January")      # 0
months.index("September")    # 8
```

Die Position zählt ab 0, Monate ab 1 — deshalb `+ 1`:

```python
month = months.index(month) + 1
```

Damit ist die Liste selbst die Umrechnungstabelle. Die **Reihenfolge** ist
die Information; ein Dictionary mit zwölf Einträgen wäre doppelte Arbeit.

**Nützlich:** `.index()` wirft einen `ValueError`, wenn der Wert nicht in
der Liste steht. Innerhalb eines `try` muss man unbekannte Werte dann
nicht selbst abfangen — `"Jan"` fliegt von allein raus.

> **Stolperstein.** `months.index("month")` sucht nach dem **Wort**
> `month`. Anführungszeichen machen aus einem Variablennamen Text.
> Gesucht werden soll der *Inhalt*, also ohne Anführungszeichen:
> `months.index(month)`.

---

### Liste oder Dictionary?

| | wofür |
|---|---|
| `[]` Liste | **sammeln** — Dinge in Reihenfolge, Dubletten erlaubt |
| `{}` Dictionary | **zählen oder nachschlagen** — ein Name zeigt auf einen Wert |

Die Frage ist nicht, was schöner ist, sondern: *brauche ich zu jedem Ding
noch einen zweiten Wert?*

```python
zaehler = {}        # grocery: Name -> Anzahl. Zählen.
persons = []        # adieu: nur die Namen, in Reihenfolge. Sammeln.
```

`.append()` gibt es **nur** bei Listen. Und Funktionen, die eine Aufzählung
erwarten — etwa `join` aus `inflect` — wollen eine Liste.

---

## Dictionaries

Eine Liste hat Positionen, ein Dictionary hat **Namen**:

```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Draco": "Slytherin",
}

students["Hermione"]     # "Gryffindor"
students["Luna"] = "Ravenclaw"     # neu dazu
```

Links der **Schlüssel** (key), rechts der **Wert** (value).
Nachschlagen geht über den Schlüssel, nicht über eine Nummer.

Durchlaufen:

```python
for name in students:                  # nur die Schlüssel
    print(name, students[name])

for name, house in students.items():   # beides auf einmal
    print(name, house)
```

Wann was: **Liste**, wenn die Reihenfolge zählt und alles gleichartig ist.
**Dictionary**, wenn du etwas unter einem Namen nachschlagen willst.

### Erst prüfen, dann nachschlagen

Ein Schlüssel, den es nicht gibt, bricht das Programm ab:

```python
students["Luna"]         # KeyError, wenn Luna nicht drin ist
```

Deshalb vorher fragen. `in` schaut bei einem Dictionary auf die
**Schlüssel**:

```python
if "Luna" in students:
    print(students["Luna"])
```

Alternative: `.get()` bricht nicht ab, sondern gibt `None` zurück.

```python
students.get("Luna")             # None statt KeyError
students.get("Luna", "unbekannt")   # oder ein Ersatzwert
```

Wann was: `if ... in`, wenn bei fehlendem Schlüssel **nichts** passieren
soll. `.get()` mit Ersatzwert, wenn du trotzdem etwas ausgeben willst.

### Groß- und Kleinschreibung

Wenn die Eingabe mit `.lower()` kleingemacht wird, müssen **alle
Schlüssel klein geschrieben sein**. Sonst können sie sich nie treffen.

```python
fruits = {"sweet cherries": 100}
item = input("Item: ").strip().lower()
```

> **Stolperstein.** `{"Sweet Cherries": 100}` mit `.lower()` auf der
> Eingabe wird **in keiner Schreibweise** gefunden — nicht als
> `Sweet Cherries`, nicht als `sweet cherries`. Der Eintrag steht im
> Dictionary, aber niemand kommt je an ihn heran. Totes Material.

### Daten gehören ins Dictionary, nicht in den Code

Zwanzig Früchte mit Kalorien — zwei Wege:

```python
if item == "apple":              # 20 Zweige, Zahlen im Code verstreut
    print("Calories: 130")
elif item == "banana":
    print("Calories: 110")
...
```

```python
fruits = {"apple": 130, "banana": 110, ...}    # 20 Datenzeilen
if item in fruits:                             # 2 Zeilen Logik, fertig
    print(f"Calories: {fruits[item]}")
```

Der Gewinn: ändert sich eine Zahl, änderst du eine Datenzeile. Beim
`elif`-Weg suchst du im Code. Und die Logik bleibt gleich lang, ob es
zwei Früchte sind oder zweihundert.

> **Stolperstein.** Nicht die Form aus dem Video übernehmen, ohne zu
> prüfen, ob sie passt. Eine **Liste von Dictionaries**
> (`[{"Item": "apple", "calories": 130}, ...]`) braucht man für mehrere
> Datensätze mit mehreren Feldern. Zum Nachschlagen eines einzelnen
> Werts reicht **ein** Dictionary — und spart die Schleife komplett.

> **Stolperstein.** Den Fehlerfall nicht in die Daten schreiben.
> `{"chocolate": ""}` für "ist keine Frucht" geht nicht auf: es gibt
> unendlich viele Dinge, die keine Frucht sind. Ins Dictionary kommt nur,
> was es wirklich gibt — alles andere erkennt man daran, dass es **nicht
> drin** ist.

---

## Funktionen

```python
def main():
    text = input()
    print(convert(text))


def convert(text):
    return text.replace(":)", "🙂")


main()
```

**Wie das läuft:** `main()` ganz unten startet das Programm — ohne
Einrückung, es gehört zu keiner Funktion. In `main` wird gefragt, das
Ergebnis landet in `text`. Dann wird `convert(text)` aufgerufen: der
Inhalt wandert in die Funktion. `convert` gibt mit `return` ein Ergebnis
zurück — dieses Ergebnis steht dann dort, wo `convert(text)` stand, und
`print` gibt es aus.

**`return` liefert zurück, `print` gibt aus.** Das ist der Kern: eine
Funktion rechnet und reicht das Ergebnis weiter; ausgegeben wird an einer
Stelle.

Regeln:

- `def name(...):` — Doppelpunkt am Ende nicht vergessen
- Unter jedem `def` muss mindestens eine eingerückte Zeile stehen.
  Eine leere Funktion ist ein Syntaxfehler.
- `def` legt die Funktion nur an. Ausgeführt wird sie erst beim Aufruf.
- `main()` muss **hinter** allen `def` stehen, die darin benutzt werden —
  sonst `NameError`, weil Python die Funktion noch nicht kennt. Deshalb ist
  der Aufruf die **letzte Zeile der Datei**.
- `return n * n`, nicht `return(n * n)` — `return` ist kein Befehl mit
  Klammern.

> **Stolperstein.** `def main():` definieren und `main()` am Ende
> vergessen — dann passiert gar nichts. Das Rezept steht im Buch,
> gekocht wird es nie.

> **Stolperstein.** Was **unter** einem `return` steht, läuft nie.
> `return` ist das Ende der Funktion, nicht nur eine Zeile darin.

### Funktionen, die eine Frage beantworten

Eine Funktion muss nicht rechnen — sie kann auch nur `True` oder `False`
zurückgeben. Das ist das Mittel, um viele Prüfungen übersichtlich zu
halten:

```python
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False

    if not plate[:2].isalpha():
        return False

    return True
```

**Jede Regel bekommt ihren eigenen Block**, und bei Verstoß steigt
`return False` sofort aus — die restlichen Regeln werden gar nicht mehr
geprüft. Das `return True` ganz unten wird nur erreicht, wenn keine Regel
zugeschlagen hat.

Drei Gründe, warum das besser ist als eine lange Zeile mit `or`:

- Mit sechs Regeln ist eine `or`-Kette nicht mehr lesbar
- Eine siebte Regel kommt dazu, ohne dass man die anderen anfasst
- Die Ausgabe steht **einmal** im Code, in `main` — egal welche Regel
  verletzt ist

Weil die Funktion `True`/`False` liefert, passt sie direkt in ein `if`:
`if is_valid(plate):` — ohne `== True`. Namen mit `is_` davor sind die
übliche Form dafür.

### Scope — wo eine Variable existiert

Was in einer Funktion angelegt wird, lebt nur dort:

```python
def main():
    x = 5
    hello()

def hello():
    print(x)      # NameError: name 'x' is not defined
```

`x` gehört zu `main`, `hello` sieht es nicht. Wenn `hello` den Wert
braucht, muss er übergeben werden — `hello(x)`, und innen heißt er dann
so, wie es in `def hello(n):` steht. Der Name draußen und der Name drinnen
haben nichts miteinander zu tun.

### Shadowing — gleicher Name innen und außen

```python
n = 5

def square(n):
    return n * n

print(square(3))      # 9, nicht 25
```

Der Parameter gewinnt. Das äußere `n` bleibt unberührt.

Es bricht also nichts — aber der Leser muss erst prüfen, welches `n`
gemeint ist. Deshalb: Parameter bekommen neutrale Namen (`n`, `text`,
`wert`), die sprechenden Namen (`c`, `m`) stehen draußen.

**Bei eingebauten Namen bricht es sehr wohl etwas.** `input`, `print`,
`str`, `int`, `list`, `len`, `sum`, `max` gehören Python. Wer sie als
Variablennamen benutzt, zerstört das Werkzeug:

```python
input = input("Item: ")        # ab hier ist input kein Werkzeug mehr,
                               # sondern Text
zweite = input("Noch eine? ")  # TypeError: 'str' object is not callable
```

> **Stolperstein.** Beim ersten Aufruf fällt es nicht auf — die Zeile
> läuft noch. Erst der zweite Aufruf scheitert, und die Fehlermeldung
> zeigt auf die *zweite* Zeile, obwohl der Fehler in der ersten steht.
> `item`, `frucht`, `eingabe` — alles gut. `input` nicht.

Dasselbe gilt für **deine eigenen** Namen:

> **Stolperstein.** `for is_valid in plate:` — die Laufvariable heißt wie
> die Funktion, in der sie steht. Ab da ist `is_valid` ein einzelner
> Buchstabe. Laufvariablen heißen `zeichen`, `i`, `n` — nie wie etwas,
> das es schon gibt.

---

## Nachschlagen statt auswendig lernen

Niemand hat die Befehle im Kopf. Was man im Kopf hat, ist:
*"Ich brauche jetzt sowas wie Ersetzen — das muss es geben."*
Den Rest liest man nach.

**In VS Code:** Tipp `text.` — es klappt eine Liste aller Befehle auf,
die es für Text gibt, mit kurzer Erklärung.

**Im interaktiven Modus:**

```
python                  startet ihn, Eingabezeile wird zu >>>
dir("")                 listet alles auf, was man mit Text machen kann
dir([])                 dasselbe für Listen
help("".replace)        erklärt einen einzelnen Befehl (raus mit q)
exit()                  beendet ihn
```

**Ausprobieren statt raten:**

```
>>> "a b c".replace(" ", "...")
'a...b...c'
```

Das Denkmuster: *Was habe ich* (Text? Zahl? Liste?) und *was will ich
haben*. Der Typ bestimmt, welche Befehle überhaupt zur Verfügung stehen.

---

## Fehler lesen

Der **Traceback** ist das wichtigste Werkzeug. Von unten nach oben lesen:
unten steht, *was* falsch ist, darüber, *wo* (Datei und Zeilennummer),
und `^^^^^` markiert die Stelle.

| Meldung | Ursache |
|---|---|
| `SyntaxError: unterminated string literal` | Anführungszeichen nicht geschlossen |
| `SyntaxError: invalid syntax` | oft ein fehlender Doppelpunkt oder eine Klammer |
| `IndentationError` | Einrückung fehlt oder ist uneinheitlich |
| `NameError: name 'x' is not defined` | Variable existiert nicht, oder falscher Scope |
| `TypeError` | falscher Typ, z. B. Text mit Zahl addiert |
| `ValueError: invalid literal for int()` | `int("hallo")` — keine Zahl im Text |
| `ValueError: not enough values to unpack` | links mehr Variablen als rechts Werte |
| `IndexError: list index out of range` | Position gibt es nicht (zählt ab 0!) |
| `KeyError` | Schlüssel im Dictionary gibt es nicht |
| `AttributeError: 'bool' object has no attribute` | zwei Fragen aneinandergehängt, z. B. `.isalpha().isdigit()` |
| `can't open file ... No such file or directory` | falscher Ordner im Terminal, oder nicht gespeichert |

VS Code färbt zusammengehörige Klammern gleich ein. Wirkt eine Klammer
einsam, fehlt das Gegenstück.

---

## Fehler abfangen (Woche 3)

Fehler lesen ist das eine. Dafür sorgen, dass sie das Programm nicht
umwerfen, das andere.

**Die Denkweise:** nicht jeden Sonderfall vorher abfragen, sondern es
versuchen und den Absturz auffangen. *Lieber um Verzeihung bitten als
vorher um Erlaubnis fragen.*

Der Grund: Sonderfälle vorher aufzuzählen wird nie fertig. Bei `5 bar`
fehlt mal das Leerzeichen, mal steht ein Komma statt eines Punktes, mal
`BAR` groß. Es gibt immer einen Fall mehr.

```python
try:
    x = int(input("x: "))      # das hier kann schiefgehen
except ValueError:
    print("keine Zahl")        # falls genau dieser Fehler kommt
else:
    print(f"x ist {x}")        # nur wenn nichts schiefging
```

| Block | Bedeutung |
|---|---|
| `try:` | Versuch das. Es **kann** scheitern. |
| `except ValueError:` | Falls **dieser** Fehler kommt, mach stattdessen das. |
| `else:` | Es ist **nicht** gescheitert — mach weiter. |

**In `try` gehört so wenig wie möglich** — nur die Zeile, die wirklich
scheitern kann. Alles andere ins `else`. Sonst fängt das `except` später
Fehler mit, die aus ganz anderen Gründen entstehen, und man sucht an der
falschen Stelle.

> **Stolperstein.** Scheitert `int()`, wurde `x` nie angelegt. Wer danach
> trotzdem darauf zugreift, bekommt `NameError` — ein Fehler ersetzt den
> anderen. Genau dafür gibt es `else`.

### So lange fragen, bis es passt

Das ist der eigentliche Gewinn: `try` in eine Schleife packen.

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
```

`pass` heißt "tu nichts" — hier sinnvoll, weil die Schleife von selbst
nochmal fragt. Der Benutzer sieht ja, dass die Frage wiederkommt.

`return` beendet die Funktion **und** die Schleife, sobald die Umwandlung
geklappt hat. Danach ist der Aufruf wieder eine Zeile — nur eine, die nicht
mehr abstürzen kann.

**Mit fachlicher Prüfung.** Oft genügt die Umwandlung nicht — die Zahl muss
auch in einen Bereich passen:

```python
def get_positive(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass
```

Zwei Hürden hintereinander: `int()` wirft bei `cat` einen `ValueError`, und
`-1` kommt sauber durch die Umwandlung und scheitert erst am `if`.

Was bei einer schlechten Eingabe passieren soll, muss man **nicht**
hinschreiben: wird `return` nicht erreicht, dreht die Schleife von selbst
noch eine Runde. Kein `else`, kein `continue`.

Der Gewinn ist, dass dieselbe Funktion an mehreren Stellen taugt — die
Beschriftung kommt als Parameter herein:

```python
level = get_positive("Level: ")
guess = get_positive("Guess: ")
```

> **Prüfen, wo der Wert hereinkommt** — nicht dort, wo er später Schaden
> anrichtet. Bei `game.py` stürzte ein `Level: -1` **nicht** am `int()` ab,
> sondern zwei Zeilen später bei `random.randint(1, -1)`:
> `ValueError: empty range in randrange(1, 0)`. Die Fehlermeldung zeigte
> auf eine Zeile, die nichts dafür konnte. Mit der Prüfung an der Tür kommt
> der schlechte Wert gar nicht erst ins Programm.

### Ein `except` fängt mehrere Fälle

Verschiedene Stellen können denselben Fehler werfen:

```python
artikel, menge = zeile.split(" ")   # ValueError, wenn nicht genau zwei Teile
int(menge)                          # ValueError, wenn keine Zahl
```

Beides ist `ValueError`, also genügt ein `except ValueError`. Man muss die
Fälle nicht auseinanderhalten, wenn die Reaktion dieselbe ist.

**Der Vorteil gegenüber selbst geschriebenen Prüfungen:** `try` prüft mit
**genau den Operationen**, die danach ohnehin ausgeführt werden. Eine
nachgebaute `if`-Prüfung kann auseinanderlaufen, wenn man den eigentlichen
Code später ändert. Die `try`-Fassung kann das nicht.

---

## Bibliotheken benutzen (Woche 4)

Bis Woche 3 war jedes Programm vollständig selbst geschrieben. Ab hier
benutzt du fremden Code — das ist der Übergang vom Selbermachen zum
Zusammensetzen.

```python
import random

random.choice(["heads", "tails"])   # ein Element zufällig herausziehen
random.randint(1, 10)               # ganze Zahl von 1 bis 10, beide dabei
random.shuffle(cards)               # mischt die Liste AN IHREM PLATZ
```

`import random` holt die Bibliothek, der Punkt verbindet sie mit dem
Werkzeug darin. Nach diesem Muster funktioniert jede Bibliothek.

> **Stolperstein.** `random.shuffle(cards)` gibt **nichts** zurück — es
> verändert die Liste direkt. `cards = random.shuffle(cards)` macht aus
> `cards` ein `None`.

> **Stolperstein.** `for card in cards: print(cards)` gibt dreimal die
> **ganze Liste** aus. Gemeint war `print(card)`, das einzelne Element.
> Einzahl und Mehrzahl unterscheiden sich um einen Buchstaben und sind
> genau deshalb leicht zu verwechseln.

### Zwei Schreibweisen für import

| | danach schreibt man |
|---|---|
| `import random` | `random.choice(...)` |
| `from random import choice` | `choice(...)` |

Beides ist richtig. `import random` ist die bessere Gewohnheit: man sieht an
jeder Stelle, woher etwas kommt. Bei `choice(...)` allein weiß man das nach
drei Wochen nicht mehr.

> **Stolperstein.** Eine eigene Datei **nie** wie eine Bibliothek benennen.
> Heißt deine Datei `random.py`, importiert Python ab dann *deine* Datei
> statt der Bibliothek. Dieselbe Falle wie `input = input(...)`, nur eine
> Etage höher.

### Fremde Bibliotheken nachladen — pip

```powershell
pip install cowsay
```

`pip` holt sie aus dem Internet. Die mitgelieferten — `random`,
`statistics`, `sys`, `json` — brauchen das nicht, die sind schon da.

### statistics

```python
import statistics

statistics.mean([100, 90])     # 95.0
```

Mittelwerte kommen als Kommazahl zurück, auch wenn es glatt aufgeht.

### sys.argv — Argumente beim Programmstart

```
python name.py Yusuf
       ^^^^^^^ ^^^^^
       argv[0] argv[1]
```

`sys.argv` ist eine **Liste** mit dem, was im Terminal stand. Position 0 ist
immer die Datei selbst.

| Befehl | `sys.argv` |
|---|---|
| `python name.py` | `["name.py"]` |
| `python name.py Yusuf` | `["name.py", "Yusuf"]` |
| `python name.py a b` | `["name.py", "a", "b"]` |

Der Sinn: das Programm **fragt nicht mehr nach**, es bekommt alles beim
Start mitgeliefert. `git commit -m "..."` ist genau dasselbe Prinzip.

> **Stolperstein.** `python name.py` ohne Argument und dann `sys.argv[1]`
> gibt `IndexError: list index out of range`. Die Liste hat nur Position 0.

```python
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
```

`sys.exit("...")` gibt die Meldung aus **und** beendet. Ein `print` allein
läuft weiter — bei einem größeren Programm dann mit fehlenden Daten.

Bei `argv` ist das `if` üblicher als `try`, weil man die Länge einer Liste
ohne Risiko abfragen kann. `try/except IndexError` wäre auch richtig.

**Alle Argumente durchlaufen**, nicht nur das erste:

```python
for arg in sys.argv[1:]:
    print(arg)
```

`[1:]` ist ein Ausschnitt ab Position 1 — alles außer dem Dateinamen.

### Dienste im Netz fragen — requests und JSON

```python
import json
import requests

response = requests.get("https://itunes.apple.com/search?term=weezer")
daten = response.json()
```

`requests.get(adresse)` tut genau das, was dein Browser tut: Adresse hin,
Antwort zurück. Es wird **nichts heruntergeladen** und es gibt keine Datei —
die Antwort ist einfach Text.

Zwei Richtungen, und das ist der verwirrende Teil:

```
Antwort-Text  --.json()-->  Python  --json.dumps()-->  lesbarer Text
```

| | |
|---|---|
| `response.json()` | Text → Python-Dictionaries und -Listen |
| `json.dumps(x, indent=2)` | Python → eingerückter Text zum Anschauen |

`indent=2` ist nur die Anzahl Leerzeichen pro Ebene, reine Lesbarkeit.

Der Umweg über Python lohnt sich, weil man dort **einzelne Werte**
herausholen kann statt der ganzen Antwort:

```python
o = response.json()
for result in o["results"]:      # ["results"] ist eine LISTE
    print(result["trackName"])   # darin stecken Dictionaries
```

Erst mit `json.dumps(..., indent=2)` anschauen, **dann** den Weg zum
gewünschten Wert heraussuchen. Blind raten geht schief.

### Eigene Module

Jede `.py`-Datei ist ein Modul und kann importiert werden:

```python
# say.py
from sayings import hello

hello("Yusuf")
```

### if \_\_name\_\_ == "\_\_main\_\_"

`import` heißt **nicht** "schau rein" — Python führt die ganze Datei aus,
von oben nach unten. Steht unten `main()`, läuft das Programm also auch beim
Importieren mit.

Python legt in jeder Datei automatisch `__name__` an:

| gestartet mit | `__name__` in `sayings.py` |
|---|---|
| `python sayings.py` | `"__main__"` |
| `import sayings` | `"sayings"` |

Deshalb:

```python
if __name__ == "__main__":
    main()
```

Wörtlich: *nur starten, wenn **diese** Datei gestartet wurde — nicht, wenn
jemand sie importiert.* Keine Zauberei, nur ein `if` auf eine Variable, die
Python für dich füllt.

Die zwei Unterstriche auf jeder Seite sind Absicht: so heißt bei Python
alles, was die Sprache selbst verwaltet und was man nicht aus Versehen
überschreiben soll.

**Die Regel:** sobald eine Datei auch nur *vielleicht* importiert wird,
gehört die Startzeile in dieses `if`.

### Ein Ding erzeugen und behalten

Manche Bibliotheken geben dir kein einzelnes Werkzeug, sondern ein **Ding**,
das sich etwas merkt:

```python
from pyfiglet import Figlet

figlet = Figlet()                   # Klammern: hier entsteht das Ding
figlet.setFont(font="slant")        # es merkt sich die Schriftart
print(figlet.renderText("CS50"))    # und benutzt sie
```

```python
import inflect

p = inflect.engine()                # dasselbe Muster
p.join(["Liesl", "Friedrich"])      # -> "Liesl and Friedrich"
```

Der Punkt bedeutet hier etwas anderes als bisher:

| | heißt |
|---|---|
| `random.choice(...)` | **Bibliothek**.Werkzeug |
| `figlet.renderText(...)` | **mein Ding**.seine Fähigkeit |

> **Stolperstein.** `Figlet().renderText("CS50")` erzeugt das Ding und
> benutzt es im selben Atemzug — dazwischen gab es keine Gelegenheit, die
> Schriftart einzustellen. Und das nächste `Figlet()` wäre ein neues Ding,
> das nichts davon weiß. Passieren mit einem Ding **zwei** Dinge
> nacheinander, muss es in eine Variable.

Mehr dazu in Woche 8 (Objekte). Fürs Erste reicht: erzeugen, in eine
Variable legen, dann einstellen und benutzen.

---

## Stil

**Variablen nach dem Inhalt benennen, Funktionen nach der Tätigkeit.**
`betrag` ist ein Ding, `dollars_to_float` tut etwas. `replace_dollar` als
Variablenname verwirrt, weil er nach einer Funktion klingt.

**Zwischenvariablen nur, wenn sie etwas bringen.** Bei einem einzigen
Schritt sind sie Ballast:

```python
return float(d.replace("$", ""))          # so
amount = d.replace("$", "")               # nicht so
return float(amount)
```

Sie lohnen sich, sobald mehrere Schritte nacheinander kommen oder der Name
erklärt, *warum* etwas passiert.

**Toter Code raus.** Berechnet-aber-nie-benutzt, auskommentierte Reste,
Variablen die sofort überschrieben werden — alles weg, solange es frisch
ist. Später fragt man sich: war das Absicht?

**Kurz ist kein Wert an sich.** Alles in eine Zeile zu packen funktioniert,
macht aber das Fehlersuchen schwer: der Traceback sagt nur "Zeile 12",
welcher der vier Schritte schuld war, musst du raten.

**Kommentare erklären das Warum, nicht das Was.** `# addiere 1` ist
überflüssig, `# Reihenfolge wichtig: erst strippen, dann ersetzen` nicht.

**"Tu nichts" nicht hinschreiben.** Wenn in einem Fall nichts passieren
soll, lässt man den Zweig weg — ohne `else` macht Python von sich aus
nichts.

```python
ergebnis += ""        # hängt nichts an
else: None            # tut nichts
```

Beides sind Zeilen, die aussehen wie Code, aber keiner sind. Tauchen sie
auf, steht meistens die Bedingung verkehrt herum: mit `not in` statt `in`
verschwindet der leere Zweig von selbst.

---

## Terminal (PowerShell)

```
pwd                      wo bin ich gerade?
cd ordnername            in einen Ordner wechseln
cd ..                    eine Ebene hoch (Leerzeichen, zwei Punkte!)
mkdir name               Ordner anlegen
python datei.py          Programm ausführen
code datei.py            Datei in VS Code öffnen
Move-Item a\b .          b hierher verschieben (Punkt = aktueller Ordner)
Remove-Item a.py         Datei löschen
Remove-Item ordner -Recurse    Ordner mit Inhalt löschen
```

**Pfade sind relativ.** Ein Pfad ohne Laufwerksbuchstabe wird immer vom
aktuellen Ordner aus gelesen. Wenn du verloren bist, hilft der volle Pfad:

```
cd "$HOME\Documents\Lernprojekte\cs50p\woche2"
```

`$HOME` = eigener Benutzerordner. Anführungszeichen, wenn Leerzeichen im
Pfad stecken.

**Den ganzen Ärger vermeiden:** Rechtsklick im Explorer auf den Ordner →
**"Open in Integrated Terminal"**. Öffnet ein Terminal direkt dort.

**Nicht viele Terminals offen lassen.** Steht eines in einem Ordner, lässt
Windows den Ordner nicht verschieben oder löschen ("wird von einem anderen
Prozess verwendet"). Überzählige mit dem Mülleimer-Symbol schließen.

**Pfeil nach oben** holt den letzten Befehl zurück.
**Esc** bringt dich raus, wenn du versehentlich in `fwd-i-search` gelandet
bist. **Strg + C** bricht ein laufendes Programm ab.

Neue Terminals starten immer im Hauptordner — auch nach einem Neustart
von VS Code ("History restored").

---

## Git

Nach jeder Lerneinheit:

```
git add -A                           alle Änderungen vormerken
git commit -m "kurze Beschreibung"   Stand festhalten
git push                             zu GitHub hochladen
```

```
git status                           was ist geändert, was nicht gesichert?
git pull                             Änderungen von GitHub holen
```

`-A` statt `.` benutzen — nur so werden gelöschte und verschobene Dateien
miterfasst. `-A` wirkt vom ganzen Repo aus, egal in welchem Unterordner
du stehst.

> **Stolperstein.** `git commit .m "..."` — Punkt statt Bindestrich.
> Git meldet `pathspec did not match` und committet nichts.

Die Meldung `LF will be replaced by CRLF` ist ein Hinweis, kein Fehler.
Windows und Linux beenden Zeilen unterschiedlich, Git gleicht das ab.

Einmalig eingerichtet, steht hier nur zum Nachschlagen:

```
git config --global user.name "Yusuf Ogul"
git config --global user.email "..."
git init
git remote add origin https://github.com/yusufpesci-del/lernprojekte.git
```

---

## VS Code

| Kürzel | Wirkung |
|---|---|
| Strg + Ö | Terminal auf/zu |
| Strg + S | speichern |
| Strg + N | neue Datei |
| Strg + P | Datei per Namen suchen |
| Strg + Umschalt + Ö | zusätzliches Terminal |

**Punkt im Reiter** = nicht gespeichert → Strg+S
**M im Explorer** = geändert, aber nicht committet → `git commit`
**U im Explorer** = neu, Git kennt die Datei noch gar nicht
**A im Explorer** = vorgemerkt mit `git add`, noch nicht committet

Rot eingefärbte Dateien und Ordner heißen: darin steckt ein Fehler.
Die Zahl bei "Problems" unten sagt, wie viele.

Unten in der Leiste steht die erkannte Einrückung ("Spaces: 4").
Steht da etwas anderes als 4, wurde von Hand mit Leerzeichen eingerückt
statt mit Tab.

---

## Arbeitsweise, die sich bewährt hat

**Beim Video:** anhalten, abtippen, laufen lassen. Nur zuschauen fühlt
sich produktiv an, bringt aber nichts — man versteht alles und kann
danach nichts.

**Varianten stehen lassen.** Alte Fassungen auskommentieren statt löschen,
mit einer Trennlinie und einer Notiz, was sich geändert hat. So sieht man
später die Entwicklung, nicht nur das Ergebnis.

**Selbst testen, nicht nur das Beispiel aus der Aufgabe.** Auch die Fälle
am Rand: leere Eingabe, Großschreibung, Leerzeichen vorne, Zahlen außerhalb
des erwarteten Bereichs.

**Brauche ich das hier, oder habe ich es nur zuletzt benutzt?** Der häufigste
Fehler zu Beginn einer neuen Aufgabe ist mitgeschlepptes Werkzeug: `import
sys`, weil es im Video vorkam. `Output: ` davor, weil die vorige Aufgabe es
wollte. `.title()`, weil es bei taqueria nötig war. `{}`, weil die letzten
drei Programme gezählt haben. Jede Zeile muss sich aus **dieser** Aufgabe
begründen lassen.

**Erst laufen lassen, dann fragen.** Das Terminal antwortet schneller als
jeder Mensch und sagt dir dasselbe. Bei camel und coke war beides schon
richtig, bevor ich nachgefragt habe.

**Klein anfangen, dann auffüllen.** Bei nutrition erst drei Früchte ins
Dictionary und das Programm zum Laufen bringen — die restlichen siebzehn
danach. Wer zwanzig Zeilen tippt und dann startet, sucht den Fehler in
zwanzig Zeilen.

**Dateien in VS Code schließen, wenn Claude sie ändert.** Sonst hält der
Editor die alte Fassung im Speicher und überschreibt die neue beim
nächsten Strg+S. So sind schon zweimal Änderungen verschwunden.

**KI-Vervollständigung aus.** In den ersten Monaten lernt man mehr, wenn
man die Sätze und den Code selbst formuliert.

**Lerntagebuch führen.** Nach jedem Lerntag drei Zeilen in `log.md`:
was gemacht, was unklar, was als Nächstes. Kostet zwei Minuten und ist
bei Motivationstiefs unbezahlbar.

---

## Noch offen

- Problem Set 4

**Woche 4 ist angeschaut** — Bibliotheken, `pip`, `sys.argv`, APIs, eigene
Module. Damit sind Woche 0 bis 4 durch und die Problem Sets 0 bis 3 gelöst.

Zeile für Zeile erklärt stehen alle Programme in `erklaert.md`: die vier
Wiederholungsaufgaben, die vier aus Problem Set 3 und der Mitschrieb
aus Woche 4.
