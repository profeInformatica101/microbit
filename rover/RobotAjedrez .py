import math
from micro_rover import Micro_Rover

class RobotAjedrez(Micro_Rover):
    def __init__(self, cell_size=9.5, wheel_radius=1.5):
        super().__init__()
        self.cell_size = cell_size
        self.wheel_radius = wheel_radius

    def avanzar(self, distancia):
        turns = distancia / wheel_circumference
        # Calculate the time required to move the specified distance
        # You might need to adjust the speed and calibrate the time value
        time_to_move = turns * 0.5  # Adjust this value based on your robot's speed

        self.motor(255, 255)
        sleep(time_to_move)
        self.motor(0, 0)

    def retroceder(self, distancia):
        self.move_backward(distancia)

    def girar_izquierda(self, grados):
        self.turn_left(grados)

    def girar_derecha(self, grados):
        self.turn_right(grados)

    def wheel_circumference(self):
        return 2 * math.pi * self.wheel_radius

    def turns_to_move_one_cell(self):
        return self.cell_size / self.wheel_circumference()
    
    
    def move_forward(self, distance):
     

    def move_backward(self, distance):
        turns = distance / wheel_circumference
        time_to_move = turns * 0.5  # Adjust this value based on your robot's speed

        self.motor(-255, -255)
        sleep(time_to_move)
        self.motor(0, 0)

    def turn_left(self, degrees):
        turns = (degrees / 360) * turns_to_move_one_cell
        time_to_turn = turns * 0.5  # Adjust this value based on your robot's turning speed

        self.motor(-255, 255)
        sleep(time_to_turn)
        self.motor(0, 0)

    def turn_right(self, degrees):
        turns = (degrees / 360) * turns_to_move_one_cell
        time_to_turn = turns * 0.5  # Adjust this value based on your robot's turning speed

        self.motor(255, -255)
        sleep(time_to_turn)
        self.motor(0, 0)
