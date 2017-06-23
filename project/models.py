from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Classroom(Base):
    """
    Classroom class. Bound to classroom database table
    """
    __tablename__ = "classroom"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Grade(Base):
    """
    Grade class. Bound to grade database table.
    """
    __tablename__ = "grade"
    id = Column(Integer, primary_key=True)
    name = Column(Integer)


class Teacher(Base):
    """
    Teachers class. Bound to teacher database table.
    """
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    name = Column(String)
