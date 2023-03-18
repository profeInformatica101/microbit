import math

cell_size = 9.5  # cm
wheel_radius = 1.5  # cm
wheel_circumference = 2 * math.pi * wheel_radius
turns_to_move_one_cell = cell_size / wheel_circumference


class Micro_Rover:
    # ...

    def move_forward(self, distance):
        turns = distance / wheel_circumference
        # Calculate the time required to move the specified distance
        # You might need to adjust the speed and calibrate the time value
        time_to_move = turns * 0.5  # Adjust this value based on your robot's speed

        self.motor(255, 255)
        sleep(time_to_move)
        self.motor(0, 0)

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
