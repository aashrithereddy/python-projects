import turtle

hr = turtle
hr.color("dark blue")
hr.speed(100)

for i in range(24):
    hr.forward(50)
    hr.penup()
    hr.setposition(0,0)
    hr.pendown()
    hr.right(15)

hr.setposition(0,-51)
hr.circle(52)
hr.penup()

hr.setposition(-500,150)
hr.pendown()
hr.fillcolor('orange')
hr.begin_fill()
hr.forward(1000)
hr.left(90)
hr.forward(300)
hr.left(90)
hr.forward(1000)
hr.left(90)
hr.forward(300)
hr.end_fill()
hr.penup()

hr.setposition(-500, -150)
hr.pendown()
hr.fillcolor('green')
hr.begin_fill()
hr.right(270)
hr.forward(1000)
hr.right(90)
hr.forward(300)
hr.right(90)
hr.forward(1000)
hr.right(90)
hr.forward(300)
hr.end_fill()


turtle.done()
