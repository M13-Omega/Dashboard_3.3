#Projekt Dashboard im Modul Objektorientierte Programmierung mit Python

# Teil 1
import tkinter as tk  # Bibliothek für GUI
from tkinter import ttk, messagebox  # Zusätzliche Widgets für Tkinter
import matplotlib.pyplot as plt  # Bibliothek für das Erstellen von Diagrammen
import random  # Zufallszahlen für die Farben der Diagramme
from datetime import datetime  # Bibliothek für Datumsoperationen
import os  # Betriebssysteminteraktionen

# Definieren der Semester und Festlegen der Modulnamen für jedes Semester
semester = {
    "Semester 1": [
        {"Name": "Artificial Intelligence", "Note": "", "Credits": 5},
        {"Name": "Einführung in das wissenschaftliche Arbeiten", "Note": "", "Credits": 5},
        {"Name": "Einführung in die Programmierung mit Python", "Note": "", "Credits": 5},
        {"Name": "Mathematik: Analysis", "Note": "", "Credits": 5},
        {"Name": "Kollaboratives Arbeiten", "Note": "", "Credits": 5},
        {"Name": "Statistik - Wahrscheinlichkeit und deskriptive Statistik", "Note": "", "Credits": 5}
    ],
    "Semester 2": [
        {"Name": "Objektorientierte und funktionale Programmierung mit Python", "Note": "", "Credits": 5},
        {"Name": "Mathematik: Lineare Algebra", "Note": "", "Credits": 5},
        {"Name": "Interkulturelle und ethische Handlungskompetenzen", "Note": "", "Credits": 5},
        {"Name": "Statistik - Schließende Statistik", "Note": "", "Credits": 5},
        {"Name": "Cloud Computing", "Note": "", "Credits": 5},
        {"Name": "Cloud Programming", "Note": "", "Credits": 5}
    ],
    "Semester 3": [
        {"Name": "Maschinelles Lernen - Supervised Learning", "Note": "", "Credits": 5},
        {"Name": "Maschinelles Lernen - Unsupervised Learning", "Note": "", "Credits": 5},
        {"Name": "Einführung Computer Vision", "Note": "", "Credits": 5},
        {"Name": "Einführung Reinforcement Learning", "Note": "", "Credits": 5},
        {"Name": "Projekt: Computer Vision", "Note": "", "Credits": 5},
        {"Name": "Neuronale Netze und Deep Learning", "Note": "", "Credits": 5}
    ],
    "Semester 4": [
        {"Name": "Einführung in NLP", "Note": "", "Credits": 5},
        {"Name": "Projekt: NLP", "Note": "", "Credits": 5},
        {"Name": "Data Science", "Note": "", "Credits": 5},
        {"Name": "Projekt: Vom Modell zum Produktvertrieb", "Note": "", "Credits": 5},
        {"Name": "Einführung in Datenschutz und IT-Sicherheit", "Note": "", "Credits": 5},
        {"Name": "Seminar. Ethische Fragen der Data Science", "Note": "", "Credits": 5}
    ],
    "Semester 5": [
        {"Name": "User Experience", "Note": "", "Credits": 5},
        {"Name": "UX-Projekt", "Note": "", "Credits": 5},
        {"Name": "Projekt: Edge AI", "Note": "", "Credits": 5},
        {"Name": "Einführung in die Robotik", "Note": "", "Credits": 5},
        {"Name": "Projekt: Agiles Projektmanagement", "Note": "", "Credits": 5},
        {"Name": "Robotik und Automatisierung", "Note": "", "Credits": 5}
    ],
    "Semester 6": [
        {"Name": "Bachelorarbeit", "Note": "", "Credits":10 },
        {"Name": "Wahlpflichtmodul A", "Note": "", "Credits": 10},
        {"Name": "Wahlpflichtmodul B ", "Note": "", "Credits": 10},
        {"Name": "Wahlpflichtmodul C", "Note": "", "Credits": 10},
    ]
}

#Teil 2
# Funktion zum Berechnen der abgeschlossene Semester
def abgeschlossene_semester():
    start_date = datetime(2024, 1, 1)  # Startdatum des Studiums
    current_date = datetime.now()  # Aktuelles Datum
    # Berechnen der Anzahl der Monate und Umrechnen in Semester (6 Monate pro Semester)
    semester_dauer = (current_date - start_date).days // 30 // 6
    return semester_dauer
