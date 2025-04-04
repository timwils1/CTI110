#Timothy Wilson
# April 6, 2025
# P4LAB1B_WilsonTimothy
# Drawing T and W initials turtle graphics


import turtle


wn = turtle.Screen()
wn.bgcolor("white")
t = turtle.Turtle()
t.pensize(5)
t.color("navyblue")


t.penup()
t.goto(-100, 0)
t.setheading(0)
t.pendown()
t.forward(60)         
t.backward(30)
t.right(90)
t.forward(100)        


t.penup()
t.goto(50, 0)
t.setheading(0)
t.pendown()


t.forward(60)
t.circle(20, 180)
t.forward(20)


t.circle(-20, 180)
t.forward(60)


t.hideturtle()
wn.mainloop()

