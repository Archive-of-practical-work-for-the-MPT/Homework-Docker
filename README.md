# Практическая работа № 12 - Создание первого пайплайна

## Цель

На локальном GitLab научиться создавать gitlab ci pipeline. Используя курсовой проект необходимо создать pipeline запускаемый на настроенном runner’е. Pipeline должен проверять сборку проекта, проверять синтаксические ошибки линтера, а также 2 любые функциональнее задачи. Также настроить переадресацию контейнера на правильный URL.

## Как сделать чтобы работало?
- Повторите предыдущую практическую работу - "[Практическая работа №11 Начало работы с Gitlab](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/tree/gitlab)".
- Скачайте этот проект, который основан на декабрьской [курсовой](https://github.com/Archive-of-practical-work-for-the-MPT/GreenQuality) 4 курса.
- Зарегестрируйте runner через ```docker exec -it gitlab-gitlab-runner-1 gitlab-runner register```. В URL пропишите id контейнера Gitlab, а токен скопируйте в Admin/CI-CD/Runners, остальное можете проскипать.
- Установите библиотеки внутри контейнера runner'а.
- Создайте репозиторий и загрузите скачанный проект.
- Pipeline запустится автоматически.
- Чтобы сделать переадресацию поменяйте файл gitlab.rb, а именно переменные: [external_url](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/blob/pipeline/gitlab.rb#L32) и [nginx["listen_port"]](https://github.com/Archive-of-practical-work-for-the-MPT/Homework-Docker/blob/pipeline/gitlab.rb#L1873)
- Затем ```gitlab-ctl reconfigure```

Перед запуском docker-compose, убедитесь, что у вас для докера установлено около 7Гб+ RAM, иначе он может работать очень медленно, затем запустите:
- docker-compose up
  
## Критерии на 4
1. Реализовать gitlab ci пайплайн, запускаемый на настроенном раннере (runner).

2. Проверка сборки проекта.

3. Проверка синтаксических ошибок линтером.

4. Любые 2 дополнительные функциональные задачи.
  
5. Настроить переадресацию контейнера на правильный URL.

## Демонстрация

<p align="center">
      <img src="https://github.com/user-attachments/assets/65a5ba3a-2fe5-43dc-aa86-a4a15011b0c6" alt="Демонстрация" width="700">
</p>

## Вывод
Используя курсовой проект был создан pipeline запускаемый на настроенном runner’е. Pipeline включает в себя проверять сборку проекта, проверку синтаксических ошибок линтера, а также 2 функциональные задачи. Также была настроена переадресация контейнера на правильный URL.
