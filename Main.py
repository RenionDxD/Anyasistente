############FUNCION DE MENU######################
def JUNO(con):
 import funciones_basicas.Funciones_voz as Fv 
 import funciones_basicas.Funciones as FJ  
 import conexiones.tcpclienttest.main as tcp
 import conexiones.tcpclienttest.cliente_compu as tcp
 import threading
 import alarma as al
 while True:
    llamado = Fv.Atencion()
    #llamado = 'ania'
    print(llamado)
    if 'ania' in llamado:
        rec = Fv.listen(con)
        #rec = "reproduce juegagerman en con claudio"
        print(rec)
        if 'reproduce' in rec:
            #FJ.reproduceY(rec)
            instruction,ip = FJ.session(rec)
            print(instruction,ip)
            tcp.tcpCompus(instruction,ip)
        elif 'hora' in rec:
            FJ.hora()
        elif 'busca' in rec:
            FJ.buscaW(rec)
        elif 'mensaje' in rec:
            sonido.contacto()
            contacto = Fv.MensajesVoz()
            sonido.mensaje()
            mensaje = Fv.MensajesVoz()
            orden = f'{contacto}|{mensaje}'
            tcp.tcpCompus(orden+"localhost")
            #if 'mensaje' in rec:
             #   rec = rec.replace('mensaje','')
            #with open('contactos_What.json','r') as contenido:
             #   FJ.mensajes(rec,contenido.read())
        elif 'alarma' in rec:
            alar = rec.replace('alarma', '')
            #alar = "01:49"
            thread = threading.Thread(target=al.programar_ala, args=(alar,))
            thread.start()
        elif 'protocolo' in rec:
            print("hola1")
            rec = rec.replace('protocolo ', '')
            print("lkfnwoedfnw")
            FJ.protocolo(rec)
        elif 'adiós' in rec:
            #Fv.habla("hasta luego señor")
            break
        elif 'encender' in rec or 'apagar' in rec or 'abrir' in rec or 'cerrar' in rec:
            print("puta madre")
            FJ.operaciones(rec)
        else:
          #conversacion(rec)
          print("no llamaste a nada")
    elif 'siri' in llamado:
            sonido.siri()
    else:
        print("fin de esuchar")
        sonido.INICIANDO()
            

##########FUNCION PRINCIPAL#############
from socket import create_connection, gethostbyname
import funciones_basicas.sonidos  as sonido
import speech_recognition as sr  
if __name__ == '__main__':
   JUNO(True) 
   def conexion():
     try:
        sonido.CARGANDO() 
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()
        return sonido.ENTRADA(), JUNO(True)
     except sr.UnknownValueError:
        return "algo fallo"
     except:
        return sonido.No_internet(),sonido.SALIDA(), JUNO(False)          
#conexion()
        