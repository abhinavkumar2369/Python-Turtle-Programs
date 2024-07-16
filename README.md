## Programs 🌟

1. Draw a Square

```py
import turtle

t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

2. Draw a Circle
```py
import turtle

t = turtle.Turtle()
t.circle(50)

turtle.done()
```

3. Draw a Star
```py
import turtle

star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

turtle.done()
```

4. Draw a spiral
```py
import turtle

t = turtle.Turtle()
t.speed(10)

for i in range(60):
    t.forward(i*10)
    t.right(144)

turtle.done()
```
