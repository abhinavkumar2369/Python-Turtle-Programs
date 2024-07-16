## Programs 🌟

1. Draw a Square

```py
import turtle

t = turtle.Turtle()

for i in range(4):
    t.color("red")
    t.forward(100)
    t.right(90)

turtle.done()
```
![ square ](https://github.com/user-attachments/assets/390c93d2-01ca-4e26-9bd4-23066c36a883)



2. Draw a Circle
```py
import turtle

t = turtle.Turtle()
t.color("blue")
t.circle(50)

turtle.done()
```
![ circle ](https://github.com/user-attachments/assets/412f20b2-e2d3-4955-b9ef-1dc5e85c0dda)





3. Draw a Star
```py
import turtle

star = turtle.Turtle()

star.color("red")
star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

turtle.done()
```
![ star ](https://github.com/user-attachments/assets/0eba4c4b-9b90-4323-8620-f9f2be47be46)



4. Draw a spiral
```py
import turtle

t = turtle.Turtle()
t.speed(10)

for i in range(60):
    t.color("red")
    t.forward(i*10)
    t.right(144)

turtle.done()
```
![ spiral ](https://github.com/user-attachments/assets/36b23aa0-6186-4675-bf4e-b10cfe1d2b7e)
