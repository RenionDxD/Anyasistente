import funciones_basicas.sonidos  as sonido
import funciones_basicas.Funciones_voz as Fv 
import funciones_basicas.Funciones as FJ 


                

############FUNCION DE MENU######################
def JUNO():
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
                datos = contenido.read()
                FJ.mensajes(rec,datos)
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
       # elif 'hablar' in rec:
        #    bot.habla()
        elif 'crear protocolo' in rec:
            print("protocolo")
        elif 'adiós' in rec:
            Fv.habla("hasta luego señor")
            break
        #else
        # protocolos()
    else:
        print("")

##########FUNCION PRINCIPAL#############
from socket import create_connection, gethostbyname
if __name__ == '__main__':
   def conexion():
     try:
        sonido.CARGANDO() 
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()
        return sonido.ENTRADA(), JUNO()
     except:
        return sonido.No_internet(),sonido.SALIDA()           
conexion()
        