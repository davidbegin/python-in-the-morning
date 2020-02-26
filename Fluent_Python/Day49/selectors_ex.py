print("\033c")

import selectors
import socket

# This helps us with I/O Multiplexing???
sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, _read)

def _read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


def main():
    while True:
        events = sel.select()
        # What do key and mask mean
        for key, mask in events:
            # key has an attribute data....thats a callback???
            callback = key.data
            callback(key.fileobj, mask)


if __name__ == "__main__":
    sock = socket.socket()
    sock.bind(('localhost', 1234))
    # I think listen 100, is waiting or how much to data to take
    sock.listen(100)
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)

    main()
