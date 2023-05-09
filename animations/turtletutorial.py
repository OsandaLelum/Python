#Instructions	Meaning
#turtle.forward(number)	Move forward
#turtle.back(number)	Move backward
#urtle.right(angle)	Turn clockwise
#turtle.left(angle)	Turn anti-clockwise
#turtle.pencolor(colour string)	Drawing colour
#turtle.pensize(number)	Choosing size of pen nib
#turtle.circle(radius)	Drawing a circle
#turtle.speed(number)	Choosing speed - 1 to 10
#turtle.write(message,font)	Writing on the screen
#turtle.ht()	Hiding the turtle
#turtle.setpos(x,y)	Changing the position of turtle

import turtle    # importing the module
trtl = turtle.Turtle()    #making a turtle object of Turtle class for drawing
screen=turtle.Screen()    #making a canvas for drawing
screen.setup(700,700)    #choosing the screen size
screen.bgcolor('black')    #making canvas black
trtl.pencolor('red')    #making colour of the pen red
trtl.pensize(5)    #choosing the size of pen nib
trtl.speed(1)    #choosing the speed of drawing
trtl.shape('turtle')   #choosing the shape of pen nib
trtl.forward(150)    #drawing a line of 200 pixels
trtl.right(90)    #asking turtle to turn 90 degrees
trtl.forward(150)#drawing a line of 200 pixels
trtl.right(90)
trtl.forward(150)   
trtl.right(90)
trtl.forward(150) 
trtl.penup()    # preparing for moving pen without drawing
trtl.setpos(-140,-120)    # making the new position of the turtle
trtl.pendown()   # bringing the pen down for drawing again
trtl.pencolor('green')    # choosin the pen colour as green
trtl.write('OsAndroid', font=("Arial", 40, "bold"))    # chosing the font
trtl.penup()
trtl.ht()    # hiding the turtle from the screen