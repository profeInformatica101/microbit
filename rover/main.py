# Imports go at the top
from microbit import *
from MicroRover import *

rover = Micro_Rover()
display.show(Image.HAPPY)

# Code in a 'while True:' loop repeats forever
while True:
    rover.moverCelda(2)
    rover.girarDerecha()
    rover.moverCelda(1)
    rover.girarIzquierda()
