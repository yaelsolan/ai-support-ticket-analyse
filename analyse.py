# analyse.py
# Dieses Skript analysiert Kundenanfragen und erstellt automatische Antworten.

import pandas as pd
import matplotlib.pyplot as plt

# CSV-Datei einlesen (mit Trennzeichen Semikolon, wenn notwendig anpassen)
df = pd.read_csv("output.csv")

# Spalten anzeigen
print("Spaltennamen im DataFrame:")
print(df.columns)

# Anzahl der Tickets pro Kategorie zählen
kategorie_counts = df['Kategorie'].value_counts()
print("Anzahl der Tickets pro Kategorie:")
print(kategorie_counts)

# Anzahl der Tickets pro Priorität zählen
prioritaet_counts = df['Priorität'].value_counts()
print("Anzahl der Tickets pro Priorität:")
print(prioritaet_counts)

# Diagramm: Tickets pro Kategorie
plt.figure(figsize=(10, 6))
kategorie_counts.plot(kind='bar')
plt.title("Anzahl der Tickets pro Kategorie")
plt.xlabel("Kategorie")
plt.ylabel("Anzahl")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("tickets_pro_kategorie.png")
plt.show()

# Diagramm: Tickets pro Priorität
plt.figure(figsize=(8, 5))
prioritaet_counts.plot(kind='bar')
plt.title("Anzahl der Tickets pro Priorität")
plt.xlabel("Priorität")
plt.ylabel("Anzahl")
plt.tight_layout()
plt.savefig("tickets_pro_prioritaet.png")
plt.show()

# KI-generierte Antworten (simuliert)
def generiere_antwort(nachricht):
    if "Drucker" in nachricht:
        return "Bitte prüfen Sie den Anschluss des Druckers und starten Sie ihn ggf. neu."
    elif "System" in nachricht or "einloggen" in nachricht:
        return "Bitte überprüfen Sie Ihren Benutzernamen und Ihr Passwort."
    elif "Internet" in nachricht:
        return "Wir analysieren gerade die Netzwerkauslastung. Bitte haben Sie einen Moment Geduld."
    elif "Bildschirm" in nachricht:
        return "Bitte überprüfen Sie die Kabelverbindungen und starten Sie den PC neu."
    else:
        return "Ihre Anfrage wurde weitergeleitet. Wir melden uns schnellstmöglich."

# Neue Spalte mit KI-Antworten erzeugen
df['KI-Antwort-NEU'] = df['Nachricht'].apply(generiere_antwort)

# Neue Datei speichern mit KI-Antworten
df.to_csv("output_mit_AI.csv", index=False)

print("KI-Antworten (neu generiert):")
print(df[['Nachricht', 'KI-Antwort-NEU']].head())
