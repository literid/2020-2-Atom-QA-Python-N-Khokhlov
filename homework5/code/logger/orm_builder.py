from logger.log_models.models import *
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection


class MysqlOrmBuilder:
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine
        self.session = self.connection.session

    def create_table(self, tablename):
        if not self.engine.dialect.has_table(self.engine, f"{tablename}"):
            Base.metadata.tables[f"{tablename}"].create(self.engine)

    def create_all(self):
        Base.metadata.create_all(self.engine, Base.metadata.tables.values(), checkfirst=True)

    def add_total_req(self, count):
        total_req_count = TotalRequests(count=count)
        self.session.add(total_req_count)
        self.session.commit()

    def add_requests_type_count(self, count_by_type):
        for req_type, count in count_by_type.items():
            self.session.add(CountByType(type=req_type, count=count))
        self.session.commit()

    def add_top_requests_by_size(self, top_requests):
        for url, code, size in top_requests:
            self.session.add(TopRequestsBySize(url=url, status_code=code, size=size))
        self.session.commit()

    def add_req_with_client_error(self, freq_requests):
        for ip, code, url in freq_requests:
            self.session.add(FreqRequestsWithClientError(ip=ip, status_code=code, url=url))
        self.session.commit()

    def add_req_with_server_error(self, top_requests):
        for ip, code, url in top_requests:
            self.session.add(TopRequestsWithServerError(ip=ip, status_code=code, url=url))
        self.session.commit()
