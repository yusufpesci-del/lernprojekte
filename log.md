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
## 12.10.2026
- Wiederholungsaufgaben 1 bis 3 geloest: druck.py, klasse.py, material.py
- druck.py hat am laengsten gedauert, sechs Anlaeufe. Der Knoten sass beim
  Zusammenspiel zweier Funktionen: was return zurueckgibt, ist das Einzige,
  was die aufrufende Funktion sieht. Eine Variable aus convert kennt main nicht
- Was geholfen hat: raus aus der Datei, rein in den interaktiven Modus und die
  Kette Zeile fuer Zeile aufbauen, bis jedes Zwischenergebnis sichtbar war.
  Danach war die Funktion nur noch Abschreiben. Merken fuer das naechste Mal,
  wenn ich mich festfahre
- split(" ") gibt eine LISTE zurueck - deshalb [0] fuer den ersten Teil.
  Und ein Leerzeichen am Ende der Eingabe erzeugt ein leeres drittes Element
- klasse.py: == statt >= hat drei Faelle verschluckt (7.0, 8.5, 9.0 landeten
  in Klasse 1). Haette ich beim Testen der Grenzwerte sofort gesehen - habe
  nicht getestet, obwohl die Werte in der Aufgabe standen
- Dabei gelernt: in einer elif-Kette weiss jeder Zweig schon, dass alle
  vorherigen nicht zutrafen. Von gross nach klein geprueft reicht die untere
  Grenze, die obere ist geschenkt
- material.py: Zaehlmuster im Dictionary - pruefen ob bekannt, dann += 1,
  sonst neu mit 1 anlegen. Ohne den zweiten Fall bleibt das Dictionary ewig leer
- Selbst gemerkt: druck.py stuerzt bei "5bar" ohne Leerzeichen ab. Genau dafuer
  ist Woche 3 da - nicht jeden Sonderfall vorher abfangen, sondern den Absturz
  auffangen
- Woche 3 angefangen, Video bis 20:00. Dann gemerkt, dass ich nicht mehr
  aufnahmefaehig bin, und aufgehoert. Das war richtig so
- Naechstes Mal: Video ab 20:00 weiter. stueckliste.py (Aufgabe 4) bleibt offen
  und kommt vor Problem Set 3
## 13.10.2026
- CS50P Woche 3 Video komplett durch (Exceptions)
- Der Kern: nicht jeden Sonderfall vorher abfragen, sondern es versuchen und
  den Absturz auffangen. Lieber um Verzeihung bitten als um Erlaubnis fragen
- try = die riskante Zeile, except ValueError = Reaktion darauf,
  else = nur wenn es geklappt hat
- In try gehoert so wenig wie moeglich - nur die Zeile, die scheitern kann.
  Sonst faengt das except spaeter Fehler mit, die ganz woanders herkommen
- Die Falle: scheitert int(), wurde x nie angelegt. Wer danach auf x zugreift,
  bekommt NameError - ein Fehler ersetzt den anderen. Dafuer ist else da
- Der eigentliche Gewinn ist while True drumherum: bei unsinniger Eingabe wird
  einfach nochmal gefragt, statt aufzugeben. pass im except reicht dabei
- Die Exception-Namen kannte ich alle schon, weil ich jede einzelne in den
  letzten Wochen selbst produziert habe. Neu ist nur, sie abzufangen
- Naechstes Mal: stueckliste.py (Wiederholungsaufgabe 4), danach Problem Set 3
## 14.10.2026
- stueckliste.py Stufe 1 bis 3: Eingabe bis "fertig", Zeile zerlegen,
  Mengen im Dictionary addieren, Ausgabe mit Gesamtsumme
- Erst gedacht, ich muesste material.py und coke.py vermischen. Falsch -
  coke hatte mit der Aufgabe nichts zu tun. material.py allein war das Geruest
- Hauptfehler: ich habe nach position (der ganzen Zeile) gefragt, aber artikel
  (nur den Namen) ins Dictionary gelegt. Deshalb wurde jede Menge
  ueberschrieben statt addiert
- Regel daraus: man muss nach demselben fragen, das man auch hineinlegt.
  In den eckigen Klammern bei zaehler[...] steht immer ein Schluessel
- .items() gibt immer erst den Schluessel, dann den Wert - egal wie man die
  beiden Namen nennt
- Zum Schluss die Form von plates.py uebertragen, ohne zu ueberlegen was
  geprueft werden soll. Zeichen fuer zu lange Konzentration, also aufgehoert
- Naechstes Mal: ERST in Worten "Eine Zeile ist brauchbar, wenn ...", dann Code
## 15.10.2026
- stueckliste.py fertig - damit sind ALLE VIER Wiederholungsaufgaben durch
- Der Satz in Worten war die eigentliche Arbeit. Danach war die Pruefunktion
  vier Zeilen und in fuenf Minuten fertig. Das Vorgehen merken
- Gelernt: teile = zeile.split(" ") klappt IMMER, egal wie viele Teile.
  Aber artikel, menge = zeile.split(" ") wirft ValueError, wenn es nicht
  genau zwei sind. Zwei Namen links verlangen genau zwei Teile
- len(zeile) zaehlt Zeichen, len(teile) zaehlt Teile - nicht verwechseln
- teile[:2] ist ein Ausschnitt (wieder eine Liste), teile[1] ein Eintrag
- .isalpha().isdigit() geht nicht: die erste Frage liefert True/False, und
  ein True kann man nicht nochmal fragen. AttributeError
- Dieselbe Pruefung nochmal mit try/except geschrieben (stueckliste2.py).
  Kuerzer, und sie prueft mit genau den Operationen, die main danach ausfuehrt
- Interessanter Fund beim Vergleich: bei "Rohr -5" sind sich die beiden
  Fassungen uneinig. isdigit() sagt False (Minus ist keine Ziffer), int("-5")
  funktioniert. Zwei Loesungen, die bei allen Testfaellen gleich sind, koennen
  trotzdem verschieden sein - zeigt sich erst bei einem Fall, an den keiner
  gedacht hat
