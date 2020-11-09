import pytest
import requests
import json
from application import atom
from mock_server.http_mock_server import MockHTTPServer
from socket_client.http_socket_client import SocketClient
from tests.settings import MOCK_HOST, MOCK_PORT, APP_HOST, APP_PORT, APP_SHUTDOWN_URL


@pytest.fixture(scope='session')
def mock():
    server = MockHTTPServer(MOCK_HOST, MOCK_PORT)
    atom.run_app()
    server.start()
    yield server
    server.stop()
    requests.get(APP_SHUTDOWN_URL)


@pytest.fixture(scope='function')
def client():
    from time import sleep
    sleep(1)
    client = SocketClient(APP_HOST, APP_PORT)
    client.connect()
    yield client
    client.disconnect()


def test_set_users(mock, client: SocketClient):
    mock.set_data([])
    data = "Nikolai,Dima"
    headers = {'Content-Type': "application/x-www-form-urlencoded",
               'Content-Length': str(len(data.encode()))}
    resp = client.send_post_request(headers=headers, path="/set_valid_users", data=data)

    assert json.loads(resp)[0].split()[1] == '200'
    assert json.loads(resp)[-1].strip('\"') == f"Users {data} now valid users"
    mock.set_data([])


def set_default_mock_data(mock: MockHTTPServer, data):
    mock.set_data([])
    data = "Nikolai,Dima"
    mock.set_data(data.split(','))


def test_get_users(mock, client: SocketClient):
    users = "Nikolai,Dima"
    set_default_mock_data(mock, users)
    resp = client.send_get_request(headers=None, path="/get_valid_users")

    assert json.loads(resp)[0].split()[1] == '200'
    assert json.loads(resp)[-1].strip('\"') == f"Valid users are {users}"
    mock.set_data([])


def test_valid_user(mock, client: SocketClient):
    users = "Nikolai,Dima"
    set_default_mock_data(mock, users)
    check_user = 'Dima'
    headers = {'Content-Type': "application/x-www-form-urlencoded",
               'Content-Length': str(len(check_user.encode()))}
    resp = client.send_post_request(headers=headers, path=f"/check_user/{check_user}", data=check_user)
    assert json.loads(resp)[0].split()[1] == '200'
    assert json.loads(resp)[-1].strip('\"') == f"User {check_user} has permissions"
    mock.set_data([])


def test_invalid_user(mock, client: SocketClient):
    users = "Nikolai,Dima"
    set_default_mock_data(mock, users)
    check_user = 'Stas'
    headers = {'Content-Type': "application/x-www-form-urlencoded",
               'Content-Length': str(len(check_user.encode()))}
    resp = client.send_post_request(headers=headers, path=f"/check_user/{check_user}", data=check_user)

    assert json.loads(resp)[0].split()[1] == '401'
    assert json.loads(resp)[-1].strip('\"') == f"User {check_user} has no permissions"
    mock.set_data([])


def test_delete_valid_user(mock, client: SocketClient):
    users = "Nikolai,Dima"
    set_default_mock_data(mock, users)
    del_user = 'Dima'
    headers = {'Content-Type': "application/x-www-form-urlencoded",
               'Content-Length': str(len(del_user.encode()))}
    resp = client.send_post_request(headers=headers, path=f"/delete_user", data=del_user)

    assert json.loads(resp)[0].split()[1] == '200'
    assert json.loads(resp)[-1].strip('\"') == f"Deleted user {del_user} from valid users"
    mock.set_data([])


def test_delete_invalid_user(mock, client):
    users = "Nikolai,Dima"
    set_default_mock_data(mock, users)
    del_user = 'Stas'
    headers = {'Content-Type': "application/x-www-form-urlencoded",
               'Content-Length': str(len(del_user.encode()))}
    resp = client.send_post_request(headers=headers, path=f"/delete_user", data=del_user)

    assert json.loads(resp)[0].split()[1] == '400'
    assert json.loads(resp)[-1].strip('\"') == f"No user {del_user} in valid users"
    mock.set_data([])
