from urllib.parse import urljoin

APP_HOST = '127.0.0.1'
APP_PORT = 1050
APP_URL = f'http://{APP_HOST}:{APP_PORT}'
APP_SHUTDOWN_URL = urljoin(APP_URL, 'shutdown')

MOCK_HOST = '127.0.0.1'
MOCK_PORT = 1052
MOCK_URL = f'http://{MOCK_HOST}:{MOCK_PORT}'
MOCK_VALID_CHECK_URL = urljoin(MOCK_URL, 'check_user')
MOCK_SET_VALID_USER_URL = urljoin(MOCK_URL, 'set_valid_users')
MOCK_GET_VALID_USER_URL = urljoin(MOCK_URL, 'get_valid_users')
MOCK_DELETE_VALID_USER_URL = urljoin(MOCK_URL, 'delete_user')
