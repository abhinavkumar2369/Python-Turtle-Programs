import turtle

screen = turtle.Screen()

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
my_turtle = turtle.Turtle()

my_turtle.speed(10)

for x in range(360):
    my_turtle.pencolor(colors[x % 6])
    my_turtle.width(x / 100 + 1)
    my_turtle.forward(x)
    my_turtle.left(59)

turtle.done()