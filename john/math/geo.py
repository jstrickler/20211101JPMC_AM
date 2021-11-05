from math import pi
#  from pkg.module import function
from requests.api import get

# file == script == module
# folder == package == "library"

ANIMAL = 'wombat'

def circle_area(diameter):
    radius = diameter / 2
    return pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

def square_area(side):
    return rectangle_area(side, side)

