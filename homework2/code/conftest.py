from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--br_version", default="latest")
    parser.addoption("--url", default="https://target.my.com")
    parser.addoption("--selenoid", default="")


@pytest.fixture(scope="session")
def config(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--br_version")
    url = request.config.getoption("--url")
    remote_server = "http://"+request.config.getoption("--selenoid")+"/wd/hub/"
    email = "berdetogni@nedoz.com"
    password = "a12345"
    return {"browser": browser, "version": version, "url": url, "remote_server": remote_server,
            "email": email, "password": password}
