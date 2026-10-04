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

## Wochenrhythmus (8–10 Std.)

| Tag | Zeit | Inhalt |
|---|---|---|
| Mo–Do | 1–2 Std. an 2–3 Abenden | Videolektion, kleine Übungen |
| Fr | frei | Puffertag — bewusst nichts |
| Sa | 3–4 Std. | Problem Set, am Stück |
| So | 2 Std. | Rest, Wiederholung, Lerntagebuch |

Zwei Regeln: An jedem Lerntag mindestens ein Commit. Und den Freitag wirklich
freihalten — der Plan läuft über Monate.

**Wenn eine Woche ausfällt:** nicht nachholen, nicht verdoppeln. Da
weitermachen, wo du aufgehört hast. Aufgeben passiert fast nie wegen zu wenig
Zeit, sondern wegen der Schuldgefühle nach einer verpassten Woche. Das hat im
September schon einmal funktioniert.

---

## Phase 1 — CS50P fertig (Oktober bis Mitte Dezember)

Eine CS50P-Woche pro Kalenderwoche. Stand 04.10.: Woche 0–2 durch,
Problem Set 2 offen.

| Zeitraum | Inhalt |
|---|---|
| 05.–11.10. | Problem Set 2, dann Woche 3 (Exceptions) |
| 12.–18.10. | Problem Set 3, Woche 4 (Libraries) |
| 19.–25.10. | Problem Set 4 |
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

> **Meilenstein 2 (Mitte Dezember):** CS50P komplett, neun Problem Sets und
> ein Abschlussprojekt im öffentlichen Repo.

**Zertifikat:** Am 10.10. kommt die Erinnerung, ob du die Einreichung bei
CS50 nachholen willst. Entscheidung dann, nicht vorher.

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
- Repo aufräumen: README mit Screenshots, saubere Commit-Historie
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

## Was bisher stimmt (Stand 04.10.2026)

Drei Wochen, und das hier läuft besser als der Plan vorsah:

- Problem Set 0 und 1 vollständig selbst gelöst, zehn Programme
- Nach fünf Tagen Zwangspause ohne Murren weitergemacht
- Lerntagebuch und Commits konsequent geführt
- Fragen nach dem Warum statt nach der Lösung

Das Tempo hinkt, die Gewohnheiten stimmen. Das ist die Reihenfolge, in der
man es haben will — Tempo lässt sich korrigieren, Gewohnheiten nicht.

---

## Lerntagebuch

`log.md` im Repo. Nach jedem Lerntag drei Zeilen: was gemacht, was unklar,
was als Nächstes. Kostet zwei Minuten und trägt durch die Tiefs.
