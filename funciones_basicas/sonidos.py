from pygame import mixer
import pygame
import time


mixer.init()

def ENTRADA():
    mixer.music.load('sounds/ENTRADA.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(10)
    exit

def SALIDA():
    mixer.music.load('sounds/SALIDA.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(10)
    
def CARGANDO():
    mixer.music.load('sounds/CARGANDO.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(10)
    
def ATENCION():
    mixer.music.load('sounds/ATENCION.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(10)
    
def ERROR():
    mixer.music.load('sounds/ERROR.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(10)   
    
def ESCANEANDO():
    mixer.music.load('sounds/ESCANEANDO.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(10)
    
def FIN():
    mixer.music.load('sounds/FIN.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(10)

def INICIANDO():
    mixer.music.load('sounds/INICIANDO.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(10)
    
    