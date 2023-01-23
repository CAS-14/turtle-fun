import turtle
import random
import math

def generation(t, x, y, start, dot_size, vertices):
        t.goto(x + start[0], y + start[1])
        t.dot(dot_size)

        vertice = random.choice(vertices)

        x = int((vertice[0]+x)/2)
        y = int((vertice[1]+y)/2)

        return x, y

def run(**kwargs):
    length = kwargs["length"] if "length" in kwargs else 300
    border_width = kwargs["border"] if "border" in kwargs else 1
    dot_size = kwargs["dotsize"] if "dotsize" in kwargs else 5
    speed = kwargs["speed"] if "speed" in kwargs else 0
    faster = kwargs["faster"] if "faster" in kwargs else False
    start = kwargs["start"] if "start" in kwargs else [0, 0]

    if faster:
        screen = turtle.Screen()
        screen.tracer(0, 0)

    t = turtle.Turtle()

    height = int((math.sqrt(3)/2)*length)
    vertices = [[length/2, height], [length, 0], [0, 0]]

    t.penup()
    t.goto(start[0], start[1])

    t.pensize(border_width)
    t.pendown()
    for coords in vertices: t.goto(coords[0] + start[0], coords[1] + start[1])
    t.penup()

    y = random.randint(0, height)
    layer_length = int((height-y)/(math.sqrt(3)/2))
    x = ((length-layer_length)/2) + random.randint(0, layer_length)

    if faster:
        t.speed(0)

        while True:
            for i in range(speed):
                x, y = generation(t, x, y, start, dot_size, vertices)
            screen.update()

    else:
        t.speed(speed)
        while True:
            x, y = generation(t, x, y, start, dot_size, vertices)

if __name__ == "__main__":
    run(faster=True, speed=1000, dotsize=1, length=900, start=[-500, -400])