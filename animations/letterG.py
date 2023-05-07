import turtle

# create a turtle object
t = turtle.Turtle()
screen = turtle.Screen()

# Set the screen size and background color
screen.setup(700, 700)
screen.bgcolor('white')

# draw the letter "G"
# draw the letter "G"
t.pensize(5)
t.goto(0, 0)
t.down()
t.circle(50, 180)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.up()
t.goto(50, 50)
t.down()
t.circle(25)

# hide the turtle object
t.hideturtle()

# wait for user to close the window
turtle.done()
