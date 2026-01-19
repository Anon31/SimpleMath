# Utiliser une image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers sources dans le conteneur
COPY simple_math.py .
COPY test_simple_math.py .

# Commande exécutée au démarrage du conteneur (Étape 7)
# Lance automatiquement les tests unitaires
CMD ["python", "-m", "unittest", "test_simple_math.py"]