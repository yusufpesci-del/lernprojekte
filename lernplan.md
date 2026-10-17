# Lernplan — Fassung 2

**Erstellt 14.09.2026, überarbeitet 04.10.2026 nach drei Wochen echter Daten.**
Ziel: Entwicklerstelle in 1–2 Jahren, bevorzugt USA.

---

## Was sich gegenüber Fassung 1 geändert hat

**Das Tempo.** Fassung 1 hatte CS50P Woche 2 und 3 in dieselbe Kalenderwoche
gelegt. Nach drei Wochen ist klar: realistisch ist **eine CS50P-Woche pro
Kalenderwoche**, inklusive Problem Set. Die Videos sind der kleinere Teil.

**Das Zeitbudget.** Angesetzt waren 16 Std./Woche, tatsächlich sind es 6–10.
Der Plan rechnet jetzt mit **8–10 Stunden**. Lieber eine ehrliche Zahl, die
stimmt, als eine ambitionierte, die jede Woche als Versagen endet.

**Das Zielland.** Fassung 1 zielte auf deutsche TGA-Softwarehäuser. Inzwischen
ist die USA das wahrscheinlichere Ziel. Das ändert die zweite Sprache (siehe
Phase 2) und macht die Fachkenntnis eher wertvoller: FM Global ist ein
amerikanisches Regelwerk.

---

## Wochenrhythmus (10–12 Std.)

**Überarbeitet am 17.10.** Entscheidend ist nicht nur wie viel Zeit, sondern
**wann**: unter der Woche geht es erst ab 21 Uhr los.

| Tag | Zeit | Inhalt |
|---|---|---|
| Mo–Do | 3 Abende, je 1,5–2 Std. ab 21 Uhr | Videolektion, Spickzettel und `erklaert.md` lesen, kleine Übungen |
| Fr | frei | Puffertag — bewusst nichts |
| Sa | 3–4 Std. am Stück | Problem Set |
| So | 2–3 Std. | Rest vom Problem Set, Wiederholung, Lerntagebuch |

**Abends aufnehmen, am Wochenende bauen.** Am 17.10. war der Unterschied
deutlich zu sehen: drei Stunden lang lief das Zerlegen und Zusammensetzen
von Code gut, in der vierten kam dreimal dieselbe Zeile mit einer
Winzigkeit geändert. Kein fehlendes Verständnis — Ermüdung. Videos,
Spickzettel und Erklärungen lesen geht um 22 Uhr noch. Ein Problem Set von
null auf lösen nicht.

**Drei Abende, nicht fünf.** Möglich sind Mo–Fr je 2–3 Stunden — fünf
Abende bis Mitternacht wären aber über 20 Std./Woche. Der Plan läuft noch
neun Monate; das hält niemand durch. Drei Abende sind das Maß, das jede
Woche funktioniert. Ein vierter ist ein Bonus, kein Soll.

Zwei Regeln bleiben: an jedem Lerntag mindestens ein Commit. Und den
Freitag wirklich freihalten.

**Wenn eine Woche ausfällt:** nicht nachholen, nicht verdoppeln. Da
weitermachen, wo du aufgehört hast. Aufgeben passiert fast nie wegen zu wenig
Zeit, sondern wegen der Schuldgefühle nach einer verpassten Woche. Das hat im
September schon einmal funktioniert.

---

## Phase 1 — CS50P fertig (Oktober bis Mitte Dezember)

Eine CS50P-Woche pro Kalenderwoche. **Stand 17.10.: Woche 0–3 durch,
Problem Set 3 komplett.** Der Plan sah die Woche bis zum 18.10. vor —
fertig am 17.10., also einen Tag früher. Zweite Woche im Takt.

