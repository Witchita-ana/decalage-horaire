# 🕒 Calculateur de Décalage Horaire – Heure de La Réunion

Ce petit programme Python permet de convertir une heure donnée à **La Réunion** vers l'heure locale de plusieurs territoires français d'outre-mer : **France métropolitaine**, **Martinique**, **Guadeloupe** et **Guyane française**.
Remarques
Ce projet est une démonstration pédagogique.
Il utilise l'heure système de l'ordinateur pour fixer la date du jour.   

## 🌍 Objectif

Vous entrez une heure (0 à 23) correspondant à l'heure actuelle à La Réunion, et l'application affiche automatiquement l'heure correspondante dans les autres régions sélectionnées.

## 🛠️ Technologies utilisées

- `tkinter` pour l'interface graphique
- `pytz` pour la gestion des fuseaux horaires
- `datetime` pour la manipulation des heures

## 📸 Aperçu

L'utilisateur entre une heure dans un champ prévu, puis clique sur **Convertir**. Le programme affiche ensuite les heures locales pour les régions suivantes :

- France métropolitaine 🇫🇷
- Martinique 🇲🇶
- Guadeloupe 🇬🇵
- Guyane française 🇬🇫

## ▶️ Lancer le programme

1. Assurez-vous d'avoir Python installé.
2. Installez `pytz` si nécessaire :
   ```bash
   pip install pytz
3. Lancez le fichier :
   python decallage_horaire.py






