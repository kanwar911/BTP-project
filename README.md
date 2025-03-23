# BTP-project
# Task Manager API - FastAPI

This is a simple, fully functional Task Manager API built with FastAPI, showcasing how to implement CRUD operations using modern Python practices like type hints, Pydantic models, and automatic documentation.

## Features

- Create, Read, Update, and Delete (CRUD) tasks
- Fast and asynchronous using FastAPI + Uvicorn
- In-memory storage (no database required)
- Interactive documentation (Swagger UI & ReDoc) auto-generated
- Clean and beginner-friendly code

---

## Project Structure

   
 fastapi-task-manager
 ├━ main.py
 ├━ requirements.txt
 ┗━ README.md
   
---

## Requirements

- Python 3.7 or above  
- pip
---
## Setup Instructions

1. Clone the repository https://github.com/kanwar911/BTP-project.git
   git clone 
   cd fastapi-task-manager

2.   Create a virtual environment  
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
      
3.   Install dependencies  
   pip install -r requirements.txt

4.   Run the API server  
   uvicorn main:app --reload
---
## API Endpoints
| Method | Endpoint           | Description             |
|--------|--------------------|-------------------------|
| POST   |  /tasks            | Create a new task       |
| GET    |  /tasks            | Get all tasks           |
| GET    |  /tasks/{task_id}  | Get a task by ID        |
| PUT    |  /tasks/{task_id}  | Update a task           |
| DELETE |  /tasks/{task_id}  | Delete a task           |

---

## Interactive Docs
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
---
## Example Task JSON

   json
{
  "id": 1,
  "title": "Write Final Report",
  "description": "Complete the FastAPI research paper",
  "completed": false
}
   
---

## Testing

Use Swagger UI to test endpoints directly in your browser or tools like   Postman   or   cURL  .
---
## License

This project is open for educational use. You may extend or build upon it for learning or demonstration purposes.
---
## Author
Kanwar Singh Sandhu    
Student @ Senecapolytechnic
GitHub: https://github.com/kanwar911
