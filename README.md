# Практические работы по Docker
Репозиторий с практическими работами 4 курса по внедрению и поддержки компьютерных систем на Dart и Flutter.

Навигация:

1 семестр:

1. [Практическая работа № 1 - Начало работы с Docker](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker)
2. [Практическая работа № 2 - Развертывание приложений в Docker](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/compose)
3. [Практическая работа № 3 - Развертывание приложения с обновлением данных](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/volumes-mounts)
4. [Практическая работа № 4 - Развертывание оконных приложений в Docker](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/xming11)
5. Практическая работа № 5 - Настройка мониторинга событий системы и их дальнейшая визуализация с использованием Grafana
6. [Практическая работа № 6 - Настройка отслеживания базы данных с помощью локально развернутой в Docker Grafana](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/localgrafana)
7. [Практическая работа № 7 - Отслеживания метирик с собственного приложения](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/metricscustom)
8. Практическая работа № 8 - Настройка мониторинга событий
9. [Практическая работа № 9 - Работа с InfluxDB](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/influxdb)

Доп: [Практическая работа № Дополнительная - Развернуть WPF приложение внутри Docker контейнера](https://github.com/Archive-of-practical-work-for-the-MPT/WPF-Docker-Example)

2 семестр:

10. [Практическая работа №10 Нагрузочное тестирование приложения c фейковыми данными](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/locust)


# Практическая работа № 1 - Начало работы с Docker

## Описание

Как сделать чтобы работало?
- Запустите Docker Desktop
- В каждой папке есть Dockerfile, где снизу есть две закомментированные строчки, которые нужно поочередно вводить в терминал, что сбилдить и запустить контейнерэ
- Укажите правильный путь до Dockerfile или передите в нужную папку перед тем как вводить команды
  
## Цель

1. Выполнить сборки и развертывание контейнеров из примера, и описать своими словами то, что именно вы сделали и как.
2. Описать вкладки в Docker (включая вкладки внутри собранного образа и контейнера)
3. Написать свои Doсkerfile и собрать контейнеры с программами из архива. 
4. Залить готовую практическую ( все программы + Dockerfile к каждой из них) на Gitlab или Github и прикрепить к заданию ссылку.
Описать по всем пунктам со скриншотами, оформить в отчет. Все также, как и всегда - в ЕДИНОМ файле с ОГЛАВЛЕНИЕМ. Также не забываем о том, что в любом отчете есть Цель работы и вывод.

## Демонстрация

<p align="center">
      <img src="https://github.com/user-attachments/assets/4907e36a-1f41-486a-a040-0d6b52e86f72" alt="Демонстрация" width="700">
</p>

## Вывод
Были созданы несколько Dockerfile, которые запускуют различные приложения.
