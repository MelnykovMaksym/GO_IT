from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey, String, Text, Table
from sqlalchemy.orm import relationship, backref

engine = create_engine('postgresql+psycopg2://postgres:pilot123z@localhost:5432/students_db')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Student(Base.metadata):
    __tablename__ = "student",
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth_date = Column(Date)

    def __init__(self, name, surname, birth_date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def __repr__(self):
        return f'{self.name}_{self.surname}'


class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)


    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{self.name}'


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    course_id = Column(Integer, ForeignKey('course.id'))


    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course

    def __repr__(self):
        return f'{self.name}_{self.surname}'
