from apistar.backends import SQLAlchemy
from apistar.settings import Settings

from project.models import Teacher


def welcome():
    return {'message': 'Welcome to API Star!'}


def attempts(settings: Settings):
    return {'attempts': settings['ATTEMPTS']}


def teachers_list(db: SQLAlchemy):
    session = db.session_class()
    teachers = session.query(Teacher).all()
    return teachers
