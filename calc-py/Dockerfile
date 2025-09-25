# Используем образ
FROM python:alpine

# Создаем рабочую директорию в контейнере
WORKDIR /python

# Копируем файл в контейнер
COPY calc.py .

# Запускаем 
CMD ["python", "calc.py"]

# docker build -t python-calc .                           
# docker run -it --rm python-calc