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


def level1():
    robot.turn(45)
    robot.straight(180)
    robot.turn(-45)
    linje(90,1)

def level2():
    robot.turn(-45)
    robot.straight(180)
    robot.turn(45)
    linje(90,1)

def level3():
    while klo_sensor.distance() >= 33:
        linje(70,1)
    else:
        robot.drive(0,0)
        ev3.speaker.beep(500,500)
        klo_motor.run_until_stalled(1000, then=Stop.BRAKE,duty_limit=100)
        robot.drive(50,0)



def level4():
    robot.drive(0,0)
    klo_motor.run_until_stalled(-1000, then=Stop.BRAKE,duty_limit=40)
    robot.straight(-50)
    robot.turn(-90)


def level5():
    robot.straight(57)
    robot.turn(-90)

def level6(x):
    robot.turn(10)
    robot.straight(110)
    robot.turn(-20)
    robot.straight(110)
    robot.turn(10)
    while color.reflection() >= 55:
        linje(90,1)
    robot.straight(400)
    robot.turn(x*90)

def level7():
    robot.reset()
    robot.turn(-45)
    robot.straight(100)
    robot.turn(45)
    while robot.distance() < 400:
        linje(90,1)
    robot.reset()
    robot.turn(-45)
    robot.straight(100)
    robot.turn(45)

def level8():
    robot.straight(60)
    robot.turn(-90)
    

def level9():
    robot.straight(300)
    robot.reset()
    while klo_sensor.distance() > 575:
        robot.turn(-1)
    robot.turn(-10)
    while klo_sensor.distance() >= 33 and robot.distance() < 600:
        robot.drive(35,0)
    robot.drive(0,0)
    klo_motor.run_until_stalled(1000, then=Stop.BRAKE,duty_limit=100)
    robot.straight(-robot.distance()-50)
    robot.drive(0,0)
    robot.turn(-robot.angle()-10)
    klo_motor.run_until_stalled(-1000, then=Stop.BRAKE,duty_limit=40)
    robot.straight(-50)
    robot.turn(-90)
    robot.straight(150)
    while color.reflection() > 65:
        robot.drive(90,1)
    robot.turn(-90)
    while color.reflection() > 10:
        linje(50,1)

def level10():
    robot.reset()
    while robot.distance() < 500:
        linje(90,1)
    robot.straight(100)
    robot.turn(-90)


def level11():
    while klo_sensor.distance() > 175:
        linje(35,1)
    robot.turn(45)
    robot.reset()
    while color.reflection() > 60:
        robot.drive(100,-17)
    robot.turn(45) 

def level12():
    robot.reset()
    while robot.distance() < 40:
        linje(35,1)
    robot.turn(45)
    robot.straight(40)
    robot.turn(-45)
    while klo_sensor.distance() > 100:
        robot.drive(70,0)
    d = robot.distance()
    robot.turn(-45)
    while klo_sensor.distance() > 100:
        robot.drive(70,3)
    robot.turn(70)
    robot.straight(250)
    robot.turn(-robot.angle())
    robot.straight(d-100)

def level13():
    robot.reset()
    while robot.distance() < 20:
        linje(10,0.1)
    while color.reflection() > 40:
        robot.drive(150,0)
    robot.straight(-(robot.distance()/2))
    while True:
        robot.drive(0,0)


list_ = [['level1()', 0],['level2()', 0],['level3()', 0],['level4()', 0],['level5()', 0],['level6(1)', 0],['level6(-1)', 0],['level7()', 0],['level8()', 0],['level9()',0],['level10()', 0],['level11()', 0],['level12()', 0],['level11()', 0],['level13()', 0]]

while True:
    if not touch.pressed():
        level += sort(75)

        if list_[level-1][1] == 0 and level != 0:
            eval(list_[level-1][0])
            list_[level-1][1] = 1


        if level != 3:
            linje(90,1)


    else:
        robot.stop()
