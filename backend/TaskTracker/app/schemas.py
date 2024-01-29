from datetime import datetime
from typing import Union, Optional

from pydantic import BaseModel


# Tokens
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


"""
    id

    name
    description 

    tasks
"""


class TechnologyBase(BaseModel):
    name: str
    description: Optional[str] = None


class TechnologyCreate(TechnologyBase):
    pass


class Technology(TechnologyBase):
    id: int

    class Config:
        orm_mode = True


"""
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)

    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    scheduled_at = Column(String, nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    task = relationship("Task", back_populates="notes")"""


class NoteBase(BaseModel):
    task_id: int

    title: str
    description: Optional[str] = None
    scheduled_at: Optional[datetime] = None


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int

    created_at: datetime
    updated_at: datetime

    # task?
    class Config:
        orm_mode = True



"""
    id 
    user_id

    contact 
    name

    tasks
    user
"""


class CustomerBase(BaseModel):
    contact: str
    name: str


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int
    user_id: int

    # user?
    # tasks: list[Task]?
    class Config:
        orm_mode = True


"""
    + id
    + user_id 
    + customer_id

    +name 
    +description
    + deadline
    + payment
    + hours

    status_completed
    completed_at

    status_payment
    payment_at

    created_at
    updated_at

    user
    customer
    notes
    technologies
"""


class TaskBase(BaseModel):
    customer_id: int

    name: str
    description: str
    deadline: Optional[datetime] = None
    payment: int


class TaskCreate(TaskBase):
    count_hours: bool


class Task(TaskBase):
    id: int
    user_id: int
    hours: Optional[int]

    status_completed: str
    completed_at: Optional[datetime]

    status_payment: str
    payment_at: Optional[datetime]

    created_at: datetime
    updated_at: datetime

    # user: User
    customer: Customer
    notes: list[Note]
    technologies: list[Technology]

    class Config:
        orm_mode = True


"""
id email

hashed_password username role

created_at updated_at

tasks customers
"""


# common add/get
class UserBase(BaseModel):
    email: str
    username: str


# for add
class UserCreate(UserBase):
    password: str


# for return
class User(UserBase):
    id: int
    role: str

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class NoteTask(NoteBase):
    task: TaskBase