- erklaert.md angelegt: alle vier Aufgaben Zeile fuer Zeile auf Deutsch
  kommentiert, zum Nachlesen
- Naechstes Mal: Problem Set 3 (Exceptions)
## 16.10.2026
- Freitag statt Samstag gelernt, weil ich So-Mo in Grossbeeren arbeiten muss.
  Puffertag getauscht - genau dafuer ist er da
- Problem Set 3: fuel.py und taqueria.py geloest. Beide mit try/except
- fuel.py in drei Stufen gebaut: erst der Normalfall, dann E und F,
  dann die Fehlerbehandlung. Das Vorgehen funktioniert
- Wichtigste Einsicht: nicht alles ist ein Fehler, den man abfangen kann.
  "drei/vier" wirft ValueError, "3/0" ZeroDivisionError - aber "5/4" laeuft
  glatt durch. Dass ein Tank nicht voller als voll sein kann, ist Fachwissen,
  keine Mathematik. Das muss ich selbst mit einem if pruefen
- Zwei Fehlerarten in einem except: except (ValueError, ZeroDivisionError)
- taqueria.py: EOFError zum ersten Mal benutzt - und zwar NICHT fuer eine
  Panne, sondern weil der Benutzer fertig ist. Exceptions sind der Weg, auf
  dem Python ungewoehnliche Situationen meldet, nicht nur Fehler
- Auf Windows ist es Strg+Z und Enter, nicht Strg+D wie in der Aufgabe
- Stolperstein: .title OHNE Klammern tut nichts - die Klammern sind das
  "wende es an". Ohne sie steht in der Variablen die Methode statt des Texts
- Nochmal derselbe Fehler wie bei nutrition: .lower() auf die Eingabe, aber
  die Schluessel gross geschrieben. Hier .title() genommen, weil die
  Speisekarte durchgehend so geschrieben ist
- Claude hatte zwei Preise falsch diktiert (Tortilla Salad, Baja Taco).
  Selbst auf der CS50-Seite nachgeschaut und korrigiert. Merke: die
  Aufgabenstellung ist die Quelle, die deutsche Erklaerung nur Uebersetzung
- Vergleich zu Montag: da sechs Anlaeufe fuer druck.py mit drei Zeilen,
  heute zwei komplette Programme mit Schleife und Fehlerbehandlung in
  derselben Zeit
- Naechstes Mal: Grocery List und Outdated, dann ist Problem Set 3 durch
## 17.10.2026
- grocery.py und outdated.py geloest - PROBLEM SET 3 IST KOMPLETT.
  Damit Woche 0 bis 3 und die Problem Sets 0 bis 3 durch, einen Tag vor Plan
- grocery.py: erst eine feste Einkaufsliste erfunden, wie bei taqueria die
  Speisekarte. Falsch gedacht - hier gibt es keinen Katalog, alles was
  getippt wird zaehlt. Die Aufgabe lesen, nicht die vorige kopieren
- sorted(zaehler).items() geht nicht: sorted() liefert eine LISTE, und eine
  Liste hat kein .items(). Also for name in sorted(zaehler) und drinnen
  zaehler[name] nachschlagen
- outdated.py in drei Stufen gebaut, und das war diesmal meine eigene
  Entscheidung: erst nur 9/8/1636, dann Schleife und Pruefungen, dann das
  Wortformat
- Englische Variablennamen ab jetzt: month, day, year. Passt zum US-Ziel
  und zur Doku. Deutsch und Englisch in einer Datei mischen will ich nicht
- months.index("September") liefert 8, nicht 9 - gezaehlt wird ab 0, also
  + 1. Und .index() wirft ValueError, wenn der Name nicht in der Liste
  steht: "Jan 1, 1970" wird dadurch von selbst abgelehnt, ohne dass ich
  eine Zeile dafuer schreibe
- Am Ende faengt EIN except ValueError fuenf Quellen ab: Nicht-Zahlen,
  falsche Teilzahl beim Schraegstrich, fehlendes Komma im Wortformat,
  unbekannter Monatsname, zu wenige Teile. Das ist der Punkt von Woche 3
- Neu gelernt: die Weiche. if "/" in date: ... else: ... und darunter geht
  es gemeinsam weiter. Beide Zweige muessen dieselben Namen fuellen, dann
  steht alles danach nur EINMAL da. Dafuer muss input() vorher in eine
  Variable, weil der Text zweimal gebraucht wird
- Stolperstein input(date): input() heisst IMMER "frag den Benutzer". Was
  in den Klammern steht, ist nur die Beschriftung - nie die Quelle. Der
  Text lag schon in date, ich wollte zerlegen statt fragen
- Stolperstein months.index("month"): in Anfuehrungszeichen ist das das
  WORT month, nicht der Inhalt der Variablen
- Stolperstein 1 < month > 12: verkettete Vergleiche werden mit UND
  verbunden, heisst also "groesser 1 und groesser 12" - erst ab 13 wahr,
  die 0 kommt durch. Richtig: not 1 <= month <= 12
- Zwischendurch dreimal dieselbe Zeile mit minimaler Aenderung geschickt
  statt den naechsten Schritt anzufangen. Claude hat das Muster erkannt
  und angeboten Schluss zu machen. Habe weitergemacht, und danach lief es
  in kleinen Schritten durch. Dasselbe Muster wie bei druck.py am Montag
- Was geholfen hat: eine Wegwerf-Datei test.py mit zwei Zeilen und einem
  FESTEN Text statt input(). Jeden Zwischenschritt einzeln ausgeben lassen.
  Erst als die drei Teile einzeln dastanden, ging es weiter. Das merken
- Zeiten neu festgelegt: Mo-Fr erst ab 21 Uhr, 2 bis 3 Stunden.
  Sa und So die langen Tage. Lernplan entsprechend angepasst
