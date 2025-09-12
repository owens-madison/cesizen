#!/bin/sh

if [ -n "$POSTGRES_HOST" ]; then
  echo "Waiting for Postgres..."
  until nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 1
  done
fi

echo "Apply database migrations..."
python manage.py migrate --noinput

echo "Collect static files..."
python manage.py collectstatic --noinput

echo "Start Gunicorn..."
exec gunicorn cesizen.wsgi:application --bind 0.0.0.0:8000 --workers 3