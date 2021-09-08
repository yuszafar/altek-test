## Задание 1 - устанвливаем и поднимаем сервер

1 - create venv 
```
python -m venv ./venv
```
2 - activate venv
```
venv\Scripts\activate.bat
```
3 - install requirements.txt
```
pip install -r requirements.txt
```
4 - makemigrations
```
python manage.py makemigrations
```
5 - migrate
```
python manage.py migrate
```

6 - runserver
```
python manage.py runserver
```

7 - create user
```
python manage.py createsuperuser
```

## Задание 2 - Создаем CRUD
Реализовывать в директории:
```
api/v1/contact
```

1. Реализовать CRUD для модели Individual
2. Реализовать CRUD для модели Company

3. Реализовать GET company/all/list/, который 
возвращает общий список объектов Individual и Company:
```
[
    {"company": "{company_obj_1}"}, 
    {"company": "{company_obj_2}"}, 
    ...
    {"company": "{company_objт_n}"}, 
    {"individual": "{individual_obj_1}"}, 
    {"individual": "{individual_obj_2}"}, 
    ...
    {"individual": "{individual_obj_m}"}, 
]
```
n, m - кол-во всех объектов класса Company и Individual.

## Задание 3 - Не забыть поздравить
У модели `Individual` может быть заполенено поле birth.
Я хочу получать уведомления о дне рождения, когда до него осталось несколько дней.

Представим, что у меня уже реализован планировщик задач, который каждый день запускает
функцию `check_birthday(before_days_count: int)`, которая находится в директории
`/contact/tasks/birthday_check.py `. Также представим, что реализована функция, которая отправляет уведомления на почту -
`send_birthday_notification(individual: Individual)`, которая находится в директории `/contact/services/mail_tamplates.py`. 
Эту функцию реализовывать **НЕ НУЖНО**, просто используйте ее.

Вам необходимо реализовать фукнцию `check_birthday(before_days_count: int)`, которая проходится по всем объектам `Individual` и проверяет:
если до дня рождения осталось `before_days_count` или меньше, то вызвать функцию:
     `send_birthday_notification(individual: Individual)`
