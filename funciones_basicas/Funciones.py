from bot import habla
import funciones_basicas.Funciones_voz as Fv 
import pywhatkit, datetime, wikipedia, json
from numpy import empty

#############FUNCIONES DE JUNO######################  

def help():
    Fv.habla("Mi nombre es yuno 0.0.1 y puedo ayudarte en lo que sea........ si quieres que te reproduzca algo en youtube me puedes decir reproduce .............si quieres que te diga la hora dime tiempo....... si quieres bucar algo en wikipedia dime... yuno busca si quieres que le mande un mensaje a alguien dime mensaje y yo te ayudo........tambien puedo programar alarmas..... y basta con que me digas alarma y a la hora que quieres que te despierte.......yo me encargo de todo..........siempre a tu servicios")

def contactos(datos):
        objecto = empty
        objecto = json.loads(datos)
        u = Fv.listen()
        f = objecto[u]
        g = f["Tel"]
        print(g)
        return g


def reproduceY(rec):
    music = rec.replace('reproduce', '')
    Fv.habla('reproduciendo' + music)
    pywhatkit.playonyt(music)

def buscaW(rec):
    order = rec.replace('busca', '')
    wikipedia.set_lang("es")
    info = wikipedia.summary(order, 2)
    Fv.habla(info)

def hora():
     hora = datetime.datetime.now().strftime('%I:%M %p')
     Fv.habla("son las "+hora)

def mensajes(rec,datos): 
        Fv.habla("a quien deseas enviar el mensaje?")       
        contacto = contactos(datos)
        Fv.habla("cual es el mensaje que deseas enviar?")
        mensaje = Fv.listen()
        try:
            pywhatkit.sendwhatmsg_instantly("+521618"+contacto,
            mensaje)
            Fv.habla("enviando..........")
            Fv.habla("El mensaje a "+ rec + "fue enviado exitosamente")
        except:
            Fv.sonido.error()
            habla("no se pudo encontrar")