from fastapi import FastAPI
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
def get_student(student_id: int):
    if student_id not in student:
        return {"error": "Student not found"}
    return student[student_id]


