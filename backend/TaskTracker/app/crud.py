from datetime import datetime

from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from . import models, schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, email: str):
    try:
        return db.query(models.User).filter(models.User.email == email).one()
    except MultipleResultsFound as e:
        print(e)
    except NoResultFound as e:
        pass


def get_technologies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Technology).offset(skip).limit(limit).all()


def get_tasks(user: schemas.User, db: Session, skip: int = 0, limit: int = 100):
    q = db.query(models.Task).filter(models.Task.user_id == user.id).join(models.Customer).join(models.Note). \
        join(models.Technology, models.Task.technologies).offset(skip).limit(limit).all()

    return q


def get_task(user: schemas.User, db: Session, task_id: int):
    q = db.query(models.Task).filter(models.Task.id == task_id).one()

    return q


def get_tasks_compl(user: schemas.User, db: Session, completed: bool, skip: int = 0, limit: int = 100):
    q = db.query(models.Task).filter(models.Task.user_id == user.id)
    if completed:
        q = q.filter(models.Task.completed_at is None)
    else:
        q = q.filter(models.Task.completed_at is not None)

    q = q.join(models.Customer).join(models.Note). \
        join(models.Technology, models.Task.technologies).offset(skip).limit(limit).all()

    return q


def get_notes(user: schemas.User, db: Session, task_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Note).filter(models.Note.task_id == task_id).offset(skip).limit(limit).all()


def create_note(current_user: schemas.User, db: Session, note: schemas.NoteCreate):
    db_note = models.Note(**note.model_dump(), created_at=datetime.utcnow(), updated_at=datetime.utcnow(), )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(current_user: schemas.User, db: Session, note_id: int):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
        return note
    return None


def get_customers(current_user: schemas.User, db: Session, skip: int = 0, limit: int = 100):
    customer = db.query(models.Customer).filter(models.Customer.user_id == current_user.id).offset(skip). \
        limit(limit).all()
    return customer


def get_customer(current_user: schemas.User, db: Session, customer_id: int):
    ## models.Customer.user_id == current_user.id,
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id) \
        .first()
    return customer


def get_notes_for_user_tasks(user: schemas.User, db: Session):
    #  .filter(models.Task.user_id == user.id)
    return (
        db.query(models.Note)
        .join(models.Task, models.Note.task_id == models.Task.id)

        .all()
    )


def get_notes(user: schemas.User, db: Session, search_text: str = None):
    query = db.query(models.Note).join(models.Task, models.Note.task_id == models.Task.id)

    if search_text:
        query = query.filter(
            or_(models.Note.title.ilike(f"%{search_text}%"), models.Note.description.ilike(f"%{search_text}%")))

    return query.all()
