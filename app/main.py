from .models import Course, Teacher
from fastapi import APIRouter, FastAPI
from fastapi import HTTPException
from .database import create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


router = APIRouter()


@router.get("/courses/{course_id}", response_model=Course)
async def read_course(course_id: int):
    course = await Course.get(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.post("/courses/", response_model=Course)
async def create_course(course: Course):
    await course.save()
    return course


@router.get("/teachers/{teacher_id}", response_model=Teacher)
async def read_teacher(teacher_id: int):
    teacher = await Teacher.get(teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher


@router.post("/teachers/", response_model=Teacher)
async def create_teacher(teacher: Teacher):
    await teacher.save()
    return teacher


app.include_router(router)
