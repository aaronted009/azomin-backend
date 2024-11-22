from .models import (
    ClassRoom,
    Course,
    Exam,
    ExamResult,
    Fee,
    Student,
    StudentTutor,
    Teacher,
)
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


# CRUD operations for the Course model
@router.post("/courses/", response_model=Course)
async def create_course(course: Course):
    await course.save()
    return course


@router.get("/courses/{course_id}", response_model=Course)
async def read_course(course_id: int):
    course = await Course.get(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.put("/courses/{course_id}", response_model=Course)
async def update_course(course_id: int, course: Course):
    await Course.update(course_id, course)
    return course


@router.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    course = await Course.get(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    await course.delete()
    return {"message": "Course deleted"}


# CRUD operations for the Course model -- end


# CRUD operations for the Student model
@router.post("/students/", response_model=Student)
async def create_student(student: Student):
    await student.save()
    return student


@router.get("/students/{student_id}", response_model=Student)
async def read_student(student_id: int):
    student = await Student.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, student: Student):
    await Student.update(student_id, student)
    return student


@router.delete("/students/{student_id}")
async def delete_student(student_id: int):
    student = await Student.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    await student.delete()
    return {"message": "Student deleted"}


# CRUD operations for the Student model -- end


# CRUD operations for the Exam model
@router.post("/exams/", response_model=Exam)
async def create_exam(exam: Exam):
    await exam.save()
    return exam


@router.get("/exams/{exam_id}", response_model=Exam)
async def read_exam(exam_id: int):
    exam = await Exam.get(exam_id)
    if exam is None:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam


@router.put("/exams/{exam_id}", response_model=Exam)
async def update_exam(exam_id: int, exam: Exam):
    await Exam.update(exam_id, exam)
    return exam


@router.delete("/exams/{exam_id}")
async def delete_exam(exam_id: int):
    exam = await Exam.get(exam_id)
    if exam is None:
        raise HTTPException(status_code=404, detail="Exam not found")
    await exam.delete()
    return {"message": "Exam deleted"}


# CRUD operations for the Exam model -- end


# CRUD operations for the ExamResult model
@router.post("/exam_results/", response_model=ExamResult)
async def create_exam_result(exam_result: ExamResult):
    await exam_result.save()
    return exam_result


@router.get("/exam_results/{exam_result_id}", response_model=ExamResult)
async def read_exam_result(exam_result_id: int):
    exam_result = await ExamResult.get(exam_result_id)
    if exam_result is None:
        raise HTTPException(status_code=404, detail="Exam result not found")
    return exam_result


@router.put("/exam_results/{exam_result_id}", response_model=ExamResult)
async def update_exam_result(exam_result_id: int, exam_result: ExamResult):
    await ExamResult.update(exam_result_id, exam_result)
    return exam_result


@router.delete("/exam_results/{exam_result_id}")
async def delete_exam_result(exam_result_id: int):
    exam_result = await ExamResult.get(exam_result_id)
    if exam_result is None:
        raise HTTPException(status_code=404, detail="Exam result not found")
    await exam_result.delete()
    return {"message": "Exam result deleted"}


# CRUD operations for the ExamResult model -- end


# CRUD operations for the Fee model
@router.post("/fees/", response_model=Fee)
async def create_fee(fee: Fee):
    await fee.save()
    return fee


@router.get("/fees/{fee_id}", response_model=Fee)
async def read_fee(fee_id: int):
    fee = await Fee.get(fee_id)
    if fee is None:
        raise HTTPException(status_code=404, detail="Fee not found")
    return fee


@router.put("/fees/{fee_id}", response_model=Fee)
async def update_fee(fee_id: int, fee: Fee):
    await Fee.update(fee_id, fee)
    return fee


@router.delete("/fees/{fee_id}")
async def delete_fee(fee_id: int):
    fee = await Fee.get(fee_id)
    if fee is None:
        raise HTTPException(status_code=404, detail="Fee not found")
    await fee.delete()
    return {"message": "Fee deleted"}


# CRUD operations for the Fee model -- end


# CRUD operations for the ClassRoom model
@router.post("/classrooms/", response_model=ClassRoom)
async def create_classroom(classroom: ClassRoom):
    await classroom.save()
    return classroom


@router.get("/classrooms/{classroom_id}", response_model=ClassRoom)
async def read_classroom(classroom_id: int):
    classroom = await ClassRoom.get(classroom_id)
    if classroom is None:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return classroom


@router.put("/classrooms/{classroom_id}", response_model=ClassRoom)
async def update_classroom(classroom_id: int, classroom: ClassRoom):
    await ClassRoom.update(classroom_id, classroom)
    return classroom


@router.delete("/classrooms/{classroom_id}")
async def delete_classroom(classroom_id: int):
    classroom = await ClassRoom.get(classroom_id)
    if classroom is None:
        raise HTTPException(status_code=404, detail="Classroom not found")
    await classroom.delete()
    return {"message": "Classroom deleted"}


# CRUD operations for the ClassRoom model -- end


# CRUD operations for the StudentTutor model
@router.post("/student_tutors/", response_model=StudentTutor)
async def create_student_tutor(student_tutor: StudentTutor):
    await student_tutor.save()
    return student_tutor


@router.get("/student_tutors/{student_tutor_id}", response_model=StudentTutor)
async def read_student_tutor(student_tutor_id: int):
    student_tutor = await StudentTutor.get(student_tutor_id)
    if student_tutor is None:
        raise HTTPException(status_code=404, detail="Student tutor not found")
    return student_tutor


@router.put("/student_tutors/{student_tutor_id}", response_model=StudentTutor)
async def update_student_tutor(student_tutor_id: int, student_tutor: StudentTutor):
    await StudentTutor.update(student_tutor_id, student_tutor)
    return student_tutor


@router.delete("/student_tutors/{student_tutor_id}")
async def delete_student_tutor(student_tutor_id: int):
    student_tutor = await StudentTutor.get(student_tutor_id)
    if student_tutor is None:
        raise HTTPException(status_code=404, detail="Student tutor not found")
    await student_tutor.delete()
    return {"message": "Student tutor deleted"}


# CRUD operations for the StudentTutor model -- end


# CRUD operations for the Teacher model
@router.post("/teachers/", response_model=Teacher)
async def create_teacher(teacher: Teacher):
    await teacher.save()
    return teacher


@router.get("/teachers/{teacher_id}", response_model=Teacher)
async def read_teacher(teacher_id: int):
    teacher = await Teacher.get(teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher


@router.put("/teachers/{teacher_id}", response_model=Teacher)
async def update_teacher(teacher_id: int, teacher: Teacher):
    await Teacher.update(teacher_id, teacher)
    return teacher


@router.delete("/teachers/{teacher_id}")
async def delete_teacher(teacher_id: int):
    teacher = await Teacher.get(teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    await teacher.delete()
    return {"message": "Teacher deleted"}


# CRUD operations for the Teacher model -- end

app.include_router(router)
