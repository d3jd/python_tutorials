from turtle import *

def square(len=90):
    for i in range(4):
        forward(len)
        right(90)

def pentagon(len=90):
    for i in range(5):
        forward(len)
        right(360 / 5)

def polygon(sides=5, len=90):
    for i in range(sides):
        forward(len)
        right(360 / sides)

def star(len=90):
    for i in range(5):
        forward(len)
        right(144)

def nautilus_spiral(step=5, ang=5):
    len = 0
    for i in range(100):
        square(len)
        right(ang)
        len += step

if __name__ == "__main__":
    shape('classic')
    color('red', 'yellow')
    begin_fill()

    polygon(len=75,sides=10)
    star(len=180)
    nautilus_spiral(step=5)
    square()
