from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)

    hashed_password = Column(String, nullable=False)
    username = Column(String, nullable=False)
    role = Column(String, nullable=False, default="User")

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    tasks = relationship("Task", back_populates="user", cascade="all, delete")
    customers = relationship("Customer", back_populates="user", cascade="all, delete")


class TasksTechnologies(Base):
    __tablename__ = "tasks_technologies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    technology_id = Column(Integer, ForeignKey("technologies.id"))


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=True)
    payment = Column(Integer, nullable=False)
    hours = Column(Integer, nullable=True)

    status_completed = Column(String, nullable=False)
    completed_at = Column(DateTime, nullable=True)

    status_payment = Column(String, nullable=False)
    payment_at = Column(DateTime, nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="tasks")
    customer = relationship("Customer", back_populates="tasks")
    notes = relationship("Note", back_populates="task", cascade="all, delete")
    technologies = relationship("Technology", secondary=TasksTechnologies.__table__, back_populates="tasks",
                                cascade="all, delete")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)

    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    scheduled_at = Column(DateTime, nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    task = relationship("Task", back_populates="notes")


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    contact = Column(String, unique=False, nullable=False)
    name = Column(String, unique=False, nullable=False)

    tasks = relationship("Task", back_populates="customer")
    user = relationship("User", back_populates="customers")


class Technology(Base):
    __tablename__ = "technologies"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

    tasks = relationship("Task", secondary=TasksTechnologies.__table__,
                         back_populates='technologies', cascade="all, delete")


'''
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


'''
