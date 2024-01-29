# Приложение для фрилансеров
Запуск сервера
```commandline
uvicorn main:app --reload
```

```commandline
 docker-compose build
docker-compose up -d
 docker compose run web alembic upgrade head

```
JWT tokens
Oauth 2.0
Bootstrap
Реактивный фронт

1. Пользователь
- email(string)(обязательно)
- password(string)(обязательно)
- username(string)(обязательно)


* таски(один ко много)(необязательно)
* заказчики(много ко много)(необязательно)

2. Таски
- ID(autoincrement)
- Email пользователя
- ID заказчика


- Имя задачи
- Краткое описание/условие 
- Дедлайн(дата)
- Оплата(сумма)
- Времени потрачено
- 
- Статус создана/завершена
- Дата завершения
- 
- Флаг оплаты не оплачена/оплачена/не будет оплачена
- Дата оплаты


* Пользователь(один)(обязательно)
* заказчик(один)(обязательно)
* технологии(много)
* заметки(много)

3. Заметки
- ID заметки(autoincrement)
- ID таска
- Title
- Text
- Created at
- Updated at
- Scheduled(optional)

4. таблица заказчики
- ID(автоинкремент)
- Контакт(string)
- Имя
- Таски(много)(необязательно)
- пользователь(один)(обязательно)

5. Технолигии
- ID(автоинкремент)
- Имя(string)
- Описание(string)

6. Таски_технолгии
- ID таска
- ID технолгии
