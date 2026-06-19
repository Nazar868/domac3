import argparse
from database import SessionLocal
from models import Student, Group, Teacher, Subject

session = SessionLocal()


def create(model, name):
    obj = model(name=name)
    session.add(obj)
    session.commit()


def list_all(model):
    return session.query(model).all()


def delete(model, id):
    obj = session.query(model).get(id)
    session.delete(obj)
    session.commit()


def update(model, id, name):
    obj = session.query(model).get(id)
    obj.name = name
    session.commit()


models_map = {
    "Student": Student,
    "Group": Group,
    "Teacher": Teacher,
    "Subject": Subject
}


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action")
parser.add_argument("-m", "--model")
parser.add_argument("--name")
parser.add_argument("--id")

args = parser.parse_args()

model = models_map.get(args.model)

if args.action == "create":
    create(model, args.name)

elif args.action == "list":
    print(list_all(model))

elif args.action == "remove":
    delete(model, args.id)

elif args.action == "update":
    update(model, args.id, args.name)