- Naechstes Mal: Woche 4 (Libraries), ab Dienstag. So und Mo Grossbeeren
## 18.10.2026
- Grossbeeren, kein Rechner. Spickzettel und erklaert.md am Handy gelesen
  (Woche-3-Teil und die neue Weiche-Stelle)
## 20.10.2026
- Woche 4 (Libraries) angefangen, Video bis 44:41 (Kapitel "Packages").
  Erster Abend nach dem neuen Rhythmus: 21:40 bis 23:20, hat gepasst
- Der Kerngedanke der Woche: bis jetzt war jedes Programm komplett von mir.
  Ab jetzt benutze ich fremden Code. import random heisst, jemand anders
  hat Zufallszahlen schon geloest
- random.choice(liste) zieht EIN Element zufaellig raus
- Zwei Schreibweisen fuer dasselbe:
  import random          -> dann random.choice(...)
  from random import choice -> dann choice(...)
  Die erste ist die bessere Gewohnheit, weil man sieht wo etwas herkommt
- statistics.mean(liste) rechnet den Mittelwert, kommt immer als
  Kommazahl zurueck - auch 95.0 wenn es glatt aufgeht
- sys.argv ist eine LISTE mit dem was im Terminal stand. argv[0] ist immer
  die Datei selbst, argv[1] das erste danach
- Dabei IndexError kassiert: python name.py ohne Namen dahinter. Dann hat
  die Liste nur Position 0, und argv[1] gibt es nicht
- Das ist der Sinn von argv: das Programm fragt nicht mehr nach, es
  bekommt alles beim Start mitgeliefert. git commit -m "..." ist genau
  dasselbe Prinzip
- Woche 3 trifft Woche 4: try/except IndexError um argv[1]. Besser ist
  sys.exit("Too few arguments") - gibt die Meldung UND beendet.
  print allein laeuft weiter
- Alternative ohne try: if len(sys.argv) < 2. Bei argv ueblicher, weil man
  die Laenge ohne Risiko abfragen kann
- Noch offen aus dem Video: pip, APIs, eigene Module,
  if __name__ == "__main__"
- Naechstes Mal: zweite Haelfte Woche 4 ab pip install
## 21.10.2026
- Woche 4 zu Ende geschaut. Zweiter Abend nach dem neuen Rhythmus,
  21:00 bis 22:30
- pip install cowsay hat geklappt. Erste fremde Bibliothek aus dem Netz -
  genau so kommen spaeter Oberflaeche und PDF-Ausgabe ins FM-Werkzeug
- requests und die iTunes-API. Da haengengeblieben: Malan zeigt die API im
  Browser und ich dachte, er laedt irgendwo eine Datei runter. Es wird
  NICHTS runtergeladen. Der Browser ist nur ein Fenster auf die Antwort
- requests.get(adresse) macht genau das, was sonst die Adresszeile macht.
  Deshalb zeigt er es erst im Browser - damit man sieht was ankommt,
  bevor Code im Weg steht
- Dass es bei ihm aufgeraeumt aussah, ist eine Browser-Erweiterung fuer
  JSON. Kosmetik, kein Einrichtungsschritt
- Zwei Richtungen, das war der verwirrende Teil:
  response.json()            Antwort-Text -> Python
  json.dumps(x, indent=2)    Python -> lesbarer Text
  indent=2 ist nur die Anzahl Leerzeichen pro Ebene
- Der Umweg ueber Python lohnt sich, weil man dort einzelne Werte
  rausholen kann statt der ganzen Antwort
- Verschachtelte Daten: o["results"] ist eine LISTE, darin stecken
  Dictionaries. Also for result in o["results"] und drinnen
  result["trackName"]
- Eigene Module: from sayings import hello in say.py. Jede .py-Datei ist
  ein Modul und kann importiert werden
- if __name__ == "__main__" verstanden. Der Schluessel: import heisst
  nicht "schau rein", Python FUEHRT die Datei AUS, von oben nach unten.
  Ohne das if wuerde main() beim Importieren mitlaufen
- __name__ ist "__main__" bei direktem Start, sonst der Modulname.
  Also nur ein if auf eine Variable die Python selbst fuellt, keine
  Zauberei. Die zwei Unterstriche heissen "verwaltet Python"
- Regel: sobald eine Datei auch nur vielleicht importiert wird, gehoert
  die Startzeile in dieses if
- Stolperstein in generate.py: for card in cards: print(cards) gibt
  dreimal die GANZE Liste aus. Gemeint war print(card). Einzahl und
  Mehrzahl unterscheiden sich um einen Buchstaben - noch zu korrigieren
- random.shuffle(cards) gibt NICHTS zurueck, es mischt die Liste direkt
  an ihrem Platz. cards = random.shuffle(cards) macht None draus
- sys.argv[1:] ist ein Ausschnitt ab Position 1, also alle Argumente
  ohne den Dateinamen
- Angewohnheit die ich beibehalte: alle Varianten aus dem Video als
  Kommentar in der Datei stehen lassen, mit ---- getrennt. Macht spaeter
  nachvollziehbar wie es sich entwickelt hat
- Naechstes Mal: Problem Set 4 am Samstag
## 23.10.2026
- Freitag statt Puffertag, aber nur eine Aufgabe. Problem Set 4,
  Aufgabe 1: emojize geloest. 22:00 bis 22:30
- pip install emoji, wie bei cowsay
- Drei aehnliche Namen durcheinandergebracht:
  emoji      = die Bibliothek, die man importiert
  emojize    = die Funktion darin
  emojize.py = meine eigene Datei
  import emojize haette also meine EIGENE Datei importiert. Genau der
  Stolperstein von Mittwoch mit random.py, nur sofort
- sys und json mitimportiert, die ich hier gar nicht brauche - nur weil
  sie im Video vorkamen. Nicht alles mitnehmen was man zuletzt gesehen hat
- Stolperstein, und zwar zweimal in einer Aufgabe: text = print(...).
  print gibt NICHTS zurueck, es legt nur etwas auf den Bildschirm.
  PRINT STEHT NIE RECHTS VOM =
