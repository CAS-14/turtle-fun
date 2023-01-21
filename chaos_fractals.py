import turtle
import random
import math
import time

def run(t: turtle.Turtle, length: int, dot_size: int = 5, border_width: int = 2):
    height = int((math.sqrt(3)/2)*length)
    vertices = [[length/2, height], [length, 0], [0, 0]]

    t.pensize(border_width)
    t.pendown()
    for coords in vertices: t.goto(coords[0], coords[1])
    t.penup()

    y = random.randint(0, height)
    layer_length = int((height-y)/(math.sqrt(3)/2))
    x = ((length-layer_length)/2) + random.randint(0, layer_length)

    for i in range(100000):
        t.goto(x, y)
        t.dot(dot_size)

        vertice = random.choice(vertices)

        x = int((vertice[0]+x)/2)
        y = int((vertice[1]+y)/2)

if __name__ == "__main__":
    cas = turtle.Turtle()
    cas.speed(0)

    run(cas, 500, 5, 2)