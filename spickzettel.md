# Spickzettel

Alles, was bis hierher dran war. Nach jeder Lerneinheit unten ergaenzen.

---

## Nachschlagen statt auswendig lernen

Niemand hat die Befehle im Kopf. Was man im Kopf hat, ist:
*"Ich brauche jetzt sowas wie Ersetzen — das muss es geben."* Den Rest liest man nach.

**In VS Code:** Tipp `text.` — es klappt eine Liste aller Befehle auf, die es
fuer Text gibt, mit kurzer Erklaerung.

**Im interaktiven Modus:**

```
python                  startet ihn, Eingabezeile wird zu >>>
dir("")                 listet alles auf, was man mit Text machen kann
help("".replace)        erklaert einen einzelnen Befehl (raus mit q)
exit()                  beendet ihn
```

**Ausprobieren statt raten:**

```
>>> "a b c".replace(" ", "...")
'a...b...c'
```

Das Denkmuster: *Was habe ich* (Text? Zahl? Liste?) und *was will ich haben*.
Der Typ bestimmt, welche Befehle ueberhaupt zur Verfuegung stehen.

---

## Python

### Ausgabe und Kommentare

```python
print("hallo")          # zeigt etwas auf dem Bildschirm an
# alles nach einer Raute ist Kommentar, Python ignoriert es
```

Rechnen und Ausgeben sind zwei verschiedene Dinge. Python zeigt von sich aus
nichts an — nur was mit `print` angefordert wird. Nur im interaktiven Modus
(`>>>`) wird jedes Ergebnis automatisch angezeigt.

### Variablen

```python
x = 1                   # Wert in x ablegen
name = "Yusuf"
```

**Ein Variablenname ist nur ein Etikett, das du frei waehlst.** Er hat nichts
damit zu tun, was der Benutzer eintippt. Bei `name = input()` landet die
Eingabe zur Laufzeit im Behaelter `name` — im Code steht sie nirgends.

### Eingabe

```python
name = input("Wie heisst du? ")
```

`input()` liefert **immer Text**, auch wenn Ziffern eingetippt werden.
Der Text in den Klammern ist nur die Frage, die angezeigt wird — er hat mit
der Antwort nichts zu tun. `input()` ohne Text fragt stumm.

### Datentypen

| Typ | Bedeutung | Beispiel |
|---|---|---|
| `int` | ganze Zahl (integer) | `42` |
| `float` | Kommazahl | `3.14` |
| `str` | Text (string) | `"hallo"` |

```python
int("1")                # macht aus dem Text die Zahl 1
float("1.5")            # macht daraus die Kommazahl 1.5
type("1")               # zeigt den Typ an: str
```

Warum das zaehlt: `1 + 2` ergibt `3`, aber `"1" + "2"` ergibt `"12"`.
Bei Zahlen addiert `+`, bei Texten haengt es aneinander.

```python
x = int(input("Was ist x? "))    # erst fragen, dann umwandeln
```

`int()` bricht mit einem Fehler ab, wenn jemand `hallo` eintippt.
Das Abfangen kommt in Woche 3 (Exceptions).

### Kommazahlen sind ungenau

```
>>> 0.1 + 0.2
0.30000000000000004
```

Kein Python-Problem — der Computer rechnet binaer, und viele Dezimalzahlen
sind dort nicht exakt darstellbar (wie 1/3 im Zehnersystem).

Zwei Konsequenzen fuer die Praxis:
- Kommazahlen **nie** mit `==` vergleichen. Stattdessen pruefen, ob die
  Differenz klein genug ist.
- Fuer Geld keine floats. `Decimal` nehmen oder in Cent als ganze Zahlen
  rechnen — sonst fehlt am Jahresende ein Cent.

### Text bearbeiten

```python
name.strip()                  # Leerzeichen NUR am Anfang und Ende weg
name.lower()                  # alles klein
name.upper()                  # alles gross
name.title()                  # erster Buchstabe jedes Wortes gross
name.replace(" ", "...")      # jedes Vorkommen ersetzen
name.split(" ")               # zerlegt an Leerzeichen -> Liste
```

