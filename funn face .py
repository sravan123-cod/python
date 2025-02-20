import turtle

# Setup the screen

screen = turtle.Screen()

screen.bgcolor("white")

# Create a turtle for drawing

pen = turtle.Turtle()

pen.speed(5)

# Function to draw a circle

def draw_circle(color, x, y, radius):

 pen.penup()

 pen.goto(x, y - radius)

 pen.pendown()

 pen.color(color)

 pen.begin_fill()

 pen.circle(radius)

 pen.end_fill()

# Draw the face

draw_circle("yellow", 0, 0, 100) # Face

# Draw eyes

draw_circle("white", -35, 40, 20) # Left eye

draw_circle("white", 35, 40, 20) # Right eye

draw_circle("black", -35, 50, 10) # Left pupil

draw_circle("black", 35, 50, 10) # Right pupil

# Draw a funny nose

pen.penup()

pen.goto(0, 30)

pen.pendown()

pen.color("red")

pen.width(5)

pen.circle(5)

# Draw a funny smiling mouth

pen.penup()

pen.goto(-40, -20)

pen.pendown()

pen.width(5)

pen.setheading(-60) # Angle for smile

pen.circle(40, 120) # Draw smile arc

# Add tongue

pen.penup()

pen.goto(0, -20)

pen.setheading(-90)

pen.pendown()

pen.color("red")

pen.begin_fill()

pen.circle(10, 180)

pen.end_fill()

# Hide turtle

pen.hideturtle()

# Keep the window open

screen.mainloop()