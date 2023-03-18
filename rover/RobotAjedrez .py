import math
from micro_rover import Micro_Rover

class RobotAjedrez(Micro_Rover):
    def __init__(self, cell_size=9.5, wheel_radius=1.5):
        super().__init__()
        self.cell_size = cell_size
        self.wheel_radius = wheel_radius

    def avanzar(self, distancia):
        self.move_forward(distancia)

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
