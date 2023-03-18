robot = RobotAjedrez()

# Mover el robot una celda hacia adelante
robot.avanzar(robot.cell_size)

# Mover el robot una celda hacia atrás
robot.retroceder(robot.cell_size)

# Girar el robot 90 grados a la izquierda
robot.girar_izquierda(90)

# Girar el robot 90 grados a la derecha
robot.girar_derecha(90)

# Obtener la circunferencia de la rueda
circunferencia_rueda = robot.wheel_circumference()
print("Circunferencia de la rueda:", circunferencia_rueda)

# Obtener las vueltas necesarias para moverse una celda
vueltas_celda = robot.turns_to_move_one_cell()
print("Vueltas para mover una celda:", vueltas_celda)
