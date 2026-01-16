FROM python:3.11-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Создание рабочей директории
WORKDIR /app

# Копирование requirements и установка Python зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода приложения
COPY coralwave/ ./coralwave/

# Создание директории для статических файлов
RUN mkdir -p /app/coralwave/staticfiles

# Сбор статических файлов
RUN python coralwave/manage.py collectstatic --noinput --verbosity=0 || true

# Открытие порта
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "coralwave/manage.py", "runserver", "0.0.0.0:8000"]