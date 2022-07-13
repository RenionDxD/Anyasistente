from distutils.util import execute
from time import sleep
import speech_recognition as sr
import subprocess as sub
import jsons.des_cod as frase
from . import Record

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
        mes = Record.listen()
        mes = s.recognize_google(mes, language="es")
        mes = mes.lower()
    except:
        habla('Perdona no pude entenderte')

    return mes


def listen():
    rec = ""
    try:
        # with sr.Microphone() as source:
        #    habla(frase.palabras("te_escucho"))
        #    r.adjust_for_ambient_noise(source, 1)
        #    audio = r.listen(source)
        rec = Record.listen()
        rec = r.recognize_google(rec, language="es")
        rec = rec.lower()
        if nombre in rec:
            rec = rec.replace(nombre, '')
            print(rec)
    except sr.UnknownValueError:
        print("no se entendio")
        habla(frase.palabras("no_entiendo"))
    except:
        habla(frase.palabras("no_entiendo"))
    return rec


def Atencion():
    llamado = ""
    try:
        # with sr.Microphone() as source:
        #        print("escuchando....")
        #        r.adjust_for_ambient_noise(source, 1)
        #        audio = r.listen(source)
        llamado = Record.listen()
        llamado = r.recognize_google(llamado, language="es")
        llamado = llamado.lower()
        if nombre in llamado:
            llamado = llamado.replace(nombre, '')
            print(llamado)
    except sr.UnknownValueError:
        print("No se entendio lo que dijiste")
    except:
        print("B")
    return llamado
