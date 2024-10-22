# FasrApi-Todo-App
ToDoList Application
ToDoList is a web application built with FastAPI that allows users to manage their daily tasks. This project demonstrates the use of FastAPI for backend development.

Features
User authentication and authorization (login, logout)
Create, read, update, and delete (CRUD) tasks
Upload and display user profile photos
Secure password hashing
Token-based authentication with JWT
Technologies Used
Backend: FastAPI, SQLAlchemy, PostgreSQL, Pydantic, JWT
Other: Docker, Jinja2, Uvicorn
Installation
Prerequisites
Python 3.8+
PostgreSQL
Docker (optional)
Backend Setup
Clone the repository:
bash
Копировать код
git clone https://github.com/Frengocode/FasrApi-Todo-App.git
Create a virtual environment:
bash
Копировать код
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:
bash
Копировать код
pip install -r requirements.txt
Set up PostgreSQL:

Create a PostgreSQL database.
Update the DATABASE_URL in your environment variables to point to your PostgreSQL database.
Example of setting environment variable:

bash
Копировать код
export DATABASE_URL=postgresql://username:password@localhost:5432/todolist

Run the FastAPI server:

bash
Копировать код
uvicorn main:app --reload
Docker Setup (Optional)
Build the Docker image:
bash
Копировать код
docker-compose build
Run the application:
bash
Копировать код
docker-compose up
Usage
Open your browser and navigate to http://localhost:8000/docs to access the FastAPI interactive API documentation.
API Endpoints
POST /login: Login and get a JWT token.
POST /logout: Logout the current user.
POST /users: Create a new user.
GET /users/{id}: Get user details by ID.
POST /todos: Create a new to-do item.
GET /todos: Get all to-do items.
GET /todos/{id}: Get a specific to-do item by ID.
PUT /todos/{id}: Update a specific to-do item by ID.
DELETE /todos/{id}: Delete a specific to-do item by ID.
POST /upload-profile-photo: Upload a profile photo for the current user.
File Structure
css
Копировать код
todolist/
│   ├── routers/
│   │   ├── todo_router.py
│   │   ├── auhentication.py
│   │   ├── hash.py
│   │   ├── token.py
│   │   ├── user.py
│   │   ├── models/
|   |         |-- database.py
|   |         |-- models.py
|   |         |-- schema.py
│   │   ├── database.py
│   │   ├── main.py
│   ├── requirements.txt
│   └── README.MD