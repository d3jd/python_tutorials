from turtle import *

# draw square
def square(len=90):
    for i in range(4):
        forward(len)
        right(90)

# draw pentagon
def pentagon(len=90):
    for i in range(5):
        forward(len)
        right(360 / 5)

# draw N-side polygon
def polygon(sides=5, len=90):
    for i in range(sides):
        forward(len)
        right(360 / sides)

# draw star
def star(len=90):
    for i in range(5):
        forward(len)
        right(144)

        # write text
        write('Star!')

draw nautilus spiral made of squares
def nautilus_spiral(step=5, ang=5):
    len = 0
    for i in range(100):
        square(len)
        right(ang)
        len += step

if __name__ == "__main__":
    # change shape of the cursor
    shape('classic')

    # change color of the cursor
    color('red', 'yellow')
    begin_fill()

    # test functions
    polygon(len=75,sides=10)
    star(len=180)
    nautilus_spiral(step=5)
    square()
