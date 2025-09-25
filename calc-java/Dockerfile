# Используем образ
FROM openjdk:8-jdk-alpine

# Создаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл в контейнер
COPY calc.java .

# Компилируем файл
RUN javac calc.java

# Запускаем Java 
CMD ["java", "calc"]

# docker build -t java-calc .                           
# docker run -it  --rm java-calc