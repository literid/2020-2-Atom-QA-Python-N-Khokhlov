from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = {'mysql_charset':'utf8'}
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    surname = Column(String(40), nullable=False)

