import math
import turtle

def drawSpiral(t, r, a):
    if r == 0:
        return
    
    x = r*math.cos(a)
    y = r*math.sin(a)
    t.goto(x, y)

    drawSpiral(t, r-0.1, a+0.05)


def main():
    r = 50
    a = 0
    x = r*math.cos(a)
    y = r*math.sin(a)

    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(x, y)
    t.pendown()

    drawSpiral(t, r, a)

    window.exitonclick()

if __name__=='__main__':
    main()

