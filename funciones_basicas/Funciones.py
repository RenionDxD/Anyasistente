import funciones_basicas.Funciones_voz as Fv 
import pywhatkit, json
import conexiones.tcpclienttest.main as tcp
import speech_recognition as sr

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
    pywhatkit.playonyt(music)

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
            pywhatkit.sendwhatmsg_instantly("+521618"+contacto,
            mensaje)
            Fv.habla("enviando..........")
            Fv.habla("El mensaje a "+ persona + "fue enviado exitosamente")
        except:
            Fv.sonido.error()
            Fv.habla("no se pudo encontrar")

def operaciones(rec):
            endo = ""
            rec = rec.split(' ')
            modulo = rec[-1]
            orden = rec[0]
            if orden == 'encender':
                endo = "encendiendo"
            elif orden == 'apagar':
                endo = "apagando"
            elif orden == 'abrir':
                endo = "abriendo"
            elif orden == 'cerrar':
                endo = "cerrando"
            Fv.habla(endo+" "+modulo)
            try:
             tcp.tcpclient(orden,modulo)
            except:
                Fv.habla("uy ocurrio un error a conectarme a tu casa")


def crear_protocolo():
 print("hola crear")


def protocolo(rec):
    with open('jsons/operac_casa.json','r') as contenido:
       datos  = contenido.read()
    for i in range (0,2):
        i = str(i)
        contacto = json.loads(datos)[rec][i]
        operaciones(contacto)
