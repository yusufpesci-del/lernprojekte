# Spickzettel

Alles, was bis hierher dran war. Nach jeder Lerneinheit unten ergaenzen.

---

## Python

### Ausgabe und Kommentare

```python
print("hallo")          # gibt Text aus
# alles nach einer Raute ist Kommentar, Python ignoriert es
```

### Variablen

```python
x = 1                   # Wert in x ablegen
name = "Yusuf"
```

### Eingabe

```python
name = input("Wie heisst du? ")
```

`input()` liefert **immer Text**, auch wenn Ziffern eingetippt werden.

### Datentypen

| Typ | Bedeutung | Beispiel |
|---|---|---|
| `int` | ganze Zahl (integer) | `42` |
| `float` | Kommazahl | `3.14` |
| `str` | Text (string) | `"hallo"` |

```python
int("1")                # macht aus dem Text die Zahl 1
type("1")               # zeigt den Typ an: str
```

Warum das zaehlt: `1 + 2` ergibt `3`, aber `"1" + "2"` ergibt `"12"`.
Bei Zahlen addiert `+`, bei Texten haengt es aneinander.

```python
x = int(input("Was ist x? "))    # erst fragen, dann umwandeln
```

Achtung: `int()` bricht mit einem Fehler ab, wenn jemand `hallo` eintippt.
Das Abfangen kommt in Woche 3 (Exceptions).

### Text bearbeiten

```python
name.strip()            # Leerzeichen am Anfang und Ende weg
name.title()            # erster Buchstabe jedes Wortes gross
name.split(" ")         # zerlegt an Leerzeichen -> Liste

"Yusuf Ogul".split(" ")  # ergibt ['Yusuf', 'Ogul']
```

Verketten ist erlaubt und ueblich:

```python
name = input("Name? ").strip().title()
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

### Interaktiver Modus

```
python              startet ihn, Eingabezeile wird zu >>>
exit()              beendet ihn
```

Gut fuer schnelle Pruefungen ("was gibt `.split()` eigentlich zurueck?"),
nie fuer richtige Programme.

---

## Fehler lesen

Der **Traceback** ist das wichtigste Werkzeug. Von unten nach oben lesen:
unten steht, *was* falsch ist, darueber, *wo* (Datei und Zeilennummer),
und `^^^^^` markiert die Stelle.

| Meldung | Ursache |
|---|---|
| `SyntaxError: unterminated string literal` | Anfuehrungszeichen nicht geschlossen oder gemischt |
| `ValueError: not enough values to unpack` | links mehr Variablen als rechts Werte |
| `can't open file ... No such file or directory` | Datei nicht gespeichert oder falscher Ordner |

---

## Terminal (PowerShell)

```
cd cs50p\woche0          in einen Ordner wechseln
cd ..                    eine Ebene hoch
mkdir name               Ordner anlegen
python datei.py          Programm ausfuehren
Move-Item a.py ordner\   Datei verschieben
Remove-Item a.py         Datei loeschen
```

**Pfeil nach oben** holt den letzten Befehl zurueck. Spart viel Tipparbeit.

Neue Terminals starten immer im Hauptordner — erst `cd cs50p\woche0`,
dann arbeiten.

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

`-A` statt `.` benutzen — nur so werden geloeschte und verschobene
Dateien miterfasst.

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

Punkt im Reiter statt X heisst: **nicht gespeichert**.
`M` neben dem Dateinamen heisst: geaendert, aber noch nicht committet.

---

## Noch offen

- Problem Set 0 (fuenf Aufgaben)
- Woche 1: Conditionals
