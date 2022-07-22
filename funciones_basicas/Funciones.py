from dis import Instruction
import funciones_basicas.Funciones_voz as Fv 
import json
import conexiones.tcpclienttest.main as tcps
import speech_recognition as sr
import pdb
import funciones_basicas.sonidos  as son
import conexiones.tcpclienttest.cliente_compu as tcp
from jsons.des_cod import palabras

#############FUNCIONES DE JUNO######################  

def help():
    Fv.habla("Mi nombre es yuno 0.0.1 y puedo ayudarte en lo que sea........ si quieres que te reproduzca algo en youtube me puedes decir reproduce .............si quieres que te diga la hora dime tiempo....... si quieres bucar algo en wikipedia dime... yuno busca si quieres que le mande un mensaje a alguien dime mensaje y yo te ayudo........tambien puedo programar alarmas..... y basta con que me digas alarma y a la hora que quieres que te despierte.......yo me encargo de todo..........siempre a tu servicios")

def contactos(datos):
        person = Fv.listen()
        contacto = json.loads(datos)[person]["Tel"] 
        return contacto,person


def reproduceY(rec):
    music = rec.replace('reproduce', '')
    Fv.habla('reproduciendo' + music)
    #pywhatkit.playonyt(music)

def buscaW(rec):
    import wikipedia
    order = rec.replace('busca', '')
    wikipedia.set_lang("es")
    info = wikipedia.summary(order, 2)
    Fv.habla(info)

def hora():
     import datetime
     hora = datetime.datetime.now().strftime('%I:%M %p')
     Fv.habla("son las "+hora)

def mensajes(rec,datos): 
        Fv.habla("a quien deseas enviar el mensaje?")       
        contacto,persona = contactos(datos)
        Fv.habla("cual es el mensaje que deseas enviar?")
        mensaje = Fv.listen()
        try:
            #pywhatkit.sendwhatmsg_instantly("+521618"+contacto,
            #mensaje)
            Fv.habla("enviando..........")
            Fv.habla("El mensaje a "+ persona + "fue enviado exitosamente")
        except:
            Fv.sonido.error()
            Fv.habla("no se pudo encontrar")

def operaciones(rec):
            endo = ""
            coordenada = ""
            #enciende luces cuarto uno 
            #en|lu|cuar
            #abr|cocher
            rec = rec.split(' ')
            modulo = ""
            try:
                modulo = rec[1]
            except:
                print("no hay modulo")
            orden = rec[0]
            coordenada = ""
            try:
                coordenada = rec[2]
                print(coordenada)
            except:
                print()
            
            print(orden+ " " +modulo+" "+coordenada+" cagada")
            if orden == 'encender':
                endo = "encendiendo"
                son.encendiendo()
            elif orden == 'apagar':
                endo = "apagando"
                son.apagando()
            elif orden == 'abrir':
                endo = "abriendo"
                son.abriendo()
            elif orden == 'cerrar':
                endo = "cerrando"
                son.cerrando()

            if modulo == 'luces':
                son.luces()
            elif modulo == 'cochera':
                son.cochera()
            elif modulo == 'puerta':
                son.puerta()
            
            if coordenada == 'cuarto':
                print()
                son.cuarto()
            elif coordenada == 'almacén"':
                print()
                son.almacen()
            elif coordenada == 'principal':
                print()
                son.principal()
            elif coordenada == 'trasera':
                print()
                son.trasera()
            elif coordenada == 'sala':
                print()
                son.sala()
            #Fv.habla(endo+" "+modulo)
            try:
             tcps.tcpclient(orden,modulo,coordenada)
            except:
                #Fv.habla("uy ocurrio un error a conectarme a tu casa")#
                print("error en try operaciones()")
                son.error_casa_con()


def crear_protocolo():
 print("hola crear")


def protocolo(rec):
    with open('jsons/operac_casa.json','r') as contenido:
       datos  = contenido.read()
    for i in range (0,5):
        link = ""
        contacto = json.loads(datos)[rec][str(i)]
        print(contacto)
        if 'youtube' in contacto:
            link = contacto.replace('youtube ', '')
            complet = "reproduce "+link
            tcp.tcpCompus(complet,"192.168.43.34")
        operaciones(contacto)


def session(rec):
    print("la sesion se ha iniciado")
    rec = rec.split(' ')
    instruction = rec
    sesion=rec[-1]
    if sesion == 'ricardo':
        print("ricardo")
        ip = "192.168.43.34"
        return instruction,ip
    elif sesion == 'celular':
        print("celular")
        ip = "192.168.43.181"
        print(instruction)
        return instruction,ip
    elif sesion == 'yahir':
        print("jair")
        ip = "172.20.10.8"
        return instruction,ip
    else:
        ip = "192.168.43.34"
        return instruction,ip
