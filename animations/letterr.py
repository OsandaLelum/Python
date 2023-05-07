import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
#t.color(("#4285F4, #4285F4"))
t.pensize(5)
t.speed(3)

# Draw the left vertical line of the R
t.left(90)
t.forward(100)
t.right(90)

# Draw the top diagonal line of the R
t.circle(-50, 180)
t.right(140)
t.forward(70)

# Draw the bottom diagonal line of the R
t.circle(-20, 200)
t.right(120)
t.forward(65)

# wait for user to close the window
turtle.done()