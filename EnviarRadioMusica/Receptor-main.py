from microbit import *
#importamos radio
import radio
import music

'''
    Configuración RADIO
'''
radio.on()
radio.config(channel=42)

#Función que dado texto se pasa a lista
def texto_lista(texto):
    return texto.split(",")

#Siempre en ejecución
while True:
   message = radio.receive()
   sleep(20)
   if message is not None:
       try:
           notas = texto_lista(message)
           music.play(notas)
       except:
            display.scroll(message)

