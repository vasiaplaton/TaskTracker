from sqlalchemy.orm import Session
from datetime import datetime
from .models import *
from .security import *
import random


def generate_technologies(db: Session):
    # Создание технологий
    technologies = [
        Technology(name="java", description="Java programming language"),
        Technology(name="python", description="Python programming language"),
        Technology(name="JavaScript",
                   description="A high-level, interpreted scripting language used for web development."),
        Technology(name="PHP", description="A widely-used server-side scripting language for web development."),
        Technology(name="HTML/CSS",
                   description="The building blocks of web pages, used for creating and styling web content."),
        Technology(name="MySQL", description="An open-source relational database management system."),
        Technology(name="Ruby", description="A dynamic, open-source programming language."),
        Technology(name="C#", description="A versatile programming language developed by Microsoft."),
        Technology(name="Swift",
                   description="Apple's programming language for iOS, macOS, watchOS, and tvOS app development."),
        Technology(name="Kotlin",
                   description="A modern, statically-typed programming language for Android app development."),
        Technology(name="React", description="A JavaScript library for building user interfaces."),
        Technology(name="Vue.js", description="A progressive JavaScript framework for building web interfaces."),
    ]
    db.bulk_save_objects(technologies)
    db.commit()


def generate_users(db: Session):
    usernames = [
        "CodeNinja", "TechGuru", "DataWizard", "CyberPirate",
        "GeekChic", "PixelPioneer", "DigitalNomad", "WebMaster", "AppDeveloper"
    ]
    # Создание пользователей на основе никнеймов
    users_data = [
        {"username": "admin", "email": "vasia.platon@gmail.com", "hashed_password": get_password_hash("admin"),
         "role": "Admin"}]
    for username in usernames:
        email = f"{username.lower()}@gmail.com"
        hashed_password = get_password_hash(username)
        users_data.append({"username": username, "email": email, "hashed_password": hashed_password, "role": "User"})

    db.bulk_save_objects(
        [User(**user_data, created_at=datetime.utcnow(), updated_at=datetime.utcnow()) for user_data in users_data])
    db.commit()


def generate_customers(db: Session):
    first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
    last_names = ["Smith", "Johnson", "Brown", "Davis", "Wilson", "Lee", "Moore", "Taylor", "Clark", "Hall"]
    # Создание заказчиков
    customers_data = []
    i = 0
    user_ids = db.query(User.id).all()
    user_ids = [user_id for (user_id,) in user_ids]
    user_ids = user_ids * 10
    random.shuffle(user_ids)

    for first_name in first_names:
        for last_name in last_names:
            user_id = user_ids[i]
            customers_data.append(
                {"contact": f"{first_name}_{last_name}", "name": f"{first_name} {last_name}", "user_id": user_id})
            i += 1

    # , created_at=datetime.utcnow(), updated_at=datetime.utcnow()
    db.bulk_save_objects(
        [Customer(**customer_data) for customer_data in
         customers_data])
    db.commit()


def generate_tasks(db: Session):
    # Создание задач
    tasks_data = []
    task_statuses = ["New", "Completed"]

    task_difficulties = ["Easy", "Moderate", "Difficult", "Gorgeous", "Interesting", "Boring", "Complex", "Tricky",
                         "Ambiguous", "Intricate"]

    adjectives = ["Important", "Critical", "Challenging", "Exciting", "Ambitious", "Innovative", "Creative",
                  "Cutting-edge", "Revolutionary", "Groundbreaking"]

    task_domains = [
        "Web Development", "Data Analysis", "Machine Learning", "Mobile App Development",
        "Double Linked List", "Chess", "Binary Tree", "Cybersecurity", "Game Development", "Blockchain"
    ]

    user_ids = db.query(User.id).all()
    user_ids = [user_id for (user_id,) in user_ids]
    user_ids = user_ids * 100
    random.shuffle(user_ids)

    customers_ids = db.query(Customer.id).all()
    customers_ids = [customers_id for (customers_id,) in customers_ids]
    customers_ids = customers_ids * 10
    random.shuffle(customers_ids)

    for i in range(1000):
        user_id = user_ids[i]
        customer_id = customers_ids[i]
        name = random.choice(task_difficulties) + " " + random.choice(adjectives) + " " + random.choice(task_domains)
        description = f"Description for Task {i}"
        deadline = datetime.utcnow()
        payment = random.randint(100, 10000)
        hours = random.randint(1, 10)
        status_completed = random.choice(task_statuses)
        completed_at = datetime.utcnow() if status_completed == "Completed" else None
        status_payment = random.choice(task_statuses)
        payment_at = datetime.utcnow() if status_payment == "Completed" else None

        tasks_data.append(
            Task(
                user_id=user_id,
                customer_id=customer_id,
                name=name,
                description=description,
                deadline=deadline,
                payment=payment,
                hours=hours,
                status_completed=status_completed,
                completed_at=completed_at,
                status_payment=status_payment,
                payment_at=payment_at,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
        )

    db.bulk_save_objects(tasks_data)
    db.commit()


def append_technologies(db: Session):
    tasks_ids = db.query(Task.id).all()
    tasks_ids = [task_id for (task_id,) in tasks_ids]

    technologies_ids = db.query(Technology.id).all()
    technologies_ids = [technologies_id for (technologies_id,) in technologies_ids]

    # Назначение случайных технологий каждой задаче
    for task in tasks_ids:
        random_technologies = random.sample(technologies_ids, 3)
        for tech in random_technologies:
            task_technology = TasksTechnologies(task_id=task, technology_id=tech)
            db.add(task_technology)
    db.commit()


def generate_notes(db: Session):
    tasks = db.query(Task).all()
    # Выбор случайных 100 задач и добавление к ним заметок
    selected_tasks = random.sample(tasks, 100)
    for task in selected_tasks:
        note = Note(
            task_id=task.id,
            title=f"Great note for task {task.name}",
            description="Some description for the great note",
            scheduled_at=None,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        db.add(note)

    selected_tasks = random.sample(selected_tasks, 30)
    for task in selected_tasks:
        note = Note(
            task_id=task.id,
            title=f"Second Great note for task {task.name}",
            description="Some description for the second great note",
            scheduled_at=None,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        db.add(note)

    db.commit()


def random_generate(db: Session):
    generate_technologies(db)
    generate_users(db)
    generate_customers(db)
    generate_tasks(db)
    append_technologies(db)
    generate_notes(db)