- Dritter Anlauf, weil ich fragen, umwandeln und ausgeben in EINE Zeile
  gequetscht habe. Drei Saetze sind drei Zeilen. Das Vorgehen von der
  Stueckliste - erst in Worten hinschreiben - hilft immer noch
- Auch wieder: den Text fest in den Code geschrieben statt ihn vom
  Benutzer zu holen. Dann sagt das Programm immer dasselbe, egal was man
  eintippt
- Gefragt wie ich Variablen nennen soll. Antwort gemerkt: Namen brauchen
  keine Kreativitaet, nur eine Beschreibung. Die Frage ist immer "was
  steckt drin?". Hier text, weil Text drin steckt. Immer das Ding, nie
  die Taetigkeit - eingeben oder umwandeln waeren schlechte Namen
- language="alias" ist NICHT optional. Ohne den Parameter fallen
  :smile_cat: und :thumbsup: durch - und :smile_cat: ist eines der drei
  Beispiele der Aufgabenstellung. Es gibt zwei Schreibweisen pro Emoji:
  den offiziellen Code (:thumbs_up:) und den Spitznamen (:thumbsup:)
- Benannte Parameter hatte ich schon gesehen: json.dumps(o, indent=2)
- Ganze Saetze funktionieren auch, die Codes werden mitten im Text
  ersetzt. Das macht die Bibliothek, nicht ich
- f-String genommen statt print mit Komma. Beides richtig
- Noch offen: generate.py aus Woche 4, print(cards) muss print(card)
  werden
- Naechstes Mal: Rest von Problem Set 4 am Samstag
## 24.10.2026
- Problem Set 4: figlet und adieu geloest. Stand 3 von 6.
  12:45 bis 16:10 mit einer Pause - der lange Samstag wie im Lernplan
- Zuerst die Aufgabenseite geholt statt aus dem Kopf zu raten. Ergebnis:
  SECHS Aufgaben, alle einzureichen. Claudes "drei auswaehlen" von
  Mittwoch war falsch
- figlet: mein erstes OBJEKT. Figlet() erzeugt ein DING, das sich etwas
  merkt - naemlich die eingestellte Schriftart. Der Punkt heisst hier
  nicht mehr Bibliothek.Werkzeug, sondern mein Ding.seine Faehigkeit
- Deshalb braucht es eine Variable: mit dem Ding passieren ZWEI Dinge
  nacheinander, erst setFont, dann renderText.
  Figlet().renderText(...) direkt verketten geht nicht - dazwischen gab
  es nie Gelegenheit, die Schrift einzustellen
- Verwechselt: sys.argv[2] ist die SCHRIFTART, input() ist der TEXT.
  Habe erstmal die Schriftart gerendert
- Tabs und Leerzeichen gemischt -> IndentationError. Fuer mich sehen die
  gleich aus. Fix in VS Code: Statusleiste unten rechts auf Spaces
  klicken, Convert Indentation to Spaces
- Bei figlet KEIN "Output: " davor, anders als bei emojize. Das verschiebt
  die erste Zeile der Grafik um acht Zeichen, das C bricht ab, check50
  faellt durch
- import figlet haette wieder die eigene Datei importiert. Die Bibliothek
  heisst pyfiglet. Zweiter Tag in Folge derselbe Fehler - merken: die
  Bibliothek heisst NIE so wie meine Datei
- Die Weiche mit drei Ausgaengen gebaut: keine Argumente -> Zufallsschrift,
  geprueftes -f -> die gewuenschte, sonst sys.exit("Invalid usage").
  Beide guten Zweige fuellen EINE Variable (font), danach geht es
  gemeinsam weiter. Dieselbe Struktur wie outdated.py
- sys.argv[1] in ("-f", "--font") statt zweimal == mit or
- Habe die Schriftart-Pruefung ANDERS gebaut als Claudes Geruest: nicht in
  die elif-Bedingung, sondern als eigenes if im Zweig. Claude sagt das ist
  sauberer, weil die Bedingung kurz bleibt und die Pruefung direkt bei der
  Variablen steht. Erste eigene Strukturentscheidung
- adieu: zum ersten Mal die Doku einer Bibliothek selbst gelesen. Erst
  p.plural geraten - das macht aber Mehrzahl aus EINEM Wort. Dann join
  gefunden, durch Eingrenzen: was geht rein, was kommt raus? Liste rein,
  fertiger Satzteil raus. Das Eingrenzen war die Methode, nicht das
  Finden eines Beispiels
- join macht alle sieben Faelle der Aufgabe allein: 1 Name ohne Komma,
  2 mit and, 3+ mit Kommas UND and. Ein Anfaenger baut dafuer eine
  if-Kette. Das ist Woche 4 in einem Satz
- {} ist ein Dictionary, [] eine Liste. Bei grocery habe ich GEZAEHLT
  (Name -> Anzahl), hier SAMMLE ich nur, in Reihenfolge. .append() gibt
  es nur bei Listen, und join will eine Liste
- .title() aus taqueria mitgeschleppt. Dort noetig, weil die Eingabe zu
  den Schluesseln der Speisekarte passen musste. Hier gibt es nichts zu
  vergleichen - aus "von Trapp" wuerde "Von Trapp"
- append AUSSERHALB des try platziert, von selbst. Nur die riskante Zeile
  gehoert ins try. Dasselbe wie bei grocery
- MUSTER DES TAGES, dreimal passiert: Werkzeug aus der vorigen Aufgabe
  mitgeschleppt. sys und json bei emojize, Output: bei figlet, {} und
  .title() bei adieu. Die Frage gehoert an den Anfang jeder Aufgabe:
  brauche ich das HIER, oder habe ich es nur zuletzt benutzt?
- "Adieu, adieu" - erstes Wort gross, zweites klein. Erst beide klein
  geschrieben, dann beide gross. check50 vergleicht buchstabengetreu
