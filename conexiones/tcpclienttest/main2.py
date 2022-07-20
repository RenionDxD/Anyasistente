import socket
import pywhatkit

def tcpserver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    print('starting up on ' + server_address[0])
    sock.bind(server_address)

    sock.listen(1)

    msg = ""
    while True:
        print('waiting for a connection')
        connection, client_address = sock.accept()

        try:
            print('connection', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                msg += data.decode('utf8')
                print('received', msg)
                if data:
                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print('no more data from client')
                    break
        finally:
            # Clean up the connection
            connection.close()
            #msg = msg.split('|')
            print(msg)

if __name__ == '__main__':
    tcpserver()
