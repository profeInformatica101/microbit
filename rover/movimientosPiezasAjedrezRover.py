# Imports go at the top
from microbit import *
from rover import *

#inicializar Rover
rover = Micro_Rover()

# Code in a 'while True:' loop repeats forever
while True:
   if button_a.is_pressed():
       display.scroll("Caballo")
       rover.moverCelda(1)
       rover.moverCelda(1)
       rover.moverCelda(1)
       rover.girarIzquierda()
       rover.moverCelda(1)
   elif button_b.is_pressed():
       display.scroll("Torre")
       rover.moverCelda(8)
   else:
       display.show("?")