- Noch offen: generate.py aus Woche 4, print(cards) muss print(card)
  werden. Steht seit Mittwoch im Log
- Naechstes Mal: game, professor, bitcoin. Spaetabends oder Sonntag
## 25.-27.10.2026
- Sonntag ab etwa 12:30 nichts mehr gemacht. Seit Sonntag in Belgien und
  remote fuer INDUZEIT gearbeitet. CS50P lag drei Tage still
- Ab Mittwoch abend (28.10.) wieder dabei
- Keine Schuldgefuehle dafuer. Genau dafuer stehen die zwei Pufferwochen
  im Lernplan, und die Regel dort heisst: nicht nachholen, nicht
  verdoppeln, da weitermachen wo ich aufgehoert habe. Im September hat
  das nach fuenf Tagen Zwangspause schon einmal funktioniert
- Stand unveraendert: Woche 0-4 durch, Problem Set 0-3 komplett,
  Problem Set 4 bei 3 von 6 (emojize, figlet, adieu)
- Naechstes Mal: game.py, und zwar nur der Level-Teil. Fragen, pruefen,
  bei einer positiven ganzen Zahl raus aus der Schleife
## 28.10.2026
- Zurueck nach drei Tagen Belgien. game.py geloest, Problem Set 4 steht
  bei 4 von 6. 21:30 bis 22:00 - nach der Pause erstaunlich glatt
- Habe mehr gebaut als gefragt war: statt nur dem Level-Teil gleich den
  ganzen Normalfall mit Rateschleife. Reihenfolge der drei Faelle stimmte
  sofort - zu klein, zu gross, else - und break nur beim Treffer.
  else statt "elif guess == number": wenn weder kleiner noch groesser,
  bleibt nur gleich
- Dann die Pruefung drumherum. NEU: eine Funktion, die so lange fragt bis
  etwas Brauchbares kommt, und die Zahl dann ZURUECKGIBT
- return statt break. break verlaesst nur die Schleife, return verlaesst
  die ganze Funktion UND bringt einen Wert mit
- Was bei schlechter Eingabe passieren soll, muss man gar nicht
  hinschreiben: wird return nicht erreicht, dreht die Schleife von selbst
  noch eine Runde. Kein else, kein continue
- Der Gewinn: EINE Funktion, zweimal benutzt.
  get_positive("Level: ") und get_positive("Guess: ").
  Die Beschriftung kommt als Parameter rein
- Unterschied zu ist_brauchbar aus der Stueckliste: das gab True/False
  zurueck und der Aufrufer musste selbst entscheiden. get_positive gibt
  die ZAHL zurueck und kuemmert sich selbst um den Fehlerfall
- WICHTIGSTE EINSICHT DES ABENDS: pruefen, wo der Wert hereinkommt -
  nicht dort, wo er spaeter Schaden anrichtet. Level: -1 stuerzte NICHT
  am int() ab, int("-1") ist ja in Ordnung, sondern zwei Zeilen spaeter
  bei random.randint(1, -1) mit "empty range in randrange(1, 0)".
  Die Fehlermeldung zeigte auf eine Zeile, die nichts dafuer konnte
- main() muss HINTER alle def stehen, die darin benutzt werden. Sonst
  NameError. Letzte Zeile der Datei
- random.randint(1, level) nimmt beide Grenzen mit - bei Level 10 also
  auch die 10
- Tabs in main(), Leerzeichen in get_positive(). Laeuft, weil jede
  Funktion fuer sich einheitlich ist, aber eine Zeitbombe. Noch zu
  konvertieren
- Noch offen: generate.py print(cards) -> print(card), und die aeusseren
  Klammern in figlet.py
- Naechstes Mal: professor und bitcoin, dann ist Problem Set 4 durch
## 31.10.2026
- PROBLEM SET 4 IST KOMPLETT. professor.py und bitcoin.py geloest, damit
  alle sechs. 15:40 bis 18:30 mit zwei Pausen
- Stand: Woche 0-4 durch, Problem Sets 0-4 geloest. Trotz der drei Tage
  Belgien wieder im Plan - die Woche sah genau das vor
- professor: die Schwierigkeit war nicht die Logik, sondern die
  BUCHHALTUNG. score = 0 VOR der aeusseren Schleife, weil es mitwachsen
  soll. solved = False IN der aeusseren Schleife, weil es bei jeder
  Aufgabe neu anfangen muss. Stuende solved oben, waere es nach der
  ersten richtigen Antwort fuer immer True und die Loesung wuerde nie
  mehr gezeigt
- Dabei haengengeblieben: ich dachte True sei die Variable. Falsch -
  True und False sind WERTE, wie 0 und 5. Ein bool braucht einen Namen,
  genau wie score = 0. Dann steht dieser Name an drei Stellen:
  anlegen (False), umschalten (True), abfragen (if not ...)
- range(True) haette uebrigens range(1) bedeutet, weil True als 1 zaehlt -
  also nur EIN Versuch statt drei
- if not solved, nicht "answer is not solved". Ein bool IST schon die
  Antwort, man vergleicht es mit nichts
- NEU: raise ValueError. Bisher habe ich Fehler nur GEFANGEN, jetzt werfe
  ich selbst einen. Ohne die Zeile faellt generate_integer(7) unten raus
  und gibt stillschweigend None zurueck - und es knallt erst in main()
  bei x + y, an einer Zeile die nichts dafuer kann
- Zwei Schleifen, zwei Gruende: for _ in range(10) weil die ANZAHL
  feststeht, for _ in range(3) weil die OBERGRENZE feststeht
- get_level() ohne Parameter, anders als get_positive(prompt) bei game.
  Ein Parameter verdient sich erst, wenn er sich auch aendert - hier ist
  die Beschriftung immer "Level: ". Habe ich dreimal falsch gemacht
- bitcoin: musste mich bei CoinCap anmelden und einen API-Schluessel
  anlegen. Die alte Schnittstelle ohne Schluessel ist abgeschaltet
