# Cesizen

Une application accessible et innovante pour la gestion du stress et la sensibilisation à la santé mentale.  
Technologies principales : Python 3.12.1, Django 5.2, PostgreSQL, Docker, Render.

# Environnement et configuration
Variables d'environnement nécessaires

SECRET_KEY=<clef_secrète>

DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,cesizen-web.onrender.com

DEBUG=True

DATABASE_URL=<url_postgresql_render>

SECRET_KEY : clé secrète Django pour la sécurité.

DJANGO_ALLOWED_HOSTS : les domaines autorisés pour Django.

DEBUG : True pour le développement, False en production.

DATABASE_URL : URL de connexion PostgreSQL sur Render (ex: postgres://user:password@host:port/dbname).

# Docker
Docker est utile pour reproduire exactement l’environnement de développement et de production. Les commandes principales :

1. Démarrer les containers localement
docker compose up

2. Créer un superuser pour tester l'administration
docker compose run web python manage.py createsuperuser

3. Appliquer les migrations dans Docker
docker compose run web python manage.py migrate
Note : Pour Render, le déploiement se fait automatiquement après un git push. Docker est donc principalement utile pour le développement local ou pour que d'autres développeurs puissent cloner et lancer l'environnement identique.

# Base de données
Localement : SQLite (fichier db.sqlite3)
Production : PostgreSQL sur Render
Commandes utiles :
python manage.py makemigrations
python manage.py migrate

# Lancer l'application
Localement (via Docker) : docker compose up
Localement sans Docker :
python manage.py runserver
Sur Render : automatiquement après git push main

# Versioning
Git est utilisé pour versionner le projet.
GitHub Actions sera utilisé pour intégrer tests et déploiement continu (CI/CD).
