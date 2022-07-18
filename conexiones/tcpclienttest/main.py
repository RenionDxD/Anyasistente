import socket
import funciones_basicas.Funciones_voz as Fv
import conexiones.tcpclienttest.seewping as seew
from dotenv import dotenv_values
import os

config = dotenv_values(".env")

def tcpclient(orden,modulo,coordenada):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (os.getenv('ESP1IP'), 50001)
    print('connecting to ' + server_address[0])
    sock.connect(server_address)

    try:
        print(orden,modulo,coordenada)
        message = f'{orden}|{modulo}|{coordenada}'.encode('utf8')
        
        sock.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            print('received')
    except: 
        Fv.habla("uy ocurrio un error a conectarme a tu casa")
        sock.close()
    finally:
        print('closing socket')
        sock.close()


