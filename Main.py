from asyncio import subprocess
from os import popen
import string
import funciones_basicas.sonidos as sonido
import funciones_basicas.Funciones_voz as Fv 
import funciones_basicas.Funciones as FJ
import alarma, bot 
import subprocess as sub
#from subprocess import Popen

                

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
            alar = rec.replace('alarma', '')
            #alarma.programar_ala(alar)  
            sub.Popen(['/home/ricardo/proyecto/Anyasistente/alarma.py', alar])
            #sub.run(["python ./alarma.py", alar])
        elif 'ayuda' in rec:
            hel = rec.replace('ayuda', '')
            help()
        elif 'hablar' in rec:
            bot.habla()
        elif 'crear protocolo' in rec:
            print("protocolo")
        elif 'adiós' in rec:
            Fv.talk("hasta luego señor")
            break
        #else
        # protocolos()
    else:
        print("")

##########FUNCION PRINCIPAL#############

if __name__ == '__main__':
    print("inicializando a JUNO...")  
    sonido.CARGANDO() 
    sonido.ENTRADA() 
    JUNO()
    sonido.SALIDA()   
    

        