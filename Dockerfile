# Utiliser une image officielle de Python
FROM python:3.11-slim

# Définir le répertoire de travail à /app
WORKDIR /app

# Copier le fichier requirements.txt dans l'image
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code du projet
COPY . /app/

# Définir une variable d'environnement pour Django
ENV PYTHONUNBUFFERED 1

# Exposer le port 8000 pour la communication avec l'application
EXPOSE 8000

# Commande pour démarrer l'application Django avec Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "config.wsgi:application"]
