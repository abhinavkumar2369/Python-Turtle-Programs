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