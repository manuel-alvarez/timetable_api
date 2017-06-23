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
    data = {"results": [TeacherSerializer(teacher) for teacher in teachers], "count": len(teachers)}
    return Response(data, status=200)


def add_teacher(db: SQLAlchemy, name: str):
    session = db.session_class()
    db_teacher = Teacher(name=name)
    session.add(db_teacher)
    session.commit()

    db_teacher = session.query(Teacher).order_by("-id").first()
    data =  {"created": TeacherSerializer(db_teacher)}
    return Response(data, status=201)


def teacher_details(db: SQLAlchemy, teacher_id: int):
    session = db.session_class()
    db_teacher = session.query(Teacher).get(teacher_id)

    if db_teacher is None:
        return Response({}, status=404)
    data =  {"result": TeacherSerializer(db_teacher)}
    return Response(data, status=201)


def delete_teacher(db: SQLAlchemy, teacher_id: int):
    session = db.session_class()
    db_teacher = session.query(Teacher).get(teacher_id)
    session.delete(db_teacher)
    session.commit()

    data = {}
    return Response(data, status=204)
