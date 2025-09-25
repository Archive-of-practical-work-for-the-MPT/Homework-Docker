# Используем образ
FROM python:alpine

# Создаем рабочую директорию в контейнере
WORKDIR /python

# Копируем файл в контейнер
COPY RockPaperScissorsGame.py .

# Запускаем 
CMD ["python", "RockPaperScissorsGame.py"]

# docker build -t python-game .                           
# docker run -it --rm python-game