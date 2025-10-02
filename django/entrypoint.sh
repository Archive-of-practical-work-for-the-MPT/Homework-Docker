#!/bin/bash

# Выполнить миграции
python manage.py makemigrations --noinput

# Применить миграции
python manage.py migrate --noinput

# Запустить сервер разработки
python manage.py runserver 0.0.0.0:8000
