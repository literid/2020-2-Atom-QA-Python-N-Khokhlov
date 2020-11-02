from mysql_orm_client.mysql_orm_client import MysqlOrmConnection
from logger.orm_builder import MysqlOrmBuilder
import os

dir_path = os.path.dirname(os.path.dirname(__file__))
file = open(os.path.join(dir_path, 'logger', 'access.log'), 'r')
requests = file.readlines()
for i in range(len(requests)):
    requests[i] = requests[i].split()
file.close()


def total():
    return len(requests)


def count_by_type(req_type):
    count = 0
    for req in requests:
        if req[5][1:] == req_type:
            count += 1
    return count


def requests_type_count():
    types = set()
    for req in requests:
        types.add(req[5][1:])
    result = dict()
    for type in types:
        result[type] = count_by_type(type)
    return result


def top_requests_by_size():
    sorted_req = sorted(requests,
                        key=lambda req: int(req[9].replace('-', '0')),
                        reverse=True)
    top_requests = []
    for i in range(10):
        new_req = (sorted_req[i][6], sorted_req[i][8], sorted_req[i][9])
        top_requests.append(new_req)
    return top_requests


def frequent_requests_with_client_error():
    url_to_count = dict()
    error_req = []
    result = []
    for req in requests:
        if (400 <= int(req[8]) < 500):
            error_req.append(req)
            if req[6] in url_to_count:
                url_to_count[req[6]] += 1
            else:
                url_to_count[req[6]] = 1
    url_to_count = {k: v for k, v in sorted(url_to_count.items(), key=lambda item: item[1], reverse=True)}

    urls = list(url_to_count.keys())[:10]
    for url in urls:
        for req in error_req:
            if req[6] == url:
                new_req = (req[0], req[8], req[6])
                result.append(new_req)
                break
    return result


def top_requests_by_size_with_server_error():
    error_req = []
    result = []
    for req in requests:
        if (500 <= int(req[8]) < 600):
            error_req.append(req)
    top_req = sorted(error_req, key=lambda req: int(req[9].replace("-", "0")), reverse=True)[:10]
    for i in range(10):
        new_req = (top_req[i][0], top_req[i][8], top_req[i][6])
        result.append(new_req)
    return result


def write_in_db():
    connection = MysqlOrmConnection(user='root', password='pass', db_name='ACCESS_LOGS')
    builder = MysqlOrmBuilder(connection=connection)
    builder.create_all()
    builder.add_total_req(total())
    builder.add_requests_type_count(requests_type_count())
    builder.add_top_requests_by_size(top_requests_by_size())
    builder.add_req_with_client_error(frequent_requests_with_client_error())
    builder.add_req_with_server_error(top_requests_by_size_with_server_error())


write_in_db()
