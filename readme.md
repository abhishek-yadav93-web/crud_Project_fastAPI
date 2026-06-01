# Employee Management API

A RESTful CRUD API built with FastAPI, SQLAlchemy, and MySQL for managing employee records. This project demonstrates backend development concepts including API design, database integration, request validation, and CRUD operations.

## Features

* Create new employee records
* Retrieve employee details
* Update existing employee information
* Delete employee records
* MySQL database integration
* SQLAlchemy ORM support
* FastAPI automatic API documentation
* Request and response validation using Pydantic

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* MySQL
* Pydantic
* Uvicorn

## Project Structure

```text
project/
│
├── main.py
├── config.py
├── database.py
├── models/
├── schemas/
├── routers/
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd Employee-Management-API
```

3. Create and activate a virtual environment

```bash
python -m venv venv
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Configure database settings in your environment or configuration file.

## Run the Application

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

## Learning Outcomes

This project helped me gain practical experience with:

* REST API development
* Database connectivity
* SQLAlchemy ORM
* FastAPI framework
* CRUD operations
* Backend project structure
* Git and GitHub workflow