# Тестовое задание на позицию pre-middle Python-разработчик
## Django приложение для получения актуального курса доллара

Приложение реализовано на основе Django Rest Framework (DRF) и служит для отображения информации о текущем курсе
в формате JSON, хранит информацию в базе данных postgres. Возможно задавать интервал периодических задач для 
обновления курса доллара с сайта центробанка РФ.  Для периодических задач используется Celery с Celery Beat.

Приложение упаковано с помощью Docker Compose и может быть без труда развернуто на удаленном сервере.

Перед запуском приложения необходимо в корне проекта создать файл .env с необходимыми переменными окружения. В качестве
примера можете воспользоваться файлом .env_example.

После запуска по адресу http://0.0.0.0:8000/swagger/ будет доступна документация API, которую можно использовать для 
интеграции сторонних ботов.

Используемые в проекте технологии:

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=green)
![](https://img.shields.io/badge/Framework-DRF-informational?style=flat&logo=django&logoColor=white&color=green)
![](https://img.shields.io/badge/Database-postgreSQL-informational?style=flat&logo=postgresql&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Redis-informational?style=flat&logo=redis&logoColor=white&color=green)

### Настройка

Убедитесь, что у вас установлены Docker и Docker Compose.

1. Клонируйте репозиторий и перейдите в каталог с проектом:

    ```bash
   git clone https://github.com/Heattehnik/rubletodollar.git
   
   cd rubletodollar
    ```
2. Создайте файл `.env` с необходимыми переменными окружения.

### Структура Файлов

- `./config`: содержаться основные настройки проекта.
- `./currency`: содержится приложение.
- `docker-compose.yml`: Файл конфигурации для Docker Compose.
- `.env`: Переменные окружения, необходимые для работы приложения.

### Запуск проекта

1. Выполните `sudo docker-compose build` для сборки образов
2. Выполните `sudo docker-compose up -d`, чтобы запустить сервисы.
3. После запуска автоматически добавляются периодические задачи celery. Отправляется запрос на получение актуального курса
ЦБ РФ, интервал запросов установлен на 1 запрос в 10 секунд.


### Использование

После запуска пользователю по адресу http://0.0.0.0:8000/get-current-usd/ будет доступен последний актуальный курс и 
 последние 10 запрошенных

