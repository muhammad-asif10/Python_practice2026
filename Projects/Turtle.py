import turtle
bob = turtle.Turtle()
bob.speed(2)

# A function to draw a single star
def draw_star():
    for _ in range(5):
        bob.fd(90)
        bob.lt(100)
        bob.fd(90)
        bob.lt(100)
        bob.fd(90)
        bob.lt(100)
        bob.fd(90)
        bob.lt(100)
        bob.fd(90)
        bob.lt(100)

# 1. Draw the first star on the left
bob.penup()
bob.goto(-150, 0)
bob.pendown()
draw_star()

# 2. Move to the right without drawing
bob.penup()
bob.goto(150, 0)
bob.pendown()
draw_star()

# Keep the window open
turtle.done()