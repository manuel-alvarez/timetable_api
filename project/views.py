from apistar.backends import SQLAlchemy
from apistar.http import Response
from apistar.settings import Settings

from project.models import Teacher
from project.serializers import TeacherSerializer


def welcome():
    return {'message': 'Welcome to API Star!'}


def attempts(settings: Settings):
    return {'attempts': settings['ATTEMPTS']}


def teachers_list(db: SQLAlchemy):
    session = db.session_class()
    teachers = session.query(Teacher).all()
    return {"ok": True, "data": [TeacherSerializer(teacher) for teacher in teachers]}


def add_teacher(db: SQLAlchemy, name: str):
    session = db.session_class()
    db_teacher = Teacher(name=name)
    session.add(db_teacher)
    session.flush()
    return  {"ok": True, "data": TeacherSerializer(db_teacher)}
