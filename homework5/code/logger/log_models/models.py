from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class TotalRequests(Base):
    __tablename__ = 'request_count'
    __table_args__ = {'mysql_charset': 'utf8'}

    count = Column(Integer, nullable=False, primary_key=True)


class CountByType(Base):
    __tablename__ = 'count_by_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    type = Column(String(500), nullable=False, primary_key=True)
    count = Column(Integer, nullable=False)


class TopRequestsBySize(Base):
    __tablename__ = 'top_requests_by_size'
    __table_args__ = {'mysql_charset': 'utf8'}

    url = Column(String(100), nullable=False)
    status_code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False, primary_key=True)


class FreqRequestsWithClientError(Base):
    __tablename__ = 'freq_requests_with_client_error'
    __table_args__ = {'mysql_charset': 'utf8'}

    ip = Column(String(30), nullable=False)
    status_code = Column(Integer, nullable=False)
    url = Column(String(100), nullable=False, primary_key=True)


class TopRequestsWithServerError(Base):
    __tablename__ = 'top_requests_with_server_error'
    __table_args__ = {'mysql_charset': 'utf8'}

    ip = Column(String(30), nullable=False)
    status_code = Column(Integer, nullable=False)
    url = Column(String(500), nullable=False, primary_key=True)
