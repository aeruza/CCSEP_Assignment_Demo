from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
# Define a FastAPI app
app = FastAPI()
# Create a Student data model
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

# In-memory list of students (as an example database)

students_db = [
    {"id": 1, "name": "Alice", "age": 21, "course": "Computer Science"},
    {"id": 2, "name": "Bob", "age": 22, "course": "Data Science"},
]

# Endpoint to fetch all students
@app.get("/students", response_model=List[Student])
def get_students():
    return students_db

# Endpoint to fetch a student by ID
@app.get("/students/{student_id}", response_model=Optional[Student])
def get_student(student_id: int):
    student = next((student for student in students_db if student["id"] ==
student_id), None)
    return student

# Endpoint to add a new student
@app.post("/students", response_model=Student)
def add_student(student: Student):
    students_db.append(student.dict())
    return student

# Malicious endpoint to demonstrate request smuggling
@app.post("/malicious")
def malicious_endpoint():
    return {"message": "Malicious action executed."}