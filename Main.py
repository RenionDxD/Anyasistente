import funciones_basicas.sonidos as sonido
import funciones_basicas.Funciones_voz as Fv 
import funciones_basicas.Funciones as FJ
import alarma, bot 
import subprocess as sub

                

############FUNCION DE MENU######################
def JUNO():
 while True:
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
        alarma.programar_ala(alar)  
    elif 'ayuda' in rec:
        hel = rec.replace('ayuda', '')
        help()
    elif 'hablar' in rec:
        bot.habla()
    elif 'adiós' in rec:
        Fv.talk("hasta luego señor")
        break

##########FUNCION PRINCIPAL#############

if __name__ == '__main__':
    print("inicializando a JUNO...")  
    sonido.CARGANDO() 
    sonido.ENTRADA() 
    JUNO()
    sonido.SALIDA()   
    

        