#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
#Motor
right_wheel = Motor(Port.D)
left_wheel = Motor(Port.C)
robot = DriveBase(left_wheel, right_wheel, wheel_diameter = 55, axle_track = 157)
klo_motor = Motor(Port.B)
klo_sensor = UltrasonicSensor(Port.S1)

#Input
color = ColorSensor(Port.S2)
touch = TouchSensor(Port.S4)


# Write your program here.
ev3.speaker.beep(50,1000)

def linje(speed,a):                            
    if 65 <= color.reflection() <= 75 or color.reflection() <= 20:
        robot.drive(speed,0)
    elif color.reflection() > 75:
        robot.drive(speed, (a*-0.2)*(color.reflection()-75)**2)
    elif color.reflection() < 65:
        robot.drive(speed, (a*0.2)*(color.reflection()-75)**2)

level = 0 

def sort(speed):
    if 5 < color.reflection() < 10:
        print(level+1)
        robot.drive(speed,0)
        ev3.speaker.beep(500,500)
        return 1
    return 0


def level2():
    robot.turn(45)
    robot.straight(180)
    robot.turn(-45)
    linje(90,1)

def level3():
    robot.turn(-45)
    robot.straight(180)
    robot.turn(45)
    linje(90,1)

def level4():
    robot.turn(35)
    while klo_sensor.distance() >= 65:
        linje(35,1)
    else:
        robot.drive(0,0)
        ev3.speaker.beep(500,500)
        klo_motor.run_until_stalled(-500, then=Stop.BRAKE,duty_limit=40)
        robot.drive(35,0)



def level5():
    robot.drive(0,0)
    klo_motor.run_until_stalled(500, then=Stop.BRAKE,duty_limit=40)
    robot.straight(-50)
    robot.turn(-90)
    linje(75,1)

list_ = [['level2()', 0],['level3()', 0],['level4()', 0],['level5()', 0]]


while True:
    print(klo_sensor.distance())
    if not touch.pressed():
        level += sort(75)

        if list_[level-1][1] == 0 and level != 0:
            eval(list_[level-1][0])
            list_[level-1][1] = 1


        if level != 3:
            linje(90,1)


    else:
        robot.stop()
