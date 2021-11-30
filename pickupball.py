from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()
motor_a = Motor('A')
motor_b = Motor('B')
Arm_motor = Motor('C')
motor_pair_wheels = MotorPair('A', 'B')
distance_sensor = DistanceSensor('D')
color_sensor = ColorSensor('E')

# Write your program here.
#motor_a.start()
#motor_b.start()


motor_pair_wheels.move(20, 'cm')

wait_for_seconds(1)

motor_pair_wheels.move(1,'seconds', -50, 4)
motor_pair_wheels.move(1,'seconds', 100, 4)

distance_sensor.wait_for_distance_closer_than(50, 'cm')

motor_pair_wheels.start(0, 20)

distance_sensor.wait_for_distance_closer_than(5, 'cm')

motor_pair_wheels.stop()


Arm_motor.run_to_position(300, direction='counterclockwise', speed=15)

Arm_motor.set_stall_detection(False)

motor_pair_wheels.start(0, -20)

#color_sensor.wait_until_color('black')
while True:
    color = color_sensor.wait_for_new_color()
    if color == 'black':
        motor_pair_wheels.stop()
        break

Arm_motor.run_to_position(-300, direction='counterclockwise', speed=15)

# wait_for_seconds(2)
# er_than(10, 'cm')
# #motor_a.stop()
#motor_b.stop()