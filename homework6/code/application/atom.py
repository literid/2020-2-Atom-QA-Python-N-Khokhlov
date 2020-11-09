import threading
import requests
from flask import Flask, request
from tests import settings

app = Flask(__name__)
DATA = {}


def run_app():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.APP_HOST, 'port': settings.APP_PORT
    })
    server.start()
    return server


def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_app()


@app.route('/')
def index():
    return "Index page"


@app.route('/set_valid_users', methods=["POST"])
def set_users():
    users = request.get_data().decode()
    mock_response = requests.post(url=f'{settings.MOCK_SET_VALID_USER_URL}', data=users)
    if mock_response.status_code == 400:
        return f'Users {users} were not set as valid', 400
    elif mock_response.status_code == 200:
        return f'Users {users} now valid users', 200


@app.route('/check_user/<user>', methods=["POST"])
def check_user(user):
    mock_response = requests.post(url=settings.MOCK_VALID_CHECK_URL, data=user)
    if mock_response.status_code == 401:
        return f"User {user} has no permissions", 401
    elif mock_response.status_code == 200:
        return f"User {user} has permissions", 200


@app.route('/delete_user', methods=["POST"])
def delete_user():
    user = request.get_data().decode()
    mock_response = requests.post(url=settings.MOCK_DELETE_VALID_USER_URL, data=user)
    if mock_response.status_code == 400:
        if mock_response.reason == f'No user {user} in valid users':
            return f"No user {user} in valid users", 400
        else:
            return "Bad request data", 400
    elif mock_response.status_code == 200:
        return f"Deleted user {user} from valid users", 200


@app.route('/get_valid_users', methods=["GET"])
def get_valid_users():
    mock_response = requests.get(url=settings.MOCK_GET_VALID_USER_URL)
    if mock_response.status_code == 200:
        return mock_response.text, 200
    else:
        return "Bad request", 400
