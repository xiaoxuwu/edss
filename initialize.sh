#!/bin/bash
# This script initializes the Django project. It will be executed (from
# supervisord) every time the Docker image is run.

echo "from django.contrib.auth.models import User, UserManager; um = UserManager(); um.create_superuser(username='root', email='hyun9@ucla.edu', password='pa55word') if len(User.objects.filter(username='root')) == 0 else None" | python3 src/student_showcase/manage.py shell

python3 src/student_showcase/manage.py collectstatic --noinput
python3 src/student_showcase/manage.py makemigrations
python3 src/student_showcase/manage.py makemigrations api
python3 src/student_showcase/manage.py makemigrations rest_framework
python3 src/student_showcase/manage.py migrate --noinput

echo "Starting up server on 0.0.0.0:8000"
python3 src/student_showcase/manage.py runserver 0.0.0.0:8000
