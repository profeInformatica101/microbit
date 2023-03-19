from microbit import *
from Micro_Rover import *

rover = Micro_Rover()

umbral_distancia = 15  # Distancia umbral en centímetros para evitar la colisión

while True:
   
    distancia = rover.get_distance()  # Obtener la distancia a un objeto frente al rover
    display.show(distancia)

    if distancia < umbral_distancia:
        # Si la distancia es menor que el umbral, retroceder y girar a la derecha
        rover.motor(-150, -100)
        sleep(1000)  # Retroceder durante 1000 milisegundos (1 segundo)
    else:
        # Si la distancia es mayor o igual que el umbral, moverse hacia adelante
        rover.motor(255, 255)

    sleep(100)  # Esperar 100 milisegundos antes de actualizar la distancia y los motores
