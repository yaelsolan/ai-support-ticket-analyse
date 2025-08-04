#  AI Support Ticket Analyse

Dieses Projekt simuliert die Analyse von IT-Supportanfragen in einem Unternehmen aus der Telekommunikations- oder Gesundheitsbranche. 

Ziel ist es, eingehende Nachrichten automatisch zu kategorisieren, die Priorität zu analysieren und eine passende KI-Antwort zu generieren.

## 🔍 Funktionen

- Einlesen von Support-Tickets aus einer CSV-Datei
- Analyse der Anzahl der Anfragen pro Kategorie und Priorität
- Visualisierung der Ergebnisse mit Balkendiagrammen
- Automatische Beantwortung typischer Support-Anfragen mit einer einfachen KI-Logik
- Export der Ergebnisse in eine neue CSV-Datei

## 🧠 Beispielhafte KI-Antworten

Das Programm durchsucht jede Nachricht nach Schlüsselwörtern und generiert dazu eine passende Standardantwort.

Beispiel:

> Nachricht: „Ich kann mich nicht mehr in das System einloggen.“  
> KI-Antwort: „Bitte überprüfen Sie Ihren Benutzernamen und Ihr Passwort.“

## 📁 Dateien im Projekt

- `analyse.py` – Hauptskript zur Analyse und Visualisierung
- `output.csv` – Beispieldaten mit Support-Anfragen
- `output_mit_AI.csv` – Ergebnisdatei mit KI-Antworten
- `tickets_pro_kategorie.png` – Diagramm der Anfragen pro Kategorie
- `tickets_pro_prioritaet.png` – Diagramm der Anfragen pro Priorität

## 🛠️ Verwendete Technologien

- Python
- Pandas
- Matplotlib

## 📌 Zielgruppe

Dieses Projekt richtet sich an Einsteiger:innen im IT-Support oder Datenanalyse, die zeigen möchten, wie einfache Automatisierung im Support-Alltag aussehen kann.

---

