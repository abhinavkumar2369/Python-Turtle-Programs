import turtle

t = turtle.Turtle()
t.speed(10)

for i in range(60):
    t.color('red')
    t.forward(i*10)
    t.right(144)

turtle.done()