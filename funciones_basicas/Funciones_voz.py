import speech_recognition as sr
import subprocess as sub




nombre = 'juno'
r = sr.Recognizer()
s = sr.Recognizer()


##########FUNCIONES DE ENTRADA Y SALIDA DE VOZ############

def habla(rec):
    command = f'gtts-cli -l es -t com "{rec}" | play -q -t mp3 - tempo 1.3 '
    sub.run([command], shell=True)

def MensajesVoz():
    try:
        with sr.Microphone() as source:
            habla("Escuchando...2")
            r.adjust_for_ambient_noise(source, 1)
            audio = s.listen(source)
            mes = s.recognize_google(audio, language="es")
            mes = mes.lower()
    except: 
            habla('Perdona no pude entenderte')
            
    return mes    

def listen():
    rec = ""
    try:
        with sr.Microphone() as source:
                habla("te escucho")
                r.adjust_for_ambient_noise(source, 1)
                audio = r.listen(source)
                rec = r.recognize_google(audio, language="es")
                rec = rec.lower()
                if nombre in rec:
                    rec = rec.replace(nombre, '')
                    print(rec)
    except sr.UnknownValueError:
         print("no se entendio")
         habla('Perdona no pude entenderte')
         print("")
    except: 
          habla('Perdona no pude entenderte')
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
