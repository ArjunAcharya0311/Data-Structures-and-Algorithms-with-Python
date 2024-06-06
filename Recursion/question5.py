''' Recursive function that draws a tree'''

import turtle

def drawBranch(t, angle, branch_count):
    if branch_count == 0:  # Base case
        t.fillcolor("green")
        t.color("green")
        t.begin_fill()
        for i in range(4):
            t.forward(5) # Forward turtle by s units
            t.left(90) # Turn turtle by 90 degree
        t.end_fill()
        t.color("brown")
        return 
    
    branch_length = branch_count*10

    t.pensize(branch_count+2)
    t.color("brown")
    t.forward(branch_length)
    t.left(angle)
    drawBranch(t, angle-1, branch_count-1)
    t.right(angle*2)
    drawBranch(t, angle-1, branch_count-1)
    t.left(angle)
    t.back(branch_length)
    



def main():
    window = turtle.Screen()
    angle = 30
    branch_count = 8
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    drawBranch(t, angle, branch_count)
    window.exitonclick()
    

if __name__=='__main__':
    main()
    