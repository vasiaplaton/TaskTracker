from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from starlette.middleware.cors import CORSMiddleware

from .database import get_db
from sqlalchemy.orm import Session
from . import crud, schemas, security
from .security import get_current_active_user

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specific origins as a list
    allow_credentials=True,
    allow_methods=["*"],  # or specific HTTP methods as a list
    allow_headers=["*"],  # or specific headers as a list
)

app.include_router(security.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[schemas.User]:
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/technologies/", response_model=list[schemas.Technology])
def read_technologies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    technologies = crud.get_technologies(db, skip=skip, limit=limit)
    return technologies


@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(current_user: Annotated[schemas.User, Depends(get_current_active_user)], skip: int = 0, limit: int = 100
               , db: Session = Depends(get_db)):
    technologies = crud.get_tasks(current_user, db, skip=skip, limit=limit)

    return technologies


@app.get("/tasks_completed/", response_model=list[schemas.Task])
def read_tasks_1(current_user: Annotated[schemas.User, Depends(get_current_active_user)], completed: bool,
                 skip: int = 0, limit: int = 100
                 , db: Session = Depends(get_db)):
    technologies = crud.get_tasks_compl(current_user, db, completed, skip=skip, limit=limit)

    return technologies


@app.get("/notes/", response_model=list[schemas.Note])
def read_notes(current_user: Annotated[schemas.User, Depends(get_current_active_user)], task_id: int, skip: int = 0,
               limit: int = 100
               , db: Session = Depends(get_db)):
    return crud.get_notes(current_user, db, task_id, skip, limit)


@app.post("/notes/", response_model=list[schemas.Note])
def read_notes(current_user: Annotated[schemas.User, Depends(get_current_active_user)], note: schemas.NoteCreate,
               db: Session = Depends(get_db)):
    return crud.create_note(current_user, db, note)


@app.delete("/notes/{note_id}", response_model=schemas.Note)
def delete_note(current_user: Annotated[schemas.User, Depends(get_current_active_user)], note_id: int,
                db: Session = Depends(get_db)):
    note = crud.delete_note(current_user, db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.get("/task/{task_id}", response_model=schemas.Task)
def delete_note(current_user: Annotated[schemas.User, Depends(get_current_active_user)], task_id: int,
                db: Session = Depends(get_db)):
    return crud.get_task(current_user, db, task_id)


@app.get("/customers/", response_model=list[schemas.Customer])
def read_customers(current_user: Annotated[schemas.User, Depends(get_current_active_user)], skip: int = 0,
                   limit: int = 100
                   , db: Session = Depends(get_db)):
    return crud.get_customers(current_user, db, skip, limit)


@app.get("/customer/{customer_id}", response_model=schemas.Customer)
def read_customers(current_user: Annotated[schemas.User, Depends(get_current_active_user)], customer_id: int,
                   db: Session = Depends(get_db)):
    return crud.get_customer(current_user, db, customer_id)


@app.get("/customer/{customer_id}/tasks", response_model=list[schemas.Task])
def get_tasks_for_customer(
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        customer_id: int,
        db: Session = Depends(get_db),
):
    tasks = crud.get_tasks_for_customer(current_user, db, customer_id)
    return tasks


@app.get("/notes/user-tasks", response_model=list[schemas.Note])
def get_notes_for_user_tasks(
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db),
):
    notes = crud.get_notes_for_user_tasks(current_user, db)

    return notes


@app.get("/notes-filter", response_model=list[schemas.NoteTask])
def get_notes(
        current_user: Annotated[schemas.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db),
        search_text: str = Query(None, title="Search by text")
):
    notes = crud.get_notes(current_user, db, search_text=search_text)

    return notes
