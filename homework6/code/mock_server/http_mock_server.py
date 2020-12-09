import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading


class MockHandleRequests(BaseHTTPRequestHandler):
    valid_users = []

    def _set_good_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _set_bad_headers(self):
        self.send_response(401)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _set_bad_data_headers(self):
        self.send_response(400, 'Bad request data')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_good_headers()
        if self.path == '/get_valid_users':
            users = ','.join(self.valid_users)
            resp_str = f'Valid users are {users}'
            self.wfile.write(resp_str.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        if self.path == '/set_valid_users':
            self.set_valid_users(body)
        elif self.path == '/check_user':
            self.check_user(body)
        elif self.path == '/delete_user':
            self.delete_user(body)
        else:
            self.send_response(400, 'Bad request')

    def do_PUT(self):
        self.do_POST()

    def set_valid_users(self, body):
        try:
            self._set_good_headers()
            for u in body.decode().split(','):
                self.valid_users.append(u)
            resp_str = f'Users {body.decode()} are valid now'
            self.wfile.write(resp_str.encode())
        except ValueError:
            self._set_bad_data_headers()

    def check_user(self, body):
        try:
            user = body.decode()
            if user in self.valid_users:
                self._set_good_headers()
                resp_str = f'User {user} is valid'
                self.wfile.write(resp_str.encode())
            else:
                self._set_bad_headers()
                resp_str = f'User {user} is not valid'
                self.wfile.write(resp_str.encode())
        except ValueError:
            self._set_bad_data_headers()

    def delete_user(self, body):
        try:
            user = body.decode()
            if user in self.valid_users:
                self.valid_users.remove(user)
                self._set_good_headers()
                resp_str = f'User {user} deleted from valid users'
                self.wfile.write(resp_str.encode())
            else:
                self.send_response(400, f'No user {user} in valid users')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
        except ValueError:
            self._set_bad_data_headers()


class MockHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = MockHandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever, daemon=True)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

    def set_data(self, data):
        self.handler.valid_users = list(data)