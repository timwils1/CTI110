#Timothy Wilson
#April 6, 2025
# P4LAB1A SHAPES
#Turtle graphics drawings

import turtle


wn = turtle.Screen()
wn.bgcolor("lightblue")
t = turtle.Turtle()
t.pensize(3)
t.color("blue")


for _ in range(4):
    t.forward(100)
    t.right(90)


t.penup()
t.goto(150, 0)  

t.pendown()
t.color("green")
i = 0
while i < 3:
    t.forward(100)
    t.left(120)
    i += 1

t.hideturtle()
wn.mainloop()
