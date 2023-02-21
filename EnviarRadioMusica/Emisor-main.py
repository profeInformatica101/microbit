from microbit import *
#importamos radio
import radio

'''
    Configuración RADIO
'''
radio.on()
radio.config(channel=42)
''''''
notas = ['C4:2','D4:2', 'E4:3', 'F4:2', 'a4:2', 'g4:4']

# Función que pasa una lista a texto
def lista_texto(lista):
    mensaje = ""
    for i in lista:
        mensaje += i + ","
    return mensaje

while True:
    if button_a.was_pressed():
        message = lista_texto(notas)
        radio.send(message)
        display.show("OK")
        sleep(1000)
    elif button_b.was_pressed():
        display.show("B")
        sleep(1000)
    else:
        display.show("?")
        sleep(1000)
