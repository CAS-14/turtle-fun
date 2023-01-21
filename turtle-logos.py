import turtle


def google(t: turtle.Turtle, size: int):
    # colors
    white = "#ffffff"
    red = "#ea4335"
    yellow = "#fbbc05"
    green = "#34a853"
    blue = "#4285f4"

    # setup
    t.penup()
    t.forward(0.5 * size)
    t.right(90)

    # blue curve part 1
    t.pencolor(blue)
    t.fillcolor(blue)
    t.pendown()
    t.begin_fill()
    t.circle(-0.5 * size, 45)
    t.right(90)
    t.forward(0.2 * size)
    t.right(90)
    t.circle(0.3 * size, 45)
    t.right(90)
    t.forward(0.2 * size)
    t.end_fill()

    # blue curve part 2
    t.begin_fill()
    t.left(90)
    t.circle(0.5 * size, 20)
    t.left(90)
    t.forward(0.2 * size)
    t.left(90)
    t.circle(-0.3 * size, 20)
    t.end_fill()
    t.penup()

    # setup for erasure
    t.right(180)
    t.forward(0.1 * size)
    t.left(90)
    t.forward(0.1 * size)
    t.right(180)

    # erase excess blue curve
    t.pencolor(white)
    t.fillcolor(white)
    t.pendown()
    t.begin_fill()
    t.forward(0.3 * size)
    t.left(90)
    t.forward(0.1 * size)
    t.left(90)
    t.forward(0.3 * size)
    t.left(90)
    t.forward(0.1 * size)
    t.end_fill()
    t.penup()

    # realign before blue stem
    t.forward(1)
    t.left(90)

    # blue stem
    t.pencolor(blue)
    t.fillcolor(blue)
    t.pendown()
    t.begin_fill()
    t.forward(0.2 * size)
    t.right(90)
    t.forward(0.2 * size)
    t.right(90)
    t.forward(0.4 * size)
    t.right(90)
    t.forward(0.2 * size)
    t.right(90)
    t.forward(0.4 * size)
    t.end_fill()
    t.penup()

    # setup for green
    t.right(90)
    t.forward(0.1 * size)
    t.right(90)
    t.forward(0.1 * size)
    t.left(90)
    t.circle(-0.3 * size, 45)

    # green curve
    t.pencolor(green)
    t.fillcolor(green)
    t.pendown()
    t.begin_fill()
    t.circle(-0.3 * size, 90)
    t.left(90)
    t.forward(0.2 * size)
    t.left(90)
    t.circle(0.5 * size, 90)
    t.left(90)
    t.forward(0.2 * size)
    t.end_fill()
    t.penup()

    # setup for yellow
    t.left(90)
    t.circle(-0.3 * size, 90)

    # yellow curve
    t.pencolor(yellow)
    t.fillcolor(yellow)
    t.pendown()
    t.begin_fill()
    t.circle(-0.3 * size, 90)
    t.left(90)
    t.forward(0.2 * size)
    t.left(90)
    t.circle(0.5 * size, 90)
    t.left(90)
    t.forward(0.2 * size)
    t.end_fill()
    t.penup()

    # setup for red
    t.left(90)
    t.circle(-0.3 * size, 90)

    # red curve
    t.pencolor(red)
    t.fillcolor(red)
    t.pendown()
    t.begin_fill()
    t.circle(-0.3 * size, 90)
    t.left(90)
    t.forward(0.2 * size)
    t.left(90)
    t.circle(0.5 * size, 90)
    t.left(90)
    t.forward(0.2 * size)
    t.end_fill()
    t.penup()

    # send home
    t.left(90)
    t.circle(-0.3 * size, 135)
    t.right(90)
    t.forward(0.3 * size)
    t.right(180)
    t.hideturtle()


def ubuntu(t: turtle.Turtle, size: int):
    # colors
    white = "#ffffff"
    orange = "#e95420"

    # setup
    t.penup()
    t.forward(0.5 * size)
    t.left(90)

    # outer circle
    t.color(orange)
    t.pendown()
    t.begin_fill()
    t.circle(0.5 * size)
    t.end_fill()
    t.penup()

    # setup for inner circle
    t.left(90)
    t.forward(0.2 * size)
    t.right(90)

    # inner circle
    t.color(white)
    t.pendown()
    t.begin_fill()
    t.circle(0.3 * size)
    t.left(90)
    t.forward(0.1 * size)
    t.right(90)
    t.circle(0.2 * size)
    t.end_fill()
    t.penup()

    # setup for cutaways
    t.color(orange)

    # cutaways
    for i in range(3):
        t.pendown()
        t.begin_fill()
        t.left(90)
        t.forward(0.025 * size)
        t.right(90)
        t.forward(0.015 * size)
        t.right(90)
        t.forward(0.15 * size)
        t.right(90)
        t.forward(0.03 * size)
        t.right(90)
        t.forward(0.15 * size)
        t.right(90)
        t.forward(0.015 * size)
        t.end_fill()
        t.right(90)
        t.forward(0.025 * size)
        t.left(90)
        t.penup()
        t.circle(0.2 * size, 120)

    t.right(90)
    t.forward(0.1 * size)
    t.left(90)
    t.circle(0.3 * size, 60)
    t.pencolor(orange)

    t.pendown()
    t.begin_fill()

    t.left(90)
    t.forward(0.033 * size)
    t.right(90)
    t.circle(-0.1 * size)
    t.end_fill()

    t.right(90)
    t.forward(0.025 * size)
    t.left(90)
    t.color(white)
    t.begin_fill()
    t.circle(-0.075 * size)
    t.end_fill()
    t.penup()

    t.right(90)
    t.forward(0.008 * size)
    t.left(90)
    t.circle(0.3 * size, 60)

    t.color("black")


if __name__ == "__main__":
    cas = turtle.Turtle()
    cas.speed(0)

    ubuntu(cas, 350)

    turtle.done()