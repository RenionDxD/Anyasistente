############FUNCION DE MENU######################
def JUNO():
 import funciones_basicas.Funciones_voz as Fv 
 import funciones_basicas.Funciones as FJ  

 while True:
    #llamado = Fv.Atencion()
    llamado = "ania"
    print(llamado)
    if 'ania' in llamado:
        rec = Fv.listen()
        #rec = "apagar luces"
        print(rec)
        if 'reproduce' in rec:
            FJ.reproduceY(rec)
        elif 'hora' in rec:
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
        elif 'crear' in rec:
            print("entra a crear")
        elif 'protocolo' in rec:
            print("hola1")
            rec = rec.replace('protocolo ', '')
            print("lkfnwoedfnw")
            FJ.protocolo(rec)
        elif 'adiós' in rec:
            Fv.habla("hasta luego señor")
            break
        elif 'encender' in rec or 'apagar' in rec or 'abrir' in rec or 'cerrar' in rec:
            print("puta madre")
            FJ.operaciones(rec)
        else:
          #conversacion(rec)
          print("hhhh")
    else:
        print("lllll")
            

##########FUNCION PRINCIPAL#############
from socket import create_connection, gethostbyname
import funciones_basicas.sonidos  as sonido
import speech_recognition as sr  
if __name__ == '__main__':
   JUNO()
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
#conexion()
        