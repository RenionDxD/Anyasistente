import Main 
import datetime,keyboard
from pygame import mixer 
import time

def programar_ala(alar):
    alar = alar.strip()
    Main.Fv.talk("alarma activada a las "+ alar +" Horas")
    while True:
        if datetime.datetime.now().strftime('%H:%M') == alar:
           Main.Fv.talk("DESPIERTAAAAAAAA!!!!") 
           mixer.init()
           mixer.music.load("rasputin-boney-m-sub-espanol.mp3")
           mixer.music.play()
           time.sleep(10)
           if keyboard.read_key() == "s":
               mixer.music.stop()
               break  