- Claude hat darauf bestanden, den Schluessel NICHT ins Repo zu lassen -
  mein Repo ist oeffentlich. Loesung: secret.py mit einer Zeile, in
  .gitignore, und in bitcoin.py steht from secret import API_KEY.
  Technisch dasselbe wie sayings.py und say.py. Steht nicht in der
  Aufgabenstellung - CS50 rechnet nicht mit oeffentlichen Loesungen
- Einmal committet bliebe der Schluessel auch in der HISTORIE stehen,
  selbst wenn man ihn danach loescht. Deshalb vorher aufpassen
- Stolperstein: except requests.RequestException beim float() gesetzt.
  Falsch - float("cat") wirft ValueError. Und weil requests dort noch
  gar nicht importiert war, kam beim BEHANDELN des Fehlers ein
  NameError. Die Frage ist immer: was kann an DIESER Stelle schiefgehen?
- Zwei Stellen, zwei Fehlertypen, zwei getrennte try-Bloecke
- Verschachtelt nachschlagen: data["data"]["priceUsd"], zwei eckige
  Klammerpaare hintereinander, eins pro Ebene. NICHT ["data","priceUsd"],
  das waere eine Liste mit zwei Woertern
- Der Preis kommt als TEXT aus dem JSON, mit Anfuehrungszeichen.
  Ohne float() rechnet man mit Text
- Ich hatte das Beispiel-JSON aus Claudes Erklaerung in meinen Code
  kopiert. Das schickt der Server, das schreibe ich nicht hin
- :,.4f - das Komma ist das Tausendertrennzeichen
- Wieder der Klassiker: $1.0 statt des Kurses, weil die Datei nicht
  gespeichert war. Zweites Mal. Erst speichern, dann wundern
- Zwei verirrte Ordner gefunden und geloescht: mkdir war zweimal
  gelaufen, waehrend ich schon IM Zielordner stand. Mit $HOME davor
  passiert das nicht
- Naechstes Mal: Woche 5 (Unit Tests)
## 02.11.2026
- Woche 5 (Unit Tests) komplett angeschaut, 21:10 bis 23:05. Alle vier
  Dateien mitgebaut: calculator.py, test_calculator.py, hello.py,
  test_hello.py
- Der Kerngedanke: Testen war bisher eine TAETIGKEIT - starten, tippen,
  hinschauen, nach jeder Aenderung von vorn. Ab jetzt ist es ein ARTEFAKT.
  Eine Datei, die bleibt und in einer Sekunde laeuft
- assert dreht die Logik um: ich schreibe hin, was STIMMEN SOLL, statt zu
  pruefen was schiefgehen koennte. Stimmt es, passiert NICHTS. Schweigen
  heisst in Ordnung
- pytest sucht selbst alle Funktionen, die mit test_ anfangen. In der
  Testdatei braucht man weder main() noch if __name__ == "__main__"
- Vier kleine Testfunktionen statt einer grossen, aus zwei Gruenden:
  pytest meldet pro Funktion, man weiss also sofort WO. Und ein
  fehlgeschlagenes assert bricht die Funktion ab - alles darunter laeuft
  gar nicht mehr und wuerde unbemerkt ungeprueft bleiben
- with pytest.raises(TypeError) - pruefen, dass es KNALLT. Hier ist der
  Fehler das gewuenschte Verhalten. Gegenstueck zu raise ValueError aus
  generate_integer: dort werfe ich, hier pruefe ich dass geworfen wird
- with ist neu, kommt in Woche 6 richtig dran
- Standardwerte: def hello(to="world"). Der Parameter wird optional.
  Kenne ich von der anderen Seite - bei emojize(text, language="alias")
  und json.dumps(o, indent=2) habe ich fremde Standardwerte ueberschrieben
- Und test_hello prueft BEIDE Wege: einmal mit Standardwert, einmal mit
  Argument. Zwei Verhaltensweisen, zwei Tests
- Warum Randfaelle: in der Vorlesung stand versehentlich n + n statt
  n * n. Bei square(2) kommt trotzdem 4 raus - der Fehler fiel erst bei
  square(3) auf. Ein Test, der nur das Naheliegende prueft, beweist nichts
- if __name__ == "__main__" ist ab jetzt PFLICHT in der getesteten Datei.
  Ohne das wuerde beim Importieren das Programm anlaufen und mitten im
  Test nach Eingaben fragen
- AI-Vervollstaendigung in VS Code abgeschaltet. Sie schreibt ganze Zeilen
  und nimmt mir genau das weg, woran ich gerade arbeite - das
  Zusammensetzen. Steht so auch in meinen Regeln im README
- Gelernt: Strg + # kommentiert markierte Zeilen aus und wieder ein.
  Spart viel Tipperei bei meiner Gewohnheit, alte Fassungen stehenzulassen
- NOCH OFFEN: der Package-Teil. Ordner test/ angelegt, test_hello.py darin
  ist aber noch leer und __init__.py fehlt. Das nachholen
- Di-Fr Schulung von 9 bis 17 Uhr. Abends bleiben 1-2 Stunden, aber nach
  acht Stunden Schulung. Deshalb diese Woche: abends nur lesen und
  wiederholen, Problem Set 5 am Wochenende
- Naechstes Mal: Problem Set 5
## 07.11.2026
- Erster Abend nach FUENF Tagen Pause (Di-Fr Schulung 9-17). Problem
  Set 5 angefangen: twttr und bank fertig, 2 von 4. 21:40 bis 23:00
- Selbst gemerkt und notiert: die Pause war spuerbar. Aber WAS weg war,
  ist der Rhythmus, nicht das Verstaendnis. Ich wusste die ganze Zeit was
  assert tut und wozu die Testdatei da ist - gestolpert bin ich beim
  Zusammensetzen. Wie Joggen nach zwei Wochen: die Lunge ist da, der
  Rhythmus nicht. Konsequenz: kurz und oft schlaegt lang und selten
