import Main 
import datetime,keyboard
from pygame import mixer 
import time
import sys


def programar_ala(alar):
    print("carajo")
    alar = alar.strip()
    while True:
        if datetime.datetime.now().strftime('%H:%M') == alar:
           print("hhhhhhhhhhhhhhh") 
           mixer.init()
           mixer.music.load("rasputin-boney-m-sub-espanol.mp3")
           mixer.music.play()
           time.sleep(20)
           mixer.music.stop()
           break  

if __name__ == '__main__':
 alar = sys.argv[1]
 programar_ala(alar)