from distutils.util import execute
from time import sleep
import speech_recognition as sr
import subprocess as sub
import jsons.des_cod as frase
from . import Record
import funciones_basicas.sonidos  as sonido

nombre = 'juno'
r = sr.Recognizer()
s = sr.Recognizer()


##########FUNCIONES DE ENTRADA Y SALIDA DE VOZ############

def habla(rec):
    command = f'gtts-cli -l es -t com "{rec}" | play -q -t mp3 - tempo 1.3 '
    sub.run([command], shell=True)


def MensajesVoz():
    try:
        # with sr.Microphone() as source:
        #    habla("Escuchando...2")
        #    r.adjust_for_ambient_noise(source, 1)
        #    audio = s.listen(source)
        data = Record.listen()
        mes = s.recognize_google(data, language="es")
        mes = mes.lower()
    except:
        habla('Perdona no pude entenderte')

    return mes


def listen(con):
    rec = ""
    try:
        # with sr.Microphone() as source:
        #    habla(frase.palabras("te_escucho"))
        #    r.adjust_for_ambient_noise(source, 1)
        #    audio = r.listen(source)
        sonido.te_escucho()
        data = Record.listen()
        rec = r.recognize_google(data, language="es")
        rec = rec.lower()
        if nombre in rec:
            rec = rec.replace(nombre, '')
            print(rec)
    except sr.UnknownValueError:
        print("no se entendio")
        if con :
            habla(frase.palabras("no_entiendo"))
        else:
            sonido.No_entiendo()
    except:
        if con:
            habla(frase.palabras("no_entiendo"))
        else:
           sonido.No_entiendo() 
    return rec


def Atencion():
    llamado = ""
    try:
        # with sr.Microphone() as source:
        #        print("escuchando....")
        #        r.adjust_for_ambient_noise(source, 1)
        #        audio = r.listen(source)
        data = Record.listen()
        llamado = r.recognize_google(data, language="es")
        llamado = llamado.lower()
        if nombre in llamado:
            llamado = llamado.replace(nombre, '')
            print(llamado)
    except sr.UnknownValueError:
        print("No se entendio lo que dijiste")
    except:
        print("B")
    return llamado