| Zeitraum | Inhalt |
|---|---|
| ~~05.–11.10.~~ | ~~Problem Set 2~~ ✅ fertig am 11.10. |
| ~~12.–18.10.~~ | ~~Wiederholung Woche 0–2, Woche 3 (Exceptions) + Problem Set 3~~ ✅ fertig am 17.10. |
| 19.–25.10. | Woche 4 (Libraries) + Problem Set 4 |
| 26.10.–01.11. | Woche 5 (Unit Tests) + Problem Set |
| 02.–08.11. | Woche 6 (File I/O) + Problem Set |
| 09.–15.11. | Woche 7 (Regular Expressions) + Problem Set |
| 16.–22.11. | Woche 8 (Object-Oriented Programming) + Problem Set |
| 23.–29.11. | Woche 9 (Et Cetera) + Problem Set |
| 30.11.–14.12. | Abschlussprojekt |

**Zwei Wochen Puffer sind eingerechnet** — eine Krankheitswoche oder eine
Projektphase im Job wirft den Plan damit nicht um. Werden sie nicht
gebraucht, bist du früher fertig.

> **Meilenstein 1 (Ende Oktober):** Du kannst Fehler abfangen (`try`/`except`)
> und fremde Bibliotheken einbinden. Ab da kannst du Programme schreiben, die
> nicht beim ersten Tippfehler des Benutzers abstürzen.
> **Erste Hälfte erreicht am 17.10.** — vier Programme mit `try`/`except`,
> keines stürzt bei falscher Eingabe ab. Bleibt: die Bibliotheken.

> **Meilenstein 2 (Mitte Dezember):** CS50P komplett, neun Problem Sets und
> ein Abschlussprojekt im öffentlichen Repo.

**Zertifikat: noch offen.** Die Erinnerung vom 10.10. ist nicht beantwortet
worden. Problem Set 0 bis 3 sind gelöst, aber nicht bei CS50 eingereicht.
Nachreichen ist möglich — je später, desto mehr Sets auf einmal. Spätestens
vor Woche 5 entscheiden.

---

## Phase 2 — Das Nischenprojekt (ab Anfang November, parallel)

Ab CS50P Woche 5 hast du genug beisammen: Funktionen, Listen,
Dictionaries, Dateien lesen und schreiben, Fehlerbehandlung.

Dann fängt das **FM-Auslegungstool** an — der Ja/Nein-Klickpfad, der
Fachplaner von der Einstufung bis zur Auslegung führt. Keine Inhalte aus den
Data Sheets übernehmen, nur auf die Fundstellen verweisen.

**Warum das wichtiger ist als der Kurs:** CS50P machen jedes Jahr
zehntausende. Ein Werkzeug, das Sprinkleranlagen nach FM-Regelwerk auslegt,
gebaut von jemandem mit VdS-Fachplanerschein und fünf Jahren Baustelle, gibt
es genau einmal. Das ist der Türöffner, den kein Mitbewerber vorzeigen kann.

Vorgehen: klein anfangen. Erst eine Textversion im Terminal, die drei oder
vier Fragen stellt und am Ende eine Einstufung ausgibt. Erst wenn die
Logik steht, kommt die Oberfläche.

> **Meilenstein 3 (Ende Januar):** Eine erste lauffähige Fassung im Repo,
> die man benutzen kann. Nicht fertig — benutzbar.

---

## Phase 3 — Web, damit man es anklicken kann (Januar bis März)

**Hier weicht Fassung 2 am deutlichsten ab.** Fassung 1 sah C# / .NET vor,
wegen Revit- und AutoCAD-Erweiterungen und deutscher TGA-Software.

Für den US-Markt und für dein eigenes Projekt ist ein anderer Weg besser:
**Python im Web.** Konkret HTML und CSS in Grundzügen, etwas JavaScript,
und FastAPI oder Flask als Rückseite.

Der Grund ist einfach: Ein Personaler in den USA klickt auf einen Link und
sieht dein Tool in zehn Sekunden laufen. Eine Revit-Erweiterung müsste er
erst installieren — und dafür Revit besitzen. Für ein Portfolio ist das
der Unterschied zwischen gesehen und nicht gesehen.

Dazu in dieser Phase: SQL und eine Datenbank, damit das Tool Projekte
speichern kann.

