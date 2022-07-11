############FUNCION DE MENU######################
from bot import habla


def JUNO():
 import funciones_basicas.Funciones_voz as Fv 
 import funciones_basicas.Funciones as FJ  
 import conexiones.tcpclienttest.main as tcp
 while True:
    llamado = Fv.Atencion()
    print(llamado)
    if 'ania' in llamado:
        rec = Fv.listen()
        print(rec)
        if 'reproduce' in rec:
            FJ.reproduceY(rec)
        elif 'tiempo' in rec:
            FJ.hora()
        elif 'busca' in rec:
            FJ.buscaW(rec)
        elif 'mensaje' in rec:
            if 'mensaje' in rec:
                rec = rec.replace('mensaje','')
            with open('contactos_What.json','r') as contenido:
                FJ.mensajes(rec,contenido.read())
        elif 'alarma' in rec:
            import threading
            import alarma as al
            alar = rec.replace('alarma', '')
            #alar = "01:49"
            thread = threading.Thread(target=al.programar_ala, args=(alar,))
            thread.start()
        elif 'ayuda' in rec:
            hel = rec.replace('ayuda', '')
            help()
        elif 'crear protocolo' in rec:
            print("protocolo")
        elif 'adiós' in rec:
            Fv.habla("hasta luego señor")
            break
        elif 'encender' in rec:
            rec = rec.split(' ')
            modulo = rec[-1]
            orden = rec[0]
            Fv.habla("encendiendo"+modulo)
            tcp.tcpclient(orden,modulo)
        elif 'apagar' in rec:
            rec = rec.split(' ')
            modulo = rec[-1]
            orden = rec[0]
            Fv.habla("apagando"+modulo)
            tcp.tcpclient(orden,modulo)
        elif 'abrir' in rec:
            rec = rec.split(' ')
            modulo = rec[-1]
            orden = rec[0]
            Fv.habla("abriendo"+modulo)
            tcp.tcpclient(orden,modulo)
        elif 'cerrar' in rec:
            rec = rec.split(' ')
            modulo = rec[-1]
            orden = rec[0]
            Fv.habla("cerrarando"+modulo)
            tcp.tcpclient(orden,modulo)
        else:
          print("kkkkkkkkk")
    else:
        print("")
            

##########FUNCION PRINCIPAL#############
from socket import create_connection, gethostbyname
import funciones_basicas.sonidos  as sonido
import speech_recognition as sr  
if __name__ == '__main__':
   def conexion():
     try:
        sonido.CARGANDO() 
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()
        return sonido.ENTRADA(), JUNO()
     except sr.UnknownValueError:
        return "algo fallo"
     except:
        return sonido.No_internet(),sonido.SALIDA()           
conexion()
        