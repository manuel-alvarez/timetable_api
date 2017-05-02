from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Classroom(Base):
    __tablename__ = "classroom"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Grade(Base):
    __tablename__ = "grade"
    id = Column(Integer, primary_key=True)
    name = Column(Integer)


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    name = Column(String)
