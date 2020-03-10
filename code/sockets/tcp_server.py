#!/usr/bin/env python3

import socket
import selectors
import types
from dataclasses import dataclass

HOST = "127.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

@dataclass
class ClientData():
    addr: str
    inb: bytes
    outb: bytes


sel = selectors.DefaultSelector()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
s.setblocking(False)
sel.register(s, selectors.EVENT_READ, data=None)


def accept_wrapper(sock):
    # Like regular TCP setup
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)

    # Again we say setblocking
    conn.setblocking(False)

    # data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    data = ClientData(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)



def service_connection(key, mask):
    sock = key.fileobj

    # This is the data class
    data = key.data

    # Sometimes mask will be None or False?
    # why?
    if mask & selectors.EVENT_READ:
	# 2048?
        recv_data = sock.recv(1024)  # Should be ready to read

        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()


    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]


# Event Loop
while True:
    events = sel.select(timeout=None)

    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)



