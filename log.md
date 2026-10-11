## 14.09.2026
- Python 3.14.7, Git 2.55 und VS Code installiert und eingerichtet
- Naechstes Mal: GitHub-Konto anlegen, dann CS50P Woche 0
## 16.09.2026
- GitHub-Konto angelegt, Repo lernprojekte steht, erster Push durch
- CS50P Woche 0 begonnen, Video bis 40:48
- Naechstes Mal: Video ab 40:48 weiter
## 18.09.2026
- CS50P Woche 0, Video bis 54:00
- hello.py mit input, strip, title und f-String
- Naechstes Mal: Video ab 54:00 weiter
## 19.09.2026
- CS50P Woche 0 Video komplett durch
- Spickzettel angelegt, calculator.py geuebt (int, float, f-Strings, scope)
- Naechstes Mal: Problem Set 0
## 20.09.2026
- Problem Set 0 komplett (indoor, playback, faces, einstein, tip)
- Funktionen verstanden: def, return, Parameter, main()
- Scope und Shadowing, Nachschlagen mit dir() und help()
- Naechstes Mal: CS50P Woche 1 (Conditionals)
## 21.09.2026
- CS50P Woche 1 begonnen, Video bis 28:32
- compare.py: if, elif, else, or, Bedingung vereinfachen
- grade.py angefangen
- Naechstes Mal: Video ab 28:32 weiter, grade.py fertig
## 22.09.2026
- CS50P Woche 1 Video komplett durch
- grade.py, parity.py (Modulo), match-case
- Naechstes Mal: Problem Set 1
## 23.09.2026
- Problem Set 1: deep thought und bank geloest
- startswith(), Reihenfolge bei elif-Ketten
- Naechstes Mal: Aufgabe 3 von Problem Set 1
## 24.-28.09.2026
- Pause, arbeitsbedingt kein Lernen
## 29.09.2026
- Problem Set 1: extensions und interpreter geloest
- endswith(), split() mit drei Variablen, f-String mit .1f
- Ordnerstruktur in woche1 aufgeraeumt (Dateien jetzt flach)
- Naechstes Mal: Meal Time, letzte Aufgabe aus Problem Set 1
## 30.09.2026
- Problem Set 1 komplett (deep, bank, extensions, interpreter, meal)
- convert-Funktion mit echter Umrechnung, verkettete Vergleiche
- Naechstes Mal: CS50P Woche 2 (Loops)
## 01.10.2026
- CS50P Woche 2 begonnen, Video bis 31:00
- while, for, range, erste Listen
- Naechstes Mal: Video ab 31:00
## 03.10.2026
- CS50P Woche 2, Video bis 55:00
- Listen und len()
- Naechstes Mal: Video ab 55:00
## 04.10.2026
- CS50P Woche 2 Video komplett durch
- Dictionaries, verschachtelte Schleifen, break
- Spickzettel Woche 0-2 neu strukturiert, Lernplan auf Fassung 2 ueberarbeitet
  (Tempo auf 1 CS50P-Woche pro Kalenderwoche, Zielland USA, Phase 3 jetzt Web statt C#)
- Naechstes Mal: Wiederholung, dann Problem Set 2
## 08.10.2026
- Problem Set 2 begonnen, Aufgabe camelCase verstanden
  (camelCase vs snake_case, jeder Grossbuchstabe wird Unterstrich + Kleinbuchstabe)
- Naechstes Mal: camel.py schreiben
## 09.10.2026
- camel.py geloest, auf eigenem Weg: direkt in der Schleife ausgeben statt sammeln
- isupper() und bool verstanden - True/False ist dasselbe, was in jedem if steckt
- for ... in wiederholt, "" (leerer Text) und end="" auseinandergehalten
- coke.py geloest, erste eigene while-Schleife
  Muenzpruefung mit "in" und Liste, Wechselgeld ueber -amount_due
- Erkenntnis: erst laufen lassen, dann fragen. Beide Loesungen waren richtig,
  bevor ich nachgefragt habe
- Naechstes Mal: Problem Set 2, Aufgabe 3 (Just setting up my twttr)
## 10.10.2026
- twttr.py geloest. Es gibt kein isvowel() - "Vokal" ist eine menschliche
  Kategorie, die Liste muss man selbst hinschreiben
- Gelernt: "in" bei Text heisst "kommt irgendwo darin vor", bei einer Liste
  "ist einer dieser Eintraege". Mit Kommas im Text verschwand das Komma aus
  Hello, World
- not in statt if/else - spart den leeren Zweig
- nutrition.py begonnen, erstes eigenes Dictionary. Drei Anlaeufe gebraucht:
  erst Liste von Dictionaries aus dem Video, dann elif-Kette, dann richtig
- Die eigentliche Lektion: Daten gehoeren ins Dictionary, Logik in die
  drei Zeilen darunter. 20 Fruechte = 20 Datenzeilen, aber keine Zeile Logik mehr
- Zwei Fehler zum Merken: input als Variablenname zerstoert die Funktion input.
  Und Schluessel muessen klein sein, wenn die Eingabe .lower() bekommt
- Reihenfolge verstanden: Python liest von oben nach unten, nichts darf
  benutzt werden, bevor es existiert
- Naechstes Mal: nutrition fertig auffuellen, dann Vanity Plates
## 11.10.2026
- nutrition.py fertig: alle 20 Fruechte, .strip().lower() auf der Eingabe
- plates.py geloest - Problem Set 2 ist damit komplett, fuenf von fuenf
- Aufbau gewaehlt: Hilfsfunktion is_valid(), die True/False zurueckgibt,
  jede Regel einzeln, bei Verstoss sofort return False. Ausgabe nur in main()
- return beendet die ganze Funktion, break nur die Schleife - der Unterschied
  war mir vorher nicht klar
- Neu und schwer: Regel 3. Man kann nicht jedes Zeichen einzeln beurteilen,
  sondern muss sich beim Durchlaufen merken, ob schon eine Ziffer kam.
  Dafuer eine bool-Variable VOR der Schleife, in der Schleife if/elif
- elif statt else war entscheidend - else haette bei jedem Buchstaben
  zugeschlagen, auch bei denen vor der ersten Ziffer
- Weitere Fallen: "".isdigit() ist False (leeres Stueck beim Slicing),
  break ohne Schleife ist ein SyntaxError, Code unter return laeuft nie,
  und die Laufvariable darf nicht so heissen wie die Funktion
- Drei Durchgaenge haben am meisten Zeit gekostet: Einrueckung, Namen die
  etwas ueberschreiben, Code unterhalb von return
- Naechstes Mal: vier Wiederholungsaufgaben (wiederholung/aufgaben.md),
  danach Woche 3 (Exceptions)
