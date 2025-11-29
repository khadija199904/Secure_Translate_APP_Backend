#  Plateforme de Traduction Sécurisée (Backend)

Ce projet est une application complète comprenant une API Backend (FastAPI), une Base de données (PostgreSQL) et un Frontend (Next.js). L'application permet de traduire du texte (FR ↔ EN) en utilisant l'API d'inférence de Hugging Face, le tout sécurisé par une authentification JWT.

## Table des matières

- [Architecture](#-architecture)
- [Prérequis](#-prérequis)
- [Installation & Démarrage](#-installation--démarrage)
- [Configuration (.env)](#-configuration-env)
- [Documentation API](#-documentation-api)
- [Tests (Postman & Unitaires & Client)](#-tests)
- [Structure du Projet](#-structure-du-projet)

---

## Architecture
L'application est composée de trois services orchestrés par Docker :

1.**Frontend** (React.js) : Interface utilisateur pour le login/Registre et la traduction.
2.**Backend** (FastAPI) : API REST qui gère la logique métier, la sécurité et les appels externes.
3.**Base de Données** (PostgreSQL) : Stockage persistant des utilisateurs et de leurs mots de passe hachés.

### Schéma technique

```mermaid
graph TD
    graph LR
    subgraph "Docker Network"
        direction TB
        API[ Backend FastAPI]
        DB[(PostgreSQL)]
        API -- "SQL (Auth)" --> DB
    end

    Client[💻 Client / Frontend] -- "1. Login (JSON)" --> API
    API -- "2. JWT Token" --> Client
    Client -- "3. Translate + Token" --> API
    
    API -- "4. Inférence HTTPS" --> HF[Hugging Face API]
    HF -- "5. Traduction" --> API
```
 **-Workflow d'Authentification & Traduction**
1.Login : L'utilisateur envoie ses identifiants (username, password).
2.JWT : Le backend vérifie le hash dans PostgreSQL et renvoie un access_token.
3.Requête Protégée : L'utilisateur appelle /translate avec le header Authorization: Bearer <TOKEN>.
4.Traduction :
    - Le backend valide le token.
    - Il appelle l'API Hugging Face.
    - Il retourne la traduction JSON.

## Prérequis
- Docker et Docker Compose installés sur votre machine.
- Un compte Hugging Face pour obtenir un Token d'accès (User Access Token) en lecture ("Read").

## Installation & Démarrage

L'application est conteneurisée. Utilisez Docker Compose pour lancer le Backend, le Frontend et la Base de données simultanément.
  1.Cloner le projet et aller dans le dossier.
  2.Lancer les services :
```bash
docker-compose up --build
```

- Le Backend sera accessible sur : http://localhost:8000
- Le Frontend sera accessible sur : http://localhost:5173/
- La DB sera sur le port 5432.
Note : Au premier lancement, la table users est créée automatiquement.

## Configuration (.env)
Créez un fichier .env à la racine du projet (au même niveau que docker-compose.yml) et configurez les variables suivant:
```
# --- Base de données PostgreSQL ---
POSTGRES_USER=admin_user
POSTGRES_PASSWORD=admin_password
POSTGRES_DB=translation_db
# URL de connexion pour SQLAlchemy (Note: le host est le nom du service docker 'db')
DATABASE_URL=postgresql://admin_user:admin_password@db:5432/translation_db

# --- Sécurité (JWT) ---

SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f

# --- Hugging Face API ---
# Votre token commence par "hf_..."
HF_API_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```



