import funciones_basicas.sonidos  as sonido
import funciones_basicas.Funciones_voz as Fv 



                

############FUNCION DE MENU######################
def JUNO():
 while True:
    llamado = Fv.Atencion()
    print(llamado)
    if 'ania' in llamado:
        import funciones_basicas.Funciones as FJ 
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
            import subprocess as sub
            alar = rec.replace('alarma', '')
            #alarma.programar_ala(alar)  
            sub.Popen(['python', '/home/ricardo/proyecto/Anyasistente/alarma.py', alar])
            #sub.run(["python ./alarma.py", alar])
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

if __name__ == '__main__':
    print("inicializando a JUNO...")  
    Fv.habla("hola mucho gusto me llamo anya")
    sonido.No_internet()
    #sub.run('fish',shell=True)
    sonido.CARGANDO() 
    sonido.ENTRADA() 
    JUNO()
    sonido.SALIDA()   
    

        