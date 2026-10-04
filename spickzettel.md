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

Prüfen, ob etwas drin ist:

```python
if "Harry" in students:
    print("gefunden")
```

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
- `return n * n`, nicht `return(n * n)` — `return` ist kein Befehl mit
  Klammern.

> **Stolperstein.** `def main():` definieren und `main()` am Ende
> vergessen — dann passiert gar nichts. Das Rezept steht im Buch,
> gekocht wird es nie.

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
| `can't open file ... No such file or directory` | falscher Ordner im Terminal, oder nicht gespeichert |

VS Code färbt zusammengehörige Klammern gleich ein. Wirkt eine Klammer
einsam, fehlt das Gegenstück.

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

**KI-Vervollständigung aus.** In den ersten Monaten lernt man mehr, wenn
man die Sätze und den Code selbst formuliert.

**Lerntagebuch führen.** Nach jedem Lerntag drei Zeilen in `log.md`:
was gemacht, was unklar, was als Nächstes. Kostet zwei Minuten und ist
bei Motivationstiefs unbezahlbar.

---

## Noch offen

- Problem Set 2
- Woche 3: Exceptions (Fehler abfangen)
