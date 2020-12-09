from mysql_orm_client.mysql_orm_client import MysqlOrmConnection
from tests.models.models import Base, Student


class MysqlOrmBuilder:
    def __init__(self, connection: MysqlOrmConnection):
        self.engine = connection.connection.engine
        self.connection = connection

    def create_students(self):
        if not self.engine.dialect.has_table(self.engine, 'students'):
            Base.metadata.tables['students'].create(self.engine)

    def add_student(self, name, surname):
        stud = Student(name=name, surname=surname)
        self.connection.session.add(stud)
        self.connection.session.commit()
