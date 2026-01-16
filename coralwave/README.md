# Проект на Django с УП 3 курса

## Описание

Как сделать чтобы работало?
- В setting.py настройки подключение к вашей БД
- python -m venv .venv
- .\venv\Scripts\activate
- python manage.py migrate
- python .\manage.py createsuperuser (запроси email и пароль)
- python manage.py runserver
- Открыть в браузере на localhost

Либо через Docker
- docker-compose up

Запуск locust:
- python -m venv .venv
- .\.venv\Scripts\activate
- pip install locust
- pip install faker
- locust -f locustfile.py

## Цель

1. Протестировать API Swagger через locust

## Демонстрация

<p align="center">
      <img src="https://github.com/user-attachments/assets/e5b63e1c-1224-41e5-8e3e-122574a7e99a" alt="Сайт" width="700">
</p>

## Вывод
В ходе работы проект был протестирован через locust.
