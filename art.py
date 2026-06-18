#!/bin/python3

from turtle import *
from random import *

shape("turtle")
color(150, 0, 150)

def randomplace():
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)

shape("turtle")
randomcolor()
randomplace()
stamp()
randomcolor()
randomplace()
stamp()
