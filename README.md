# TaskTracker

This project is a Task Tracker application built using FastAPI and SQLAlchemy. It allows users to manage tasks, customers, notes, and technologies. The application uses Pydantic for data validation and configuration settings.

## Technologies Used

- FastAPI: A modern, fast web framework for building APIs with Python.
- SQLAlchemy: An SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- Pydantic: Data validation and settings management using Python type annotations.
- PostgreSQL: A powerful, open-source relational database system.
- Docker: Containerization tool for packaging and distributing applications.

## Project Structure

The project is organized into several modules:

- `main.py`: FastAPI application instance and route definitions.
- `crud.py`: CRUD (Create, Read, Update, Delete) operations for interacting with the database.
- `schemas.py`: Pydantic models representing data structures used in the application.
- `models.py`: SQLAlchemy models representing database tables and relationships.
- `database.py`: Database setup and connection management.
- `config.py`: Configuration settings using Pydantic.

## API Endpoints

### User Management

- `/token`: Obtain an access token by providing valid credentials (username and password).
- `/refresh`: Obtain a new access token by providing a valid refresh token.

### Task Operations

- `/tasks/`: Get a list of tasks.
- `/tasks_completed/`: Get a list of completed or incompleted tasks.
- `/task/{task_id}`: Get details of a specific task.
- `/notes/`: Get a list of notes for a specific task.
- `/notes/`: Create a new note for a task.
- `/notes/{note_id}`: Delete a note for a task.

### Customer Operations

- `/customers/`: Get a list of customers.
- `/customer/{customer_id}`: Get details of a specific customer.
- `/customer/{customer_id}/tasks`: Get a list of tasks associated with a specific customer.

### Technology Operations

- `/technologies/`: Get a list of technologies.

### User Operations

- `/users/me/`: Get details of the authenticated user.

## How to Run

1. Install Docker on your machine.
2. Clone the repository.
3. Navigate to the project directory.
4. Run `docker-compose up --build` to build and start the containers.
5. Access the FastAPI application at [http://localhost:8008](http://localhost:8008).
6. Access the pgAdmin interface at [http://localhost:5050](http://localhost:5050) (credentials: admin@admin.com / root).

## Notes

- The application is configured to use a PostgreSQL database.
- The `settings.py` file contains configuration settings such as the database URL, secret key, and algorithm.
- The Docker setup includes containers for the FastAPI application, PostgreSQL database, and pgAdmin for database management.

Feel free to explore the API and modify the code to suit your requirements!

# Frontend
