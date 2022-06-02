import math
import os
import random
import re
import sys
from turtle import speed


class Car:
    max_speed = float
    speed_unit = str
    def __init__(self,max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit
        
    def __str__(self) -> str:
        return "Car with the maximum speed of {} {}".format(self.max_speed, self.speed_unit)
    

class Boat:
    max_speed = float
    speed_unit = 'knots'
    def __init__(self,max_speed):
        self.max_speed = max_speed

    def __str__(self) -> str:
        return "Boat with the maximum speed of {} {}".format(self.max_speed, self.speed_unit)

if __name__ == '__main__':
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        print("%s\n" % vehicle)