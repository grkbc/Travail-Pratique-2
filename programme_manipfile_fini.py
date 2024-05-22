import json
import csv


#Lire fichier json
with open('data.json',) as f:
    nbm = json.load(f)

# Écrire chaque nombre dans un fichier CSV
with open('nombre_du_fichier_json.csv', 'w', newline='') as csvfile:
    csv = csv.writer(csvfile)
    csv.writerow(['reel','imaginaire'])
    for nombre in nbm:
        csv.writerow([nombre['reel'],nombre['imaginaire']])