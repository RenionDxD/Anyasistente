import socket
import funciones_basicas.Funciones_voz as Fv
import conexiones.tcpclienttest.seewping as seew
from dotenv import dotenv_values
import os
import traceback
import funciones_basicas.sonidos  as son

config = dotenv_values(".env")

def tcpCompus(rec,ip):
 try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(6)
    server_address = (ip, 10000)#50001)
    print('connecting to ' + server_address[0])
    sock.connect(server_address)
    try:
        print(rec)
        message = f'{rec}'.encode('utf8')
        print(message)
        
        sock.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            print('received')
    except Exception:
        traceback.print_exc()
        #Fv.habla("uy ocurrio un error a conectarme a tu casa pppppppp")
        son.error_dis()
        sock.close()
    finally:
        print('closing socket')
        sock.close()
 except:
    son.error_dis()