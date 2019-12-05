#!/usr/bin/env bash

# Variables
DEFAULT_USER="admin"
DEFAULT_EMAIL="admin@mail.com"
DEFAULT_PASS="pass"

python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DEFAULT_USER', '$DEFAULT_EMAIL', '$DEFAULT_PASS')" | python manage.py shell
exec "$@"