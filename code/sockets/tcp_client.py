import socket
from dataclasses import dataclass


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# PORT = 65433  # The port used by the server

messages = [b'Message 1 from client.', b'Message 2 from client.']

@dataclass
class Msg():
    connid: int
    messages: list
    recv_total: int = 0
    outb: bytes = b''

    def __post__init__(self):
        self.msg_total = sum(len(m) for m in self.messages)


def start_connections(host, port, num_conns):
    server_addr = (host, port)

    for i in range(0, num_conns):
        connid = i + 1
        print('starting connection', connid, 'to', server_addr)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.setblocking(False)

        sock.connect_ex(server_addr)

        events = selectors.EVENT_READ | selectors.EVENT_WRITE

        data = Msg(connid=connid, messages=list(messages))

        sel.register(sock, events, data=data)

start_connections(HOST, PORT, 5)
