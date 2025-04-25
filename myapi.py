from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()
student = {
    1: {
        "name": "hello",
        "age": 30,
        "class": 12
    },
    2: {
        "name": "john",
        "age": 20,
        "class": 11
    }
}

@app.get("/")
def index():
    return{ "name" : "first data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., title="Student ID", description="The ID of the student to retrieve")):
    
    if student_id not in student:
        return {"error": "Student not found"}
    return student[student_id]

@app.get("/get-by-name/{student_id})")
def get_by_name(*, student_id : int ,name: Optional[str] = None, test :int):
    for student_id in students:
        return student[student_id]["name"]== name
    return {"data": "not found"}



