# Lernplan Monate 1–3 — Python-Fundament
**Start: Samstag, 12.09.2026 · Ziel: Entwicklerstelle in 1–2 Jahren, Schwerpunkt Bau-/TGA-Software**

---

## Wochenrhythmus (16 Std./Woche)

| Tag | Zeit | Inhalt |
|---|---|---|
| Mo–Do | 2 Std. abends | Kurslektion + Übungsaufgaben |
| Fr | frei | Pufferttag – bewusst nichts |
| Sa | 5 Std. (2× 2,5 Std.) | Projektarbeit am Stück |
| So | 3 Std. | Wiederholung, kleine Aufgaben, Lerntagebuch |

**Zwei Regeln:** Jeden Lerntag mindestens ein Commit auf GitHub. Und den Freitag wirklich freihalten — der Plan läuft 18 Monate, nicht 6 Wochen.

---

## Werkzeuge (einmalig einrichten, Tag 1)

- Python (aktuelle Version von python.org)
- VS Code + Erweiterungen „Python" und „Pylance"
- Git für Windows
- GitHub-Konto (Klarname oder klarer Nutzername — das wird später dein Bewerbungsportfolio)

---

## Ressourcen

| Zweck | Ressource | Kosten |
|---|---|---|
| Hauptkurs | CS50P – „Introduction to Programming with Python" (Harvard, edX/YouTube) | kostenlos |
| Praxisbuch | „Automate the Boring Stuff with Python" (Al Sweigart), online lesbar | kostenlos |
| Tägliche Übungen | Exercism – Python Track | kostenlos |
| Git verstehen | „Learn Git Branching" (interaktiv) + Pro Git (Buch, online) | kostenlos |
| SQL | SQLBolt, danach PostgreSQL lokal installieren | kostenlos |

Alles auf Englisch. Das ist kein Umweg, sondern Teil des Jobs — Dokumentation, Fehlermeldungen und Stellenausschreibungen sind englisch.

---

## Monat 1 — Grundlagen (KW 12.09. – 09.10.)

**Woche 1 (12.–18.09.)**
- Sa: Werkzeuge einrichten, erstes Repo `lernprojekte` anlegen, erster Commit. Danach CS50P Woche 0.
- Mo–Do: CS50P Woche 1 (Bedingungen), Aufgaben lösen
- So: Exercism – 3 einfache Aufgaben

**Woche 2 (19.–25.09.)**
- Schleifen, Funktionen (CS50P Woche 2–3)
- Sa: Kleines Skript — Rohrlängen aus einer Liste summieren, Ergebnis formatiert ausgeben

**Woche 3 (26.09.–02.10.)**
- Ausnahmebehandlung, Bibliotheken (CS50P Woche 4)
- Sa: Skript liest eine echte Excel-Datei aus deinem Arbeitsalltag ein (`openpyxl`) und zählt/summiert Positionen

**Woche 4 (03.–09.10.)**
- Git richtig: Branch, Merge, Pull Request am eigenen Repo üben
- Sa: **Meilenstein 1** — Repo mit sauberem README, 4 Skripten, mind. 20 Commits

> **Meilenstein 1:** Du kannst eine Excel-Liste einlesen, verarbeiten und ein Ergebnis ausgeben — ohne Anleitung nebenbei.

---

## Monat 2 — Vom Skript zum Werkzeug (10.10. – 06.11.)

**Woche 5 (10.–16.10.)** — Datenstrukturen: Listen, Dictionaries, Mengen. Übungen bis es sitzt.
**Woche 6 (17.–23.10.)** — Objektorientierung: Klassen, Methoden (CS50P Woche 8). Sa: bestehendes Skript in Klassen umbauen.
**Woche 7 (24.–30.10.)** — Tests mit `pytest`, Code sauber strukturieren (Module, virtuelle Umgebungen).
**Woche 8 (31.10.–06.11.)** — **Projekt 1 bauen:** ein Kommandozeilen-Werkzeug, das du im Job wirklich benutzt. Vorschlag: Aufmaß-Auswerter — liest mehrere Excel-Dateien, prüft auf fehlende Positionen, erzeugt eine Zusammenfassung als Excel oder PDF.

> **Meilenstein 2:** Projekt 1 läuft, hat Tests, ein README mit Screenshots und liegt öffentlich auf GitHub. Du benutzt es tatsächlich bei der Arbeit.

---

## Monat 3 — Daten und Schnittstellen (07.11. – 04.12.)

**Woche 9 (07.–13.11.)** — SQL: SELECT, JOIN, GROUP BY (SQLBolt komplett). PostgreSQL lokal installieren.
**Woche 10 (14.–20.11.)** — Python + Datenbank verbinden, Daten aus Projekt 1 in eine Datenbank schreiben.
**Woche 11 (21.–27.11.)** — HTTP und APIs verstehen: `requests`, JSON, eine öffentliche API abfragen (z. B. Wetterdaten für eine Auslegungsrechnung).
**Woche 12 (28.11.–04.12.)** — Kleine Weboberfläche mit FastAPI für Projekt 1. Danach: Rückblick schreiben, Plan für Monat 4–5 (Umstieg auf C#/.NET) festlegen.

> **Meilenstein 3:** Zwei öffentliche Repos, ~200 Commits über 12 Wochen, ein Werkzeug mit Datenbank und Weboberfläche. Damit bist du weiter als die meisten Bootcamp-Absolventen.

---

## Was danach kommt (nur zur Orientierung)

Ab Monat 4–5 Wechsel auf **C# / .NET**, weil Revit-, AutoCAD- und Allplan-Erweiterungen sowie die meisten deutschen TGA-Softwarehäuser darauf laufen. Der Umstieg kostet etwa 3–4 Wochen, weil die Denkweise dieselbe bleibt. Ab Monat 10 dann das Nischenprojekt: eine Revit-Erweiterung, die Sprinklerabstände nach Regelwerk prüft. Das ist der Bewerbungstürsteher, den fast kein Mitbewerber vorzeigen kann.

---

## Lerntagebuch

Lege im Repo eine Datei `LOG.md` an. Nach jedem Lerntag drei Zeilen: Was gemacht, was nicht verstanden, was morgen dran ist. Kostet zwei Minuten und ist bei Motivationstiefs im Januar unbezahlbar.

## Wenn eine Woche ausfällt

Nicht nachholen, nicht verdoppeln. Einfach an der Stelle weitermachen, wo du aufgehört hast. Aufgeben passiert fast nie wegen zu wenig Zeit, sondern wegen der Schuldgefühle nach einer verpassten Woche.
