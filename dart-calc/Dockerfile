# Используем образ
FROM dart:3.9.3-sdk

# Создаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл в контейнер
COPY calc.dart .

# Запускаем 
CMD ["dart", "calc.dart"]

# docker build -t dart-calc .                           
# docker run -it --rm dart-calc