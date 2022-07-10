import speech_recognition as sr
import subprocess as sub
import pyttsx3



nombre = 'juno'
r = sr.Recognizer()
s = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)


##########FUNCIONES DE ENTRADA Y SALIDA DE VOZ############
def talk(rec):
    engine.say(rec)
    engine.runAndWait()

def MensajesVoz():
    try:
        with sr.Microphone() as source:
            talk("Escuchando...2")
            r.adjust_for_ambient_noise(source, 1)
            audio = s.listen(source)
            mes = s.recognize_google(audio, language="es")
            mes = mes.lower()
    except: 
            talk('Perdona no pude entenderte')
            
    return mes    

def listen():
    rec = ""
    try:
        with sr.Microphone() as source:
                talk("te escucho")
                r.adjust_for_ambient_noise(source, 1)
                audio = r.listen(source)
                rec = r.recognize_google(audio, language="es")
                rec = rec.lower()
                if nombre in rec:
                    rec = rec.replace(nombre, '')
                    print(rec)
    except sr.UnknownValueError:
         print("no se entendio")
         talk('Perdona no pude entenderte')
         print("")
    except: 
          talk('Perdona no pude entenderte')
          print("")
    return rec


def Atencion():
    llamado = ""
    try:
        with sr.Microphone() as source:
                print("hola")
                r.adjust_for_ambient_noise(source, 1)
                audio = r.listen(source)
                llamado = r.recognize_google(audio, language="es")
                llamado = llamado.lower()
                if nombre in llamado:
                    llamado = llamado.replace(nombre, '')
                    print(llamado)
    except sr.UnknownValueError:
         print("A")
    except: 
          print("B")
    return llamado
