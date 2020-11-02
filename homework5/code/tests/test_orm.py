import pytest

from tests.models.models import Student
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection
from tests.orm_builder import MysqlOrmBuilder
from faker import Faker
from sqlalchemy.sql import exists


class TestStudents:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlOrmConnection = mysql_orm_client
        self.builder: MysqlOrmBuilder = MysqlOrmBuilder(connection=self.mysql)

    def test_creating_students_table(self):
        self.builder.create_students()
        assert self.builder.engine.dialect.has_table(self.builder.engine, 'students')

    def test_adding_student(self):
        fake = Faker()
        name = fake.first_name()
        surname = fake.last_name()
        self.builder.create_students()
        self.builder.add_student(name, surname)
        assert (self.mysql.session.query(exists().where(Student.name == name and Student.surname == surname)).scalar())
