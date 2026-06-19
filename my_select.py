from sqlalchemy import func
from database import SessionLocal
from models import Student, Group, Teacher, Subject, Grade

session = SessionLocal()


def select_1():
    return session.query(Student, func.avg(Grade.value))\
        .join(Grade)\
        .group_by(Student.id)\
        .order_by(func.avg(Grade.value).desc())\
        .limit(5)\
        .all()


def select_2(subject_id):
    return session.query(Student, func.avg(Grade.value))\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Student.id)\
        .order_by(func.avg(Grade.value).desc())\
        .first()


def select_3(subject_id):
    return session.query(Group.name, func.avg(Grade.value))\
        .join(Student)\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Group.id)\
        .all()


def select_4():
    return session.query(func.avg(Grade.value)).scalar()


def select_5(teacher_id):
    return session.query(Subject).filter(Subject.teacher_id == teacher_id).all()


def select_6(group_id):
    return session.query(Student).filter(Student.group_id == group_id).all()


def select_7(group_id, subject_id):
    return session.query(Student.name, Grade.value)\
        .join(Grade)\
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)\
        .all()


def select_8(teacher_id):
    return session.query(func.avg(Grade.value))\
        .join(Subject)\
        .filter(Subject.teacher_id == teacher_id)\
        .scalar()


def select_9(student_id):
    return session.query(Subject)\
        .join(Grade)\
        .filter(Grade.student_id == student_id)\
        .distinct()\
        .all()


def select_10(student_id, teacher_id):
    return session.query(Subject)\
        .join(Grade)\
        .filter(
            Grade.student_id == student_id,
            Subject.teacher_id == teacher_id
        ).distinct().all()
