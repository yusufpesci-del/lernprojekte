# Wiederholung Woche 0 bis 2

Vier Aufgaben, bevor Woche 3 anfängt. Sie bringen **nichts Neues** — alles
darin hast du schon benutzt. Es geht darum, ob es sitzt, wenn niemand
danebensteht und sagt, welches Werkzeug dran ist.

**So arbeitest du sie durch:**

- Eine nach der anderen, in dieser Reihenfolge. Sie werden schwerer.
- Erst selbst versuchen, ohne Spickzettel. Wenn du nach fünf Minuten nicht
  weißt, womit du anfangen sollst, dann nachschlagen — das ist kein
  Scheitern, Nachschlagen ist die Arbeit.
- **Jede Aufgabe laufen lassen und mit allen Beispielen testen**, bevor du
  mich fragst. Das Terminal antwortet schneller.
- Erst danach zeigst du mir alle vier zusammen.

Lege für jede eine eigene Datei im Ordner `wiederholung` an.

---

## Aufgabe 1 — `druck.py`

Ein Druck in bar soll in psi umgerechnet werden. **1 bar = 14.5038 psi.**

Das Programm fragt nach dem Druck, die Eingabe enthält die Einheit mit.
Ausgegeben wird das Ergebnis auf **zwei Nachkommastellen**.

```
Druck: 5 bar
72.52 psi
```

```
Druck: 1 bar
14.50 psi
```

```
Druck: 12.5 bar
181.30 psi
```

**Bedingungen:**

- Die Umrechnung steht in einer **eigenen Funktion**, die das Ergebnis mit
  `return` zurückgibt — sie gibt selbst nichts aus.
- Das Programm hat ein `main()`, das die Funktion benutzt.
- Du darfst annehmen, dass die Eingabe immer die Form `<zahl> bar` hat.

*Geprüft wird:* `input`, Text zerlegen, Umwandlung in eine Kommazahl,
Funktion mit `return`, f-String mit Nachkommastellen.

---

## Aufgabe 2 — `klasse.py`

Eine Lagerguthöhe in Metern soll einer Klasse zugeordnet werden.

| Höhe | Ausgabe |
|---|---|
| unter 3.0 m | `Klasse 1` |
| ab 3.0 bis unter 6.0 m | `Klasse 2` |
| ab 6.0 bis 9.0 m einschließlich | `Klasse 3` |
| über 9.0 m | `Sonderfall` |

```
Lagerguthoehe in m: 2.5
Klasse 1
```

```
Lagerguthoehe in m: 6.0
Klasse 3
```

```
Lagerguthoehe in m: 9.4
Sonderfall
```

**Teste unbedingt die Grenzen:** `2.9`, `3.0`, `5.9`, `6.0`, `9.0`, `9.1`.
Genau dort gehen solche Programme kaputt. Überleg dir bei jedem Wert
vorher, was herauskommen muss, und vergleiche dann.

*Geprüft wird:* Umwandlung in eine Kommazahl, `if`/`elif`/`else`,
Reihenfolge der Zweige, verkettete Vergleiche.

---

## Aufgabe 3 — `material.py`

Ein Monteur zählt auf, was er verbaut hat. Das Programm fragt so lange
nach Material, bis eine **leere Eingabe** kommt. Danach gibt es aus, wie
oft jedes Material genannt wurde.

```
Material: Sprinklerkopf
Material: Rohr
Material: Sprinklerkopf
Material: Halterung
Material: Sprinklerkopf
Material:
Sprinklerkopf: 3
Rohr: 1
Halterung: 1
```

**Bedingungen:**

- Die Ausgabe kommt in der Reihenfolge, in der die Materialien **zuerst**
  genannt wurden — nicht alphabetisch, nicht nach Anzahl.
- Groß- und Kleinschreibung soll egal sein: `rohr` und `Rohr` sind dasselbe.
- Wird gar nichts eingegeben, gibt das Programm nichts aus und endet.

*Geprüft wird:* `while`, `break`, Dictionary aufbauen und hochzählen,
`in`, über ein Dictionary laufen, f-String.

---

## Aufgabe 4 — `stueckliste.py` (die Kür)

Diese Aufgabe fasst alles zusammen. Nimm dir Zeit und bau sie in Schritten,
so wie bei plates.

Das Programm liest Zeilen der Form `<Artikel> <Anzahl>` ein, bis `fertig`
eingegeben wird. Danach gibt es jeden Artikel mit seiner Gesamtzahl aus und
darunter die Summe aller Teile.

```
Position: Sprinklerkopf 12
Position: Rohr 40
Position: Sprinklerkopf 8
Position: fertig

Sprinklerkopf: 20
Rohr: 40
Gesamt: 60
```

**Bedingungen:**

- Kommt ein Artikel mehrfach vor, werden die Anzahlen **addiert**.
- Eine Zeile ohne Anzahl oder mit etwas anderem als einer ganzen Zahl wird
  **ignoriert** — kein Absturz, keine Fehlermeldung, einfach weiter fragen.
  (`Rohr`, `Rohr zwei`, `Rohr 3 Stück` → alle ignorieren.)
- Die Prüfung, ob eine Zeile brauchbar ist, steht in einer **eigenen
  Funktion**, die `True` oder `False` zurückgibt.
- Vor der Ausgabe steht eine Leerzeile, wie im Beispiel.

**Der Tipp, den du bei plates gelernt hast:** nicht alles auf einmal. Erst
die Schleife, die bis `fertig` liest und die Zeilen nur ausgibt. Dann das
Zerlegen. Dann das Dictionary. Dann die Prüfung. Jeden Schritt laufen
lassen.

*Geprüft wird:* alles zusammen — `while`, `break`, Text zerlegen,
Umwandlung in eine ganze Zahl, Dictionary aufbauen und addieren,
Funktion mit `True`/`False`, Summe bilden, Ausgabe formatieren.

---

## Wenn du nicht weiterkommst

Erst im Spickzettel nachschlagen, nicht fragen. Wo was steht:

| Du brauchst | Abschnitt im Spickzettel |
|---|---|
| Eingabe zerlegen, Stücke herausschneiden | Text bearbeiten |
| Zahl aus Text machen | Datentypen |
| Nachkommastellen in der Ausgabe | Ausgabe formatieren |
| `if` / `elif`, Reihenfolge der Zweige | Bedingungen |
| `while`, `break`, über Zeichen laufen | Schleifen |
| Dictionary anlegen, nachschlagen, prüfen | Dictionaries |
| `return`, `main()`, Funktion mit True/False | Funktionen |
| Fehlermeldung verstehen | Fehler lesen |

Und wenn der Spickzettel nicht reicht: `dir("")` im interaktiven Modus.
Das Denkmuster steht unter **Nachschlagen statt auswendig lernen** — was
habe ich, was will ich haben.

---

## Danach

Wenn alle vier laufen, bist du für Woche 3 bereit. Dort kommt etwas
wirklich Neues dazu: **Exceptions** — wie man dafür sorgt, dass ein
Programm bei einer unsinnigen Eingabe nicht abstürzt, sondern nochmal
fragt. Bei Aufgabe 4 umgehst du das noch zu Fuß. Ab Woche 3 gibt es ein
Werkzeug dafür.
