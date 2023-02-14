# Imports van al inicio
from microbit import *
import random
import music

total_palabras = 9
vocales = ['A','E','I','O','U']
consonantes =['B', 'C','D','F','G','H','J','K','L','LL','M','N','Ñ', 'P', 'QU', 'R','S', 'T','V','W','X','Y','Z']

def obtenerVocal():
    return vocales[random.randint(0, len(vocales)-1)]

def obtenerConsonante():
    return consonantes[random.randint(0,len(consonantes)-1)]

def cronometro(t):
    for i in range(t, 0, -1):
        display.scroll(i)
        music.play("a3")
        sleep(1000)
    music.play(music.POWER_DOWN)
    display.show(Image.SWORD)

# Muestra '?', si se pulsa A devolverá vocal, si se pulsa B devolverá consonante
while total_palabras>0:
    if button_a.was_pressed():
        display.show(obtenerVocal())
        sleep(1000)
        total_palabras = total_palabras - 1    
    elif button_b.was_pressed():
        display.show(obtenerConsonante())
        sleep(1000)
        total_palabras = total_palabras - 1
    else:
        display.show("?")
    

while True:
    #Hay que pulsar el logo para comenzar a contar
    if pin_logo.is_touched():
        cronometro(30)
        break
    else:
        music.play(music.POWER_UP)
        display.show(Image.STICKFIGURE)
        
music.play(music.POWER_DOWN)
display.scroll("Fin")
