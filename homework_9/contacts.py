from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date, ForeignKey


engine = create_engine('postgresql+psycopg2://postgres:pilot123z@localhost:5432/AddressBook')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Contacts(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phones = Column(String)
    birthday = Column(Date)
    email = Column(String)
    status = Column(Integer)
    note = Column(String)

    def __init__(self, name, phones, birthday, email, status, note):
        self.name = name
        self.phones = phones
        self.birthday = birthday
        self.email = email
        self.status = status
        self.note = note

    def __repr__(self):
        return f"{self.name} {self.email}"




