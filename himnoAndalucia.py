# Imports go at the top
from microbit import *
import music


texto= "Himno Andalucia";
notas = ['C4:2','D4:2', 'E4:3', 'F4:2', 'a4:2', 'g4:4', 
       'f4#', 'g4:4', 'd4:4', '', '', 'a4:2', 'a4:2', 'a4:4',
       'b4','a4', 'g4:4', 'f4:2', 'g4', 'f4', 'e4:3', '', 'c4:4',
       'g4:4', 'f4:2', 'a4:2', 'g4:2', 'f4:2', 'e4:4',
       'C4:4', 'g4:4', 'F4:2', 'A4:2', 'G4:2', 'F4:2', 'E4:4', 'E4:3', 'D4:2',  'E4:4', 'F4:4', 'A4:4', 'b4', 'a4', 'g4', 'f4#'
        ,'','','','','','','','','','' ]

display.scroll(texto, delay=40)
music.play(notas, wait=False, loop=True)

while True:
    display.show(Image.HEART)
    sleep(1000)
    display.show(Image.HEART_SMALL)
    sleep(1000)

