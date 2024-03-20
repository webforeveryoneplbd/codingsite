import zipfile
import os
import pandas as pd
import matplotlib.pyplot as plt

# Chemin vers le fichier ZIP de votre base de données
zip_file_path = 'C:\Users\Lenovo\Downloads.zip'

# Répertoire de destination pour extraire les fichiers
extract_to_directory = 'C:\Users\Lenovo\Downloads'

# Création du répertoire de destination s'il n'existe pas
os.makedirs(extract_to_directory, exist_ok=True)

# Extraction des fichiers de l'archive ZIP
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_directory)

print("Extraction des fichiers terminée.")

# Sélection du fichier de données à visualiser (à adapter en fonction de votre structure)
data_file_path = os.path.join(extract_to_directory, 'nom_du_fichier_de_donnees.csv')

# Lecture des données depuis le fichier CSV dans un DataFrame Pandas
df = pd.read_csv(data_file_path)

# Affichage des premières lignes du DataFrame
print(df.head())

# Visualisation des données
plt.figure(figsize=(10, 6))
df['column_name'].value_counts().plot(kind='bar')
plt.title('Distribution des données')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.show()

