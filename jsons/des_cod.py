import json
import random

def palabras(palabra):
    with open('jsons/frases.json','r') as contenido:  
     frase = json.loads(contenido.read())[palabra][str(random.randint(0, 3))] 
    return frase

