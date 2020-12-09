import socket
import json


class SocketClient:

    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client.settimeout(0.1)
        self.client.connect((self.target_host, self.target_port))

    def disconnect(self):
        self.client.close()

    def send_get_request(self, headers, path="/"):
        request = self.make_request(type='GET', headers=headers, path=path, data=None)
        self.client.send(request.encode())
        return self.data_receive()

    def send_post_request(self, headers, data, path="/"):
        request = self.make_request(type='POST', headers=headers, path=path, data=data)
        self.client.send(request.encode())
        return self.data_receive()

    def make_request(self, type, headers: dict, path, data=None):
        request = f"{type} {path} HTTP/1.1\r\nHost:{self.target_host}\r\n"
        if headers:
            for item in headers.items():
                request += item[0] + ":" + item[1] + "\r\n"
        if data:
            request += f"\r\n{data}"
        else:
            request += '\r\n'
        return request

    def data_receive(self):
        total_data = []
        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break
        data = ''.join(total_data).splitlines()
        return json.dumps(data)
