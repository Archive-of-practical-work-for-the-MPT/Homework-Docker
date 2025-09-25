# Используем образ
FROM openjdk:8-jdk-alpine

# Создаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл в контейнер
COPY game.java .

# Компилируем файл
RUN javac game.java

# Запускаем Java 
CMD ["java", "game"]

# docker build -t java-game .                           
# docker run -it  --rm java-game