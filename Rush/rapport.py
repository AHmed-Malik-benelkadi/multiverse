import os

# Ouvrez un fichier de rapport en écriture
with open("rapport_ftp.txt", "w") as f:
  # Exécutez la commande who et récupérez les résultats
  connexions = os.popen("who").read()

  # Créez un dictionnaire pour stocker le nombre de connexions par utilisateur
  comptes = {}

  # Parcourez les connexions et comptez le nombre de connexions pour chaque utilisateur
  for connexion in connexions.split("\n"):
    utilisateur = connexion.split()[0]
    if utilisateur in comptes:
      comptes[utilisateur] += 1
    else:
      comptes[utilisateur] = 1

  # Écrivez les résultats dans le fichier de rapport
  f.write("Rapport des connexions\n")
  f.write("=====================\n")
  for utilisateur, nb_connexions in comptes.items():
    f.write("Utilisateur: {}\tNombre de connexions: {}\n".format(utilisateur, nb_connexions)

    print('fini')