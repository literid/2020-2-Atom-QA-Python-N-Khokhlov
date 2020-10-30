import pytest
from api.my_target_client import MyTargetClient
import string
import random


@pytest.fixture(scope="function")
def api_client():
    user = "berdetogni@nedoz.com"
    password = "a12345"
    return MyTargetClient(user, password)


@pytest.fixture(scope="function")
def seg_name(length=7):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
