#!/bin/bash

cd /app/greenquality

echo "Ждем готовности базы данных..."
while ! pg_isready -h db -p 5432 -U postgres > /dev/null 2> /dev/null; do
    sleep 1
done
echo "База данных готова."

# Миграции (если нужно)
# python manage.py makemigrations --noinput
# python manage.py migrate --

python manage.py runserver 0.0.0.0:8000