import turtle
import time

# Create a turtle object and a screen object
trtl = turtle.Turtle()
screen = turtle.Screen()

# Set the screen size and background color
screen.setup(700, 700)
screen.bgcolor('black')

# Set the pen color, pen size, turtle shape, and initial number of sides
trtl.pencolor('red')
trtl.pensize(5)
trtl.shape('turtle')
n = 3

# Define a list of shapes for later use
shapes = ['Triangle', 'Square', 'Pentagon', 'Hexagon', 'Heptagon', 'Octagon', 'Nonagon', 'Decagon']

# Loop through the list of shapes
for shape in shapes:
    # Draw the shape
    for i in range(n):
        trtl.pencolor('red')
        trtl.forward(60)
        trtl.right(360/n)
    
    # Pause for one second and clear the screen
    time.sleep(1)
    trtl.clear()
    
    # Increment the number of sides and reset the turtle's position
    n += 1
    trtl.penup()
    trtl.home()
    trtl.pendown()
    
# Hide the turtle when finished
trtl.ht()