- Problem Set 5 verlangt keine neuen Programme, sondern TESTS fuer die
  alten. Und damit den Umbau: die Logik muss in eine Funktion, die etwas
  ZURUECKGIBT. Ein Programm, das alles in main() erledigt und direkt
  printet, kann man nicht pruefen - nur starten und hingucken
- Erkenntnis der Woche: testbarer Code und gut gebauter Code sind
  DASSELBE
- twttr war fast fertig, weil ich es im Oktober schon mit einer
  zurueckgebenden Funktion gebaut hatte. Nur: Datei hiess twttr OHNE
  .py und war damit nicht importierbar, convert musste shorten heissen,
  und main() unten wurde zum if __name__
- Dabei einmal den Rumpf von shorten geloescht, weil ich vom leeren
  Geruest der Aufgabenseite neu angefangen habe statt meine Datei zu
  aendern. Das Geruest zeigt die FORM, es ist keine Vorlage zum Abtippen
- Und das if __name__ landete in der for-Schleife. Es gehoert ganz nach
  unten an den linken Rand, ausserhalb jeder Funktion - es ist die
  Startzeile der DATEI, kein Teil einer Funktion
- return ergebnis vergessen. Ohne return gibt eine Funktion None zurueck,
  der Test haette None mit "hll" verglichen
- WICHTIGSTE LEKTION DES ABENDS: meine ersten Tests prueften nichts.
  shorten("hello") und shorten("Yusuf") gingen BEIDE durch, als die
  Funktion absichtlich kaputtgemacht wurde (nur kleine Vokale). Grund:
  in keinem der Woerter steckt ein grosser Vokal - bei Yusuf ist das Y
  gross, aber Y ist kein Vokal. Mit TWITTER statt Yusuf hat der Test
  sofort angeschlagen
- Daraus: in JEDE Testfunktion gehoert ein Beispiel vom Rand
- bank war echte Umbauarbeit, die Fassung aus Problem Set 1 hatte gar
  keine Funktionen. Zwei Verschiebungen:
  1. Das $ wanderte von der Logik in die Ausgabe. value gibt die ZAHL 0
     zurueck, main setzt das $ davor. Eine Zahl kann man vergleichen,
     "$0" ist nur zum Angucken
  2. Das .lower() wanderte von main() nach value(). Das ist die
     wichtigere: der Test ruft value DIREKT auf. Mit .lower() in main
     bekaeme value("Hello") ein grosses H und antwortete 20 statt 0 -
     obwohl das Programm beim normalen Starten stimmt
- EINE FUNKTION MUSS FUER SICH ALLEIN RICHTIG SEIN. Ein Test ist genau
  der Aufrufer, der sich nicht an die Gewohnheiten des Programms haelt
- Stolperstein: == "0" statt == 0 geschrieben, alle fuenf Tests fielen
  durch. value liefert eine ZAHL. pytest zeigt es an den
  Anfuehrungszeichen: assert 0 == '0'. Von der anderen Seite kenne ich
  das seit Woche 1 - input() liefert immer Text, deshalb int() drum
- Testnamen aus der vorigen Aufgabe mitgeschleppt (test_default,
  test_argument aus test_hello.py) und pytest.raises aus
  test_calculator.py, wo hier gar nichts schiefgehen soll. Zum x-ten Mal
  dasselbe Muster. Der Testname ist die FEHLERMELDUNG - pytest meldet
  FAILED test_bank.py::test_uppercase, da hilft test_argument nicht
- Den erwarteten Wert bestimme ICH, nicht das Programm. Sonst pruefe ich
  nur, dass das Programm tut was es tut - Fehler inklusive
- Gegenprobe bei bank: .lower() geloescht -> 3 failed, 2 passed. Eine
  mehr als erwartet, weil value("How are you") mit grossem H auch
  durchfiel. Und test_lowercase und test_any blieben gruen - richtig so,
  ein gutes Testset meldet genau das was kaputt ist, nicht alles
- Noch 18 Tage bis Uebersee, tagsuber viel zu tun
- Naechstes Mal: plates und fuel, dann ist Problem Set 5 durch
## 08.11.2026
- PROBLEM SET 5 IST KOMPLETT. plates und fuel geloest, damit alle vier.
  16:00 bis 17:35. Woche 0-5 durch, Problem Sets 0-5 geloest - einen Tag
  vor Plan
- plates war fast geschenkt: die Fassung aus Problem Set 2 hatte schon
  main() und ein is_valid(plate), das True/False ZURUECKGIBT. Nur die
  Waechterzeile fehlte. Claude hat is_valid gegen 13 Faelle geprueft,
  keine Abweichung
- Bei den Testnamen gehangen und gefragt. Hatte aber selbst schon fuenf
  brauchbare: test_length, test_startswith, test_endswith, test_notzero,
  test_nopunctuation. Claude hat nur geschaerft - test_digits_at_end
  statt test_endswith, weil die Regel nicht "endet mit" heisst (NRVOUS
  ohne Zahl ist gueltig), sondern "WENN Ziffern kommen, dann nur am Ende"
- Erster Entwurf von test_length enthielt is_valid("CS05") - das ist aber
  wegen der fuehrenden Null ungueltig, nicht wegen der Laenge. Der Test
  waere gruen geblieben, auch ohne Laengenpruefung
- DIE PROBE FUER JEDEN TEST: wenn ich genau diese eine Regel aus dem
  Programm entferne - faellt dann genau DIESER Test durch? Wenn nicht,
  prueft er etwas anderes als sein Name sagt
- Gegenprobe plates: Laengenpruefung auskommentiert -> 1 failed,
  4 passed. Einer rot, vier gruen
- assert is_valid("CS50") statt == True. Ein bool ist schon die Antwort,
  wie if not solved bei professor
- fuel war der groesste Umbau: die alte Fassung hatte GAR KEINE
  Funktionen, alles in einer Schleife, die obendrein ihre eigenen Fehler
  abfing