`.strip()` zerlegt nichts, es raeumt nur aussen auf. Zerlegen ist `.split()`.

```
>>> "   hallo welt   ".strip()
'hallo welt'
>>> "Yusuf Ogul".split(" ")
['Yusuf', 'Ogul']
```

Verketten ist erlaubt und ueblich, die Reihenfolge zaehlt:

```python
name = input("Name? ").strip().title()
text.strip().replace(" ", "...")    # erst aussen aufraeumen, dann ersetzen
```

Faustregel: zwei bis drei Aufrufe verketten, darueber hinaus aufteilen.
Sonst kommt man beim Fehlersuchen an die Zwischenergebnisse nicht mehr heran.

### Mehrere Werte auf einmal zuweisen

```python
first_name, last_name = name.split(" ")
```

Die Anzahl muss passen. Bei nur einem Wort gibt es
`ValueError: not enough values to unpack (expected 2, got 1)`.

### f-Strings

```python
print(f"hallo, {name}")     # setzt den Wert von name ein
```

Das `f` vor dem Anfuehrungszeichen nicht vergessen, sonst steht
woertlich `{name}` da.

Der Doppelpunkt trennt: links **was**, rechts **wie**:

| Angabe | Wirkung | `1234.5678` wird zu |
|---|---|---|
| `,` | Tausendertrennzeichen | `1,234.5678` |
| `.2f` | zwei Nachkommastellen | `1234.57` |
| `,.2f` | beides kombiniert | `1,234.57` |

Achtung: Python nimmt das englische Format (Komma = Tausender,
Punkt = Dezimal). `1,234.57` heisst bei uns `1.234,57`.

### Emoji und Sonderzeichen

Emoji sind normale Zeichen, wie Buchstaben:

```python
text.replace(":)", "🙂")
"\N{SLIGHTLY SMILING FACE}"     # dasselbe, ohne das Zeichen zu tippen
```

Windows-Taste + Punkt oeffnet die Emoji-Auswahl.

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

**Wie das laeuft:** `main()` ganz unten startet das Programm — ohne Einrueckung,
es gehoert zu keiner Funktion. In `main` wird gefragt, das Ergebnis landet in
`text`. Dann wird `convert(text)` aufgerufen: der Inhalt wandert in die
Funktion. `convert` gibt mit `return` ein Ergebnis zurueck — dieses Ergebnis
steht dann dort, wo `convert(text)` stand, und `print` gibt es aus.

**`return` liefert zurueck, `print` gibt aus.** Das ist der Kern: eine Funktion
rechnet und reicht das Ergebnis weiter; ausgegeben wird an einer Stelle.
`return` ist kein Befehl mit Klammern: `return n * n`, nicht `return(n * n)`.

**Regeln:**
- `def name(...):` — Doppelpunkt am Ende nicht vergessen
- Unter jedem `def` muss mindestens eine eingerueckte Zeile stehen.
  Eine leere Funktion ist ein Syntaxfehler.
- `def` legt die Funktion nur an. Ausgefuehrt wird sie erst beim Aufruf.
- Einruecken mit der **Tab-Taste** (= 4 Leerzeichen, Python-Standard)

### Scope — wo eine Variable existiert

Was in einer Funktion angelegt wird, lebt nur dort:

```python
def main():
    x = 5
    hello()

def hello():
    print(x)      # NameError: name 'x' is not defined
```

`x` gehoert zu `main`, `hello` sieht es nicht. Wenn `hello` den Wert braucht,
muss er uebergeben werden — `hello(x)`, und innen heisst er dann so, wie es
in `def hello(n):` steht. Der Name draussen und der Name drinnen haben nichts
miteinander zu tun.

Variablen ganz aussen (nicht in einer Funktion) sind ueberall lesbar — heissen
global, benutzt man sparsam.

