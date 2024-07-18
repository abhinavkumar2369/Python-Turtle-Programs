## Programs 🌟


#### 1. Draw a Square

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





#### 2. Draw a Circle

```py
import turtle

t = turtle.Turtle()
t.color("blue")
t.circle(50)

turtle.done()
```
![ circle ](https://github.com/user-attachments/assets/412f20b2-e2d3-4955-b9ef-1dc5e85c0dda)





#### 3. Draw a Star

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






#### 4. Draw a spiral

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







#### 5. Draw a Hexagon

```py
import turtle

t = turtle.Turtle()

for i in range(6):
    t.forward(100)
    t.right(60)

turtle.done()
```
![image](https://github.com/user-attachments/assets/c7962271-6c76-4cd5-beb4-6deb7df622fe)










#### 6. Draw the Spiral of sqaures.

```py
import turtle

t = turtle.Turtle()

for i in range(36):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

turtle.done()
```

![image](https://github.com/user-attachments/assets/c71a39bc-35df-42c5-be32-1433d1c652ce)






#### 7. Draw a Coloured Spiral

```py
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
my_turtle = turtle.Turtle()

my_turtle.speed(10)

for x in range(360):
    my_turtle.pencolor(colors[x % 6])
    my_turtle.width(x / 100 + 1)
    my_turtle.forward(x)
    my_turtle.left(59)

turtle.done()
```
![image](https://github.com/user-attachments/assets/de92a63c-0316-492e-ad1b-c290c0405115)






#### 8. Draw a Fractal Tree.

```py
import turtle

def draw_tree(branch_len, t):
    angle = 30
    sf = 0.8
    if branch_len < 3:
        return
    else:
        t.forward(branch_len)
        t.left(angle)
        draw_tree(branch_len * sf, t)
        t.right(angle * 2)
        draw_tree(branch_len * sf, t)
        t.left(angle)
        t.backward(branch_len)

screen = turtle.Screen()
t = turtle.Turtle()
t.left(90)
t.up()
t.backward(200)
t.down()
t.color("green")
draw_tree(100, t)

turtle.done()
```
![image](https://github.com/user-attachments/assets/61f55e54-0d96-4c57-8bce-77d0185b1527)
