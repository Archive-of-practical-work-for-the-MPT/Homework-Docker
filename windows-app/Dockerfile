# Используем базовый образ Ubuntu
FROM ubuntu:latest

# Устанавливаем необходимые пакеты: Java, X11 и xauth
RUN apt-get update && apt-get install -y \
    openjdk-11-jre \
    x11-apps \
    xauth \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем переменную окружения DISPLAY для X11
ENV DISPLAY=host.docker.internal:0

# Копируем файл calc.jar в контейнер
COPY calc.jar .

# Указываем команду для запуска JAR-файла
CMD ["java", "-jar", "calc.jar"]

# docker build -t calc-p1 .
# docker run --rm calc-p1 