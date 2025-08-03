#!/bin/bash
set -e

# Aplica migrações
python3 manage.py makemigrations
python3 manage.py migrate
echo "Migrations Done!"

# Cria superusuário se não existir
python3 manage.py shell -c "\
from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@admin.com', 'admin')"
echo "Superuser 'admin' was created!"

# Inicia o servidor
python manage.py runserver 0.0.0.0:8000