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
            r.adjust_for_ambient_noise(source, duration = 1)
            audio = s.listen(source)
            mes = s.recognize_google(audio, language="es")
            mes = mes.lower()
    except: 
            talk('Perdona no pude entenderte')
            
    return mes    

def listen():
    try:
        with sr.Microphone() as source:
                talk("te escucho")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
                rec = r.recognize_google(audio, language="es")
                rec = rec.lower()
                if nombre in rec:
                    rec = rec.replace(nombre, '')
                    print(rec)
    except: 
            talk('Perdona no pude entenderte')
            
    return rec