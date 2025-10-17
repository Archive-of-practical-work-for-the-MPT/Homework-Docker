# Практическая работа № 3 - Развертывание приложения с обновлением данных

## Описание

В данной практической учимся использовать Bind Mount и Volume.

## Как сделать чтобы работало?
- Запустите Docker Desktop
- В каждой папке есть docker-compose, используйте команду `docker-compose up` и перейдите на localhost, чтобы открыть сайт.
  
## Цель

1. Развернуть любое [приложение](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/volumes-mounts/www), которое меняет изображения через Bind Mounts и через Volume. Описать работу приложения, как работают данные компоненты, а также разницу между ними.
2. Развернуть любое [приложение](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/volumes-mounts/django), которое будет обновлять какую-либо информацию (не фото) через  Bind Mounts и через Volume. Описать работу приложения, как работают данные компоненты, а также разницу между ними. 
   
## Демонстрация

Лекция
<p align="center">
      <img src="https://github.com/user-attachments/assets/ab2bd02a-67ba-4350-90cf-2f211fd3f9ef" alt="Лекция" width="600">
</p>
Django
<p align="center">
      <img src="https://github.com/user-attachments/assets/9125e7a9-fa14-4d8e-a3a9-37349a56acc7" alt="Django" width="700">
</p>

## Вывод
Было развернуто приложение из лекции, которое меняет изображения через Blind Mounts и через Volume. Было развернуто Django приложение в Docker, которое меняет текст на сайте через Blind Mounts и Volume. Были описаны все пункты и аргументирован выбор команд