---

## Fehler lesen

Der **Traceback** ist das wichtigste Werkzeug. Von unten nach oben lesen:
unten steht, *was* falsch ist, darueber, *wo* (Datei und Zeilennummer),
und `^^^^^` markiert die Stelle.

| Meldung | Ursache |
|---|---|
| `SyntaxError: unterminated string literal` | Anfuehrungszeichen nicht geschlossen oder gemischt |
| `ValueError: not enough values to unpack` | links mehr Variablen als rechts Werte |
| `ValueError: too many values to unpack` | dasselbe andersherum |
| `NameError: name 'x' is not defined` | Variable existiert nicht (oder falscher Scope) |
| `IndentationError` | Einrueckung fehlt oder ist uneinheitlich |
| `can't open file ... No such file or directory` | falscher Ordner im Terminal, oder nicht gespeichert |

VS Code faerbt zusammengehoerige Klammern gleich ein. Wirkt eine Klammer
einsam, fehlt das Gegenstueck.

---

## Terminal (PowerShell)

```
pwd                      wo bin ich gerade?
cd ordnername            in einen Ordner wechseln
cd ..                    eine Ebene hoch (Leerzeichen, zwei Punkte!)
mkdir name               Ordner anlegen
python datei.py          Programm ausfuehren
code datei.py            Datei in VS Code oeffnen
Move-Item a\b .          b hierher verschieben (Punkt = aktueller Ordner)
Remove-Item a.py         Datei loeschen
```

**Pfade sind relativ.** Ein Pfad ohne Laufwerksbuchstabe wird immer vom
aktuellen Ordner aus gelesen. Wenn du verloren bist, hilft der volle Pfad:

```
cd "$HOME\Documents\Lernprojekte\cs50p\woche0"
```

`$HOME` = eigener Benutzerordner. Anfuehrungszeichen, wenn Leerzeichen im
Pfad stecken.

**Den ganzen Aerger vermeiden:** Rechtsklick im Explorer auf den Ordner →
**"Open in Integrated Terminal"**. Oeffnet ein Terminal direkt dort, kein `cd` noetig.

**Nicht viele Terminals offen lassen.** Steht eines in einem Ordner, laesst
Windows den Ordner nicht verschieben ("wird von einem anderen Prozess
verwendet"). Ueberzaehlige mit dem Muelleimer-Symbol schliessen.

**Pfeil nach oben** holt den letzten Befehl zurueck.
**Esc** bringt dich raus, wenn du versehentlich in `fwd-i-search` gelandet bist.

Neue Terminals starten immer im Hauptordner — auch nach einem Neustart
von VS Code ("History restored").

---

## Git

Nach jeder Lerneinheit:

```
git add -A                           alle Aenderungen vormerken
git commit -m "kurze Beschreibung"   Stand festhalten
git push                             zu GitHub hochladen
```

```
git pull                             Aenderungen von GitHub holen
```

`-A` statt `.` benutzen — nur so werden geloeschte und verschobene Dateien
miterfasst. `-A` wirkt vom ganzen Repo aus, egal in welchem Unterordner
du stehst.

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

| Kuerzel | Wirkung |
|---|---|
| Strg + Ö | Terminal auf/zu |
| Strg + S | speichern |
| Strg + N | neue Datei |
| Strg + P | Datei per Namen suchen |
| Strg + Umschalt + Ö | zusaetzliches Terminal |

**Punkt im Reiter** = nicht gespeichert → Strg+S
**M im Explorer** = gespeichert, aber seit dem letzten Commit geaendert → commit
**U im Explorer** = neu, Git kennt die Datei noch gar nicht

Unten in der Leiste steht die erkannte Einrueckung ("Spaces: 4").
Steht da etwas anderes als 4, wurde von Hand eingerueckt statt mit Tab.

---

## Noch offen

- Problem Set 0: Einstein, Tip Calculator
- Woche 1: Conditionals
