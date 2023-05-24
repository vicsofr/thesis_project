# Тестовое задание Наймиум


## Описание проекта
Тестовое задание, в котором я реализовал API для представления структуры компании. Проект выполнен на Django + Django Rest
Framework. Запускается в Docker + docker-compose, для хранения данных используется СУБД PostgreSQL из контейнера.
В проекте доступны API для просмотра/изменения списка сотрудников и департамнтов. Доступна админка для изменения параметров.

## Настройка окружения
При запуске локально настройте окружение и установите зависимости:
```shell script
python -m venv venv
pip install -r requirements.txt
source venv/bin/activate
```

## Запуск проекта
Запуск осуществляется командой:
```shell script
docker-compose up -d
```

## Создание superuser
```shell script
docker-compose run app python manage.py createsuperuser
```

## Документация
Документация проекта доступна по ссылке после запуска проекта: [*Company API*](http://0.0.0.0:8000/swagger)

## Описание API и работы с проектом
* Запустите проект;
* Создайте суперюзера для работы с API, требующими авторизации;
* Администрационная панель для работы с моделями: [*Admin panel*](http://0.0.0.0:8000/admin);
* Для создания или получения списка сотрудников: [*GET POST /employees*](http://0.0.0.0:8000/company/employees);
* Для получения информации/изменения/удаления информации о сотруднике: [*GET PUT DELETE /employees/id*](http://0.0.0.0:8000/company/employees/EMPLOYEE_ID);
* Для получения списка департаментов: [*GET /departments*](http://0.0.0.0:8000/company/departments)



###### _Python 3.9.5_