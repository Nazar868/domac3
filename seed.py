from faker import Faker
import random

from database import SessionLocal
from models import Group, Teacher, Subject, Student, Grade

fake = Faker()

session = SessionLocal()

groups = [Group(name=f"Group-{i}") for i in range(1, 4)]
session.add_all(groups)

teachers = [Teacher(name=fake.name()) for _ in range(4)]
session.add_all(teachers)

subjects = []
for i in range(6):
    subjects.append(
        Subject(
            name=f"Subject-{i}",
            teacher=random.choice(teachers)
        )
    )
session.add_all(subjects)

students = []
for _ in range(40):
    students.append(
        Student(
            name=fake.name(),
            group=random.choice(groups)
        )
    )
session.add_all(students)

session.commit()

# grades
for student in students:
    for _ in range(random.randint(5, 20)):
        grade = Grade(
            value=random.randint(1, 12),
            student=student,
            subject=random.choice(subjects)
        )
        session.add(grade)

session.commit()

print("Database seeded!")
