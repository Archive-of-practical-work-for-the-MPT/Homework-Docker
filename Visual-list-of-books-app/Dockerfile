# Используем официальный образ Ubuntu с Python
FROM ubuntu:latest

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    python3-venv \
    python3-pyqt5 \
    xterm \
    xauth \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем переменные окружения для X11 и виртуального окружения
ENV DISPLAY=host.docker.internal:0
ENV PATH="/opt/venv/bin:$PATH"

# Рабочая директория приложения в контейнере
WORKDIR /app

# Создаем виртуальное окружение
RUN python3 -m venv /opt/venv

# Обновляем pip в виртуальном окружении
RUN pip install --upgrade pip

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости внутри виртуального окружения
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Запускаем терминал и BookTracker
CMD xterm -hold -e "ls -la /app; ls -la /; bash" & python main.py


# docker build -t shelf .
# docker run --rm shelf 