- KERNGEDANKE DER AUFGABE: wer wirft, und wer faengt?
  convert wirft den Fehler - sie weiss nur, dass "cat/50" Unsinn ist
  main faengt ihn auf - sie entscheidet, was dann passiert
  Grund: convert KANN NICHT WISSEN, was der Aufrufer tun will. Nochmal
  fragen? Abbrechen? Protokollieren? Sache des Aufrufers
- Und genau deshalb ist sie testbar. Ein Test will nicht, dass convert
  nochmal fragt - er will sehen, dass sie sich beschwert. Eine Funktion
  mit eingebauter Schleife wuerde im Test ewig auf Eingabe warten
- Aus continue wurde raise ValueError. Zwei Fehler musste ich gar nicht
  selbst werfen: int("cat") wirft von allein, x / 0 auch. Ein eigenes
  raise braucht nur die Regel, die NIEMAND AUSSER MIR kennt: x > y
- Verwechselt: ich dachte convert zerlegt nur und gibt zwei Zahlen
  zurueck. Nein - convert macht den GANZEN Weg, "3/4" rein, 75 raus
- DIE REIHENFOLGE DER PRUEFUNGEN entscheidet, welchen Fehler der Aufrufer
  sieht. Mit if x > y vor der Division gibt convert("1/0") einen
  ValueError, weil 1 > 0 wahr ist und zur Division nie kommt. Verlangt
  war ZeroDivisionError. Also Null-Pruefung zuerst
- gauge(percentage) musste von print auf return umgebaut werden. Einmal
  dabei gauge(percentage) ohne print geschrieben - Ergebnis ausgerechnet
  und weggeworfen
- Das print habe ich aus der Schleife herausgenommen und dahinter
  gesetzt. Claude sagt, das ist besser als sein Vorschlag: die Schleife
  hat genau eine Aufgabe, naemlich eine brauchbare Eingabe beschaffen.
  Die Ausgabe passiert danach, einmal
- Bei fuel ist pytest.raises RICHTIG - anders als bei twttr gestern, wo
  ich danach gegriffen hatte, obwohl nichts schiefgehen sollte.
  convert("5/4") MUSS sich beschweren, der Fehler ist das gewuenschte
  Verhalten
- Erster Testentwurf hatte ein test_str, das dasselbe prueft wie
  test_convert_errors - und die x > y-Regel blieb ungetestet. Claude hat
  die Pruefung aus fuel.py entfernt: 4 passed, nichts gemerkt
- ZUM DRITTEN MAL AN DIESEM WOCHENENDE dieselbe Luecke. Bei twttr die
  Grossschreibung, bei plates die Laenge, bei fuel der zu grosse Zaehler.
  MEINE EIGENEN raise UND return False SIND DIE CHECKLISTE. Die Regel,
  an die man beim Testen nicht denkt, ist die, die man beim
  Programmieren selbst eingebaut hat
- Mit test_too_big dann vier Gegenproben, jede macht GENAU EINEN Test
  rot. Das ist das Guetezeichen: null rot heisst, die Regel wird von
  keinem Test bewacht. Alle rot heisst, die Tests sind nicht getrennt
- Was Problem Set 5 im Ganzen war: vier alte Programme so umbauen, dass
  man sie pruefen kann. Rechnen und Ausgeben trennen, Werfen und Fangen
  trennen, alles Noetige IN die Funktion, Darstellung an den Rand.
  Laeuft alles auf dasselbe hinaus: eine Funktion muss fuer sich allein
  richtig und fuer sich allein benutzbar sein
- Abends noch Woche 6 angefangen (File I/O), bis Minute 30 von 92.
  Doppelter Tag also: Problem Set 5 fertig UND die halbe naechste Woche
- Gefragt, warum Malan erst die Listen-Fassung schreiben laesst und sie
  dann wegwirft. Antwort: die zeigt das PROBLEM, das die Datei loest.
  Liste dreimal starten -> jedes Mal leer. Datei dreimal starten -> die
  Namen sammeln sich. Erst die Wand, dann die Tuer. Dasselbe Muster wie
  Woche 3 (if-Ketten -> try/except) und Woche 4 (selbst schreiben ->
  import)
- Die Listen-Fassung hatte ausserdem range(3), also genau drei Namen,
  vorher festgelegt. Die Datei kennt keine Obergrenze
- open(name, modus) mit drei Betriebsarten: "r" lesen, "w" NEU schreiben
  (alter Inhalt weg), "a" anhaengen. Mit "w" haette jeder Start die Datei
  ueberschrieben und nur der letzte Name waere uebrig
- append heisst dasselbe wie bei liste.append(x) - hinten dran. Einmal
  fuer Listen im Speicher, einmal fuer Dateien auf der Platte. Hatte ich
  bei adieu.py schon benutzt, war mir aber nicht mehr praesent
- write setzt KEINEN Zeilenumbruch, den muss man selbst mitschicken:
  f"{name}\n"
- with open(...) as file: kein close() mehr noetig. Am Ende des Blocks
  wird die Datei zugemacht, AUCH wenn dazwischen ein Fehler fliegt.
  Genau dafuer ist with da
- with kannte ich schon von with pytest.raises(TypeError) aus Woche 5 -
  dasselbe Bauprinzip, ein Block mit besonderer Regel und Aufraeumen am
  Ende. Jetzt weiss ich auch, was es wirklich tut
- for line in file: eine Datei verhaelt sich wie eine Liste ihrer Zeilen,
  man laeuft direkt darueber
- .rstrip() noetig, weil jede Zeile ihren Zeilenumbruch mitbringt:
  "Hermione\n". Ohne rstrip steht der in der Ausgabe und jeder Vergleich
  schlaegt fehl
- sorted(names, reverse=True) dreht die Reihenfolge um. Wieder ein
  benannter Parameter mit Standardwert, wie language="alias" und indent=2
- Noch offen in Woche 6: CSV und Bilder (PIL)
- Naechstes Mal: zweite Haelfte Woche 6
