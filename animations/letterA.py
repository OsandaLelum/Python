from turtle import *

# Set up the turtle
t = Turtle()
t.speed(0)
t.hideturtle()

# Draw the letter A
t.pu()
t.goto(-100, 0)
t.pd()
t.goto(-50, 200)
t.goto(0, 0)
t.goto(50, 200)
t.goto(100, 0)
t.pu()

# Animate the letter A
for i in range(10):
    t.clear()
    t.pu()
    t.goto(-100 + i * 20, 0)
    t.pd()
    t.goto(-50 + i * 20, 200)
    t.goto(0 + i * 20, 0)
    t.goto(50 + i * 20, 200)
    t.goto(100 + i * 20, 0)
    t.pu()
    update()
    ontimer(t.clear, 100)

done()
