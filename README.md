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
# Frontend Project README

This repository contains the frontend code for a web application built using React. The project is a TaskTracker with features like user authentication, navigation, and interaction with a backend API.

## Technologies Used

- **React**: The project is developed using the React library for building user interfaces. React allows for the creation of reusable UI components, making the code modular and maintainable.

- **React Router**: Navigation within the application is handled using React Router. It enables the creation of a multi-page user experience while maintaining a single-page application feel.

- **Bootstrap**: The project utilizes Bootstrap for styling and layout. Bootstrap provides a responsive and visually appealing design, reducing the need for custom styling.

- **React Bootstrap**: The React Bootstrap library is integrated to use Bootstrap components as React components, facilitating seamless integration with the React application.

## Additional Features and Functionality
### Authentication and User Management
The application includes user authentication functionality. The Navibar component manages user login, logout, and displays user-specific information after login.

### Dynamic Content Loading
The application dynamically loads content based on the selected route, improving user experience.

## Docker Configuration

The project includes a Dockerfile for containerization. It uses the official Node.js image, sets up the working directory, installs dependencies using Yarn, and builds the frontend.


## Application Structure

The main application is defined in `App.js`, which includes routing and rendering components based on the URL. The `Navibar` component handles navigation and user authentication.

User authentication is managed with a login modal using React Bootstrap components. The application communicates with the backend API for user authentication and updates the UI accordingly.

## How to Run

1. Clone this repository.
2. Navigate to the project directory.
3. Build the Docker image:

    ```bash
    docker build -t frontend-app .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 3000:3000 frontend-app
    ```

5. Access the application in your browser at [http://localhost:3000](http://localhost:3000).

## Note

Ensure that the backend API is running and accessible at `http://127.0.0.1:8008` for proper functionality.

Feel free to customize the code to fit your specific requirements and styling preferences. Happy coding!