# Funktion zum Berechnen der verbleibenden Semester
def verbleibende_semester():
    total_program_semesters = 6
    completed_semesters = abgeschlossene_semester()
    return total_program_semesters - completed_semesters if completed_semesters < total_program_semesters else 0

# Funktion zum Berechnen des Notendurchschnitts
def noten_durchschnitt(semester):
    total_credits = 0 #Initialisierung der neuen Variable mit Wert 0
    total_grades = 0 #Initialisierung der neuen Variable mit Wert 0
    for modules in semester.values(): #Schleife durch die Werte im Dictionary 'semester'
        for modul in modules: #Schleife durch jedes Modul in den aktuellen Modulen
            if modul['Note'] != '': #Überprüft das Eingabenfeld von der Note zum Modul auf Eintrag
                total_credits += int(modul['Credits']) #Summiert die Gesamtanzahl der Creditpoints
                total_grades += float(modul['Note']) * int(modul['Credits']) #Für die gewichtete Berechnung: Multiplikation von Modulnote mal Modulcredits
    return total_grades / total_credits if total_credits != 0 else 0 #Berechnet den gewichteten Notendurchschnitt durch teilen durch Gesamtanzahl Credits

# Funktion zum Erstellen der Tortendiagramme
def create_pie_charts(semester_data):
    fig, axs = plt.subplots(2, 3, figsize=(15, 10)) #Erstellung einer 2x3-Anordnung der 6 Tortendiagramme, Größe Gesamtabbildung
    axs = axs.flatten()
    for idx, (sem, modules) in enumerate(semester_data.items()): #Durchläuft Semester und jeweilige Module
        labels = [] #Liste, um Modulnamen zu speichern
        sizes = [] #Liste, um Größenanteile Module abhängig von Credits zu speichern
        colors = [] #Liste für Modulfarben im Tortendiagramm
        legend_labels = [] #Liste für die Labels in der Legende
        for module in modules:
            labels.append(module["Name"]) #Hinzufügen der Modulnamens in Liste
            legend_labels.append(module["Name"]) #Hinzufügen des Modulnamens in Legende
            if module["Note"]: #Überprüft Eintragung einer Note je Modul
                sizes.append(int(module["Credits"])) #Fügt Credits zur Dimensinierung dem Modul hinzu
                colors.append("#{0:06x}".format(random.randint(0, 0xFFFFFF))) #Fügt zufällige Farbe den Modul mit Note zu
            else:
                sizes.append(30 / len(modules)) #Alternative, falls keine Credits eingetragen werden
                colors.append("grey") #Grau als Farbe zur Liste hinzufügen
        axs[idx].pie(sizes, colors=colors, startangle=90, autopct='%1.1f%%') #Erstellung Tortendiagramme
        axs[idx].axis('equal')
        axs[idx].set_title(f'{sem}')
        axs[idx].legend(legend_labels, loc='upper right', bbox_to_anchor=(0,1,1,0)) #Legende zum Tortendiagramm und Positionierung
    plt.tight_layout()
    plt.show()

# Funktion zum Speichern der Daten in einer Textdatei
def save_data(semester_data):
    with open(os.path.join(os.path.expanduser("~"), "Desktop", "studium_fortschritt.txt"), "w") as file: #Festlegung Speicherort und Dateiname
        for sem, modules in semester_data.items():
            file.write(f"{sem}\n")
            for module in modules:
                file.write(f"{module['Name']},{module['Note']},{module['Credits']}\n") #Dateiinformationen

# Funktion zum Laden der Daten aus einer Textdatei
def load_data():
    semester_data = semester.copy()
    try:
        with open(os.path.join(os.path.expanduser("~"), "Desktop", "studium_fortschritt.txt"), "r") as file:
            current_sem = ""
            for line in file:
                if line.startswith("Semester"):
                    current_sem = line.strip()
                else:
                    values = line.strip().split(",")
                    if len(values) == 3:  # Überprüfen, ob die Zeile genau 3 Werte enthält
                        name, note, credits = values
                        for module in semester_data[current_sem]:
                            if module["Name"] == name:
                                module["Note"] = note
                                module["Credits"] = credits
                    else:
                        print(f"Zeile hat unerwartete Anzahl von Werten: {line}")
    except FileNotFoundError:
        pass
    return semester_data

