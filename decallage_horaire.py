import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pytz

# Fuseaux horaires
timezones = {
    "France métropolitaine": "Europe/Paris",
    "Martinique": "America/Martinique",
    "Guadeloupe": "America/Guadeloupe",
    "Guyane française": "America/Cayenne"
}

# Fonction de conversion
def convertir_heure():
    try:
        heure_input = int(entry_heure.get())
        if not (0 <= heure_input <= 23):
            raise ValueError
        
        now = datetime.now()
        heure_reunion = now.replace(hour=heure_input, minute=0, second=0, microsecond=0)
        tz_reunion = pytz.timezone("Indian/Reunion")
        dt_reunion = tz_reunion.localize(heure_reunion)

        # Effacer les anciens résultats
        text_resultat.delete("1.0", tk.END)

        for lieu, tz_name in timezones.items():
            tz = pytz.timezone(tz_name)
            heure_locale = dt_reunion.astimezone(tz)
            resultat = f"{lieu} : {heure_locale.strftime('%H:%M')}\n"
            text_resultat.insert(tk.END, resultat)

    except ValueError:
        messagebox.showerror("Erreur", "Merci d'entrer une heure valide entre 0 et 23.")

# Interface
fenetre = tk.Tk()
fenetre.title("Décalage horaire depuis La Réunion")

label_instruction = tk.Label(fenetre, text="Heure à La Réunion (0-23) :")
label_instruction.pack(pady=5)

entry_heure = tk.Entry(fenetre)
entry_heure.pack(pady=5)

bouton_convertir = tk.Button(fenetre, text="Convertir", command=convertir_heure)
bouton_convertir.pack(pady=5)

text_resultat = tk.Text(fenetre, height=6, width=40)
text_resultat.pack(pady=10)

fenetre.mainloop()
