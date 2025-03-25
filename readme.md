# 🚀 Projet Django avec Docker et GitHub Actions

## 📌 Description
Ce projet est une application Django utilisant PostgreSQL et pgAdmin, entièrement conteneurisée avec Docker. Il inclut une pipeline CI/CD via GitHub Actions.

## 🛠️ Technologies utilisées
- **Django** (Backend web)
- **PostgreSQL** (Base de données)
- **pgAdmin** (Gestionnaire PostgreSQL)
- **Docker & Docker Compose** (Conteneurisation)
- **Gunicorn** (Serveur WSGI)
- **GitHub Actions** (CI/CD)

---

## 🚀 Installation & Lancement

### 🔹 Prérequis
Assurez-vous d'avoir installé :
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 🔹 Cloner le projet
```bash
git clone https://github.com/ton-utilisateur/ton-projet.git
cd ton-projet
```

### 🔹 Configurer les variables d'environnement
Créer un fichier `.env` à la racine avec :
```ini
DEBUG=True
DATABASE_URL=postgres://postgres:password@db:5432/rent-api
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=rent-api
PGADMIN_DEFAULT_EMAIL=test@example.com
PGADMIN_DEFAULT_PASSWORD=pgadminpass
```

### 🔹 Démarrer les conteneurs
```bash
docker compose up --build
```

L’application sera disponible sur : `http://localhost:8000`

**Accès à pgAdmin** : `http://localhost:5050` (Email/Mot de passe définis dans `.env`)

---

## 🏗️ Pipeline GitHub Actions
Le projet inclut une pipeline CI/CD qui :
✅ **Build l’image Docker**
✅ **Gère plusieurs environnements (`develop`, `staging`, `main`)**

### 🔹 Secrets GitHub à configurer
Dans **Settings > Secrets and variables > Actions**, ajoutez :
| Nom | Valeur |
|------|--------|
| `DEBUG` | `True` |
| `DATABASE_URL` | `postgres://postgres:password@db:5432/rent-api` |
| `POSTGRES_USER` | `postgres` |
| `POSTGRES_PASSWORD` | `password` |
| `POSTGRES_DB` | `rent-api` |
| `PGADMIN_DEFAULT_EMAIL` | `test@example.com` |
| `PGADMIN_DEFAULT_PASSWORD` | `pgadminpass` |

---