#Teil 3
# Erstellen des GUI mit Tkinter

class StudiumFortschrittApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Titel für erstes Fenster
        self.title("Fortschritt Studium")

        semester_data = load_data()
        remaining_semesters = verbleibende_semester()
        average_grade = noten_durchschnitt(semester_data)
        elapsed_time = (datetime.now() - datetime(2024, 1, 1)).days # Startdatum Studium

        # Angezeigen von "verbleibende Semester", "Durchschnittsnote" und "vergangene Zeit"
        info_label = tk.Label(self, text=f"Verbleibende Semester: {remaining_semesters}, Durchschnittsnote: {average_grade:.2f}, "
                                         f"Vergangene Zeit: {elapsed_time // 365} Jahre, {elapsed_time % 365 // 30} Monate, "
                                         f"{elapsed_time % 30} Tage")
        info_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Hinzufügen der Module und Eingabemöglichkeiten
        self.entries = {}
        for idx, (sem, modules) in enumerate(semester_data.items()):
            frame = ttk.Frame(self) #Erstellung Frame Widget für jedes der sechs Semester
            frame.grid(row=(idx // 3) + 1, column=(idx % 3), padx=10, pady=10) #Position Frame im Rasterlayout, 3 Frames pro Zeile

            ttk.Label(frame, text=sem).grid(row=0, column=0, columnspan=3) #Erstellung und Positionierung von Label im Frame von Semester
            headers = ["Modul", "Note", "Credits"] #Definition Liste für Zeilenüberschriften für Tabellen

            for col, header in enumerate(headers): #Durchlaufen Kopfzeilenliste
                ttk.Label(frame, text=header).grid(row=1, column=col, sticky=tk.W) #Erstellung und Positionierung Kopfzeilen

            for i, module in enumerate(modules, start=2): #Durchläuft Module aktuelles Semester (Beginn zweite Zeile)
                ttk.Label(frame, text=module["Name"]).grid(row=i, column=0, sticky=tk.W) #Erstellen und positionieren von Label Modulnamen
                note_entry = ttk.Entry(frame) #Erstellt Eingabefeld für Modulnote
                note_entry.insert(0, module["Note"]) #Setzt Modulnote in Eingabefeld ein
                note_entry.grid(row=i, column=1) #Positioniert Eingabefeld für Note im Frame
                credits_entry = ttk.Entry(frame) #Erstellt Eingabefeld für Credits
                credits_entry.insert(0, module["Credits"]) #Setzt Credits ins Eingabefeld ein
                credits_entry.grid(row=i, column=2) #Positioniert Eingabefeld im Frame
                self.entries[(sem, module["Name"], "Note")] = note_entry #Speichert Eingabefeld Note in entries Dictionary
                self.entries[(sem, module["Name"], "Credits")] = credits_entry #Speichert Eingabefeld Credits in entries Dictionary

        # Erstellung von Button "Speichern"
        save_button = ttk.Button(self, text="Speichern", command=self.save_data) #Erstellung Button, aktiv durch Anklicken
        save_button.grid(row=4, column=1, pady=10) #Positionierung des Buttons im Rasterlayout

        # Erstellung von Button "Tortendiagramm erstellen"
        pie_button = ttk.Button(self, text="Tortendiagramm erstellen", command=lambda: create_pie_charts(semester_data)) #Erstellung Button, aktiv durch Anklicken
        pie_button.grid(row=5, column=1, pady=10) #Positionierung des Buttons im Rasterlayout

    def save_data(self):
        for (sem, module_name, field), entry in self.entries.items(): #Durchlaufen der gespeicherten Eingabefelder im entries dictionary
            for module in semester[sem]: #Durchlaufen Module im entsprechenden Semester
                if module["Name"] == module_name: #Prüfung Modulname
                    module[field] = entry.get() #Einsetzen von Wert aus Eingabefeld in Modul
        save_data(semester) #Ruft die save_data Funktion auf und speichert die Daten

if __name__ == "__main__": #Überprüfung, ob Skript direkt ausgeführt wird
    app = StudiumFortschrittApp() #Erstellung StudiumFortschrittApp Klasse
    app.mainloop() #Start der App