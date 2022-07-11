import socket


def tcpclient(orden,modulo):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    print('connecting to ' + server_address[0])
    sock.connect(server_address)

    try:
        print(orden,modulo)
        message = f'action|open|{orden}|{modulo}'.encode('utf8')

        sock.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            print('received')

    finally:
        print('closing socket')
        sock.close()


