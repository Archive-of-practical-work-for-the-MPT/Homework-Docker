# Практическая работа № 4 - Развертывание оконных приложений в Docker

## Описание

В данной практической мы учимся использовать X-сервер, для отображения графическим приложений развернутых в Docker контейнерах. В практической также нужно развернуть свое графическое приложение. Я выбрал свой проект - [Book Tracker](https://github.com/Merrcurys/Visual-list-of-books-app).

## Как сделать чтобы работало?
- Запустите Docker Desktop
- Запустите [Xming](https://sourceforge.net/projects/xming)
- В каждом Dockerfile снизу закомментированы команды для запуска в терминале.
  
## Цель

1. Развернуть [приложения](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/xming11/windows-app) xeyes и calc.jar из примера в Docker. Описать каждый пункт -почему именно эти команды и компоненты вы создаете. Развернуть еще одно любое приложение из x11-apps.
2. Развернуть любое [свое](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/xming11/Visual-list-of-books-app) оконное приложение.
3. Обязательное доп задание: прокинуть UI терминала из контейнера и вывести через него состав любой директории контейнера.
4. Залить готовую практическую на Gitlab или Github и прикрепить к заданию ссылку.

## Демонстрация

X11-apps
<p align="center">
      <img src="https://github.com/user-attachments/assets/37a20a52-a412-4d76-8027-97f22f283a71" alt="Лекция" width="600">
</p>
Book Tracker
<p align="center">
      <img src="https://github.com/user-attachments/assets/25841ad9-aa41-420f-88a3-6957adb19574" alt="Django" width="700">
</p>

## Вывод
Были развернуты оконные приложения из лекции. Развернуто еще одно приложение из x11-apps. Развернуто оконное приложение на PyQt и прокинут UI терминал из контейнера и выведен через него состав двух директорий. Описаны все пункты и аргументирован выбор команд.
