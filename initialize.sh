#!/bin/bash
# This script initializes the Django project. It will be executed (from
# supervisord) every time the Docker image is run.

echo "from django.contrib.auth.models import User; if not User.objects.all().exists(): User.create_superuser('root', 'root@localhost', password='password')" | python3 src/manage.py shell

python3 src/manage.py collectstatic --noinput
python3 src/manage.py makemigrations
python3 src/manage.py migrate --noinput

echo "Starting up server on 0.0.0.0:8000"
python3 src/manage.py runserver 0.0.0.0:8000