C# bleibt eine Option für später, falls sich herausstellt, dass du gezielt
zu einem Revit-Plugin-Haus willst. Der Umstieg kostet dann drei bis vier
Wochen, weil die Denkweise dieselbe ist.

> **Meilenstein 4 (Ende März):** Das FM-Tool läuft im Browser unter einer
> eigenen Adresse. Jemand anders als du hat es benutzt.

---

## Phase 4 — Bewerbungsreife (April bis Sommer)

- Zweites Projekt, das nichts mit Brandschutz zu tun hat — zeigt, dass du
  nicht nur eine Sache kannst
- Repo aufräumen: README mit Screenshots, saubere Commit-Historie.
  Ab hier wird das Repo englisch — README zuerst, dann die Kommentare
  im Code
- Englischer Lebenslauf und LinkedIn auf die neue Richtung ausrichten
- Visum und Arbeitserlaubnis USA klären — das ist der längste Vorlauf
  und gehört früher angefangen als man denkt

---

## Ressourcen

| Zweck | Ressource | Kosten |
|---|---|---|
| Hauptkurs | CS50P (Harvard, cs50.harvard.edu/python) | kostenlos |
| Praxisbuch | Automate the Boring Stuff with Python | kostenlos online |
| Tägliche Übungen | Exercism, Python Track | kostenlos |
| Git | Learn Git Branching, Pro Git | kostenlos |
| SQL | SQLBolt, danach PostgreSQL lokal | kostenlos |
| Web | MDN Web Docs | kostenlos |

Alles auf Englisch — das ist kein Umweg, sondern Teil des Jobs, besonders
mit dem US-Ziel.

---

## Was bisher stimmt (Stand 17.10.2026)

Fünf Wochen, dreiundzwanzig selbst geschriebene Programme, vier Problem
Sets.

- Problem Set 0 bis 3 vollständig selbst gelöst
- Nach fünf Tagen Zwangspause ohne Murren weitergemacht
- Lerntagebuch und Commits konsequent geführt
- Fragen nach dem Warum statt nach der Lösung
- **Das Tempo stimmt.** Am 04.10. hinkte der Plan; Fassung 2 wurde in
  ihren ersten beiden Wochen eingehalten, die zweite sogar einen Tag früher.

Was in Woche 2 dazukam, war mehr als eine neue Technik: bei plates war
zum ersten Mal ein Programm zu bauen, das sich beim Durchlaufen etwas
**merkt**, statt jedes Element für sich zu beurteilen. Das ist der
Übergang von Rechnen zu Programmieren.

Woche 3 hat noch einen draufgesetzt: **nicht jede falsche Eingabe ist ein
Fehler.** `5/4` beim Tank und `13/8/1636` beim Datum rechnen sich sauber
aus und sind trotzdem unmöglich. Diese Grenze zwischen "Python meldet es"
und "das weiß nur ich" selbst zu ziehen, ist Ingenieursarbeit — und genau
das, was bei einem Auslegungswerkzeug später die ganze Logik ausmacht.

Was sich wiederholt und Zeit kostet: Einrückung, Namen die etwas
überschreiben, und das Zusammensetzen funktionierender Einzelteile zu
einer Kette. Das Letzte ist der eigentliche Engpass — nicht Verständnis,
sondern Montage. Dagegen hilft nachweislich: in kleinen Schritten bauen,
jeden Zwischenschritt ausgeben lassen, und bei Formeln erst den deutschen
Satz hinschreiben, dann übersetzen.

**Vor Woche 3** standen vier Wiederholungsaufgaben in
`cs50p/wiederholung/aufgaben.md`. Nicht übersprungen — und das hat sich
ausgezahlt: die Stückliste enthielt bereits die Zählerstruktur, die bei
grocery wieder gebraucht wurde.

---

## Lerntagebuch

`log.md` im Repo. Nach jedem Lerntag drei Zeilen: was gemacht, was unklar,
was als Nächstes. Kostet zwei Minuten und trägt durch die Tiefs.
