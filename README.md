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
Реализовывать в дериктории:
```
api/v1/contact
```

1. Реализовать CRUD для модели Individual
2. Реализовать CRUD для модели Company

3. Реализовать company/all/list/ который 
возвращает общий список моделей Individual и Company:
```
[
    {"company": "{company_obj_1}"}, 
    {"company": "{company_obj_2}"}, 
    {"company": "{company_objт_n}"}, 
    {"individual": "{individual_obj_1}"}, 
    {"individual": "{individual_obj_2}"}, 
    {"individual": "{individual_obj_m}"}, 
]
```
n, m - кол-во всех объектов класса company и individual

## Задание 3 - Не забыть поздравить
У моделя `individual` может быть заполенено поле birth.
Я хочу получать уведомления о день рождении, когда осталось несколько дней.

Представим что у меня уже реализован планировщик задач, который каждый день запускат
функцию `check_birthday(before_days_count: int)`, которая находится по дериктории
`/contact/tasks/birthday_check.py `. Также представим что реализована функция которая отправляет уведомления на почту -
`send_birthday_notification(individual: Individual)`, которая находится по дериктории `/contact/services/mail_tamplates.py`. 
Эту функция реализовывать НЕ НУЖНО, просто используйте ее.

Вам необходимо реализовать фукнцию `check_birthday(before_days_count: int)`, которая проходится по всем объектам `individual` и проверяет:
если до день рождения осталось `before_days_count` или меньше, то вызвать функцию:
     `send_birthday_notification(individual: Individual)`