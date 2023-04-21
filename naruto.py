import turtle

turtle.Screen().bgcolor("#eeeeee")
draw = turtle.Turtle()

draw.pensize(8)
draw.hideturtle()
turtle.tracer(5)
draw.pencolor('black')
draw.left(13)
draw.speed(30)
draw.fillcolor("yellow")
draw.begin_fill()
draw.penup()
draw.forward(190)
draw.pendown()

# Hair
draw.right(25)
draw.forward(60)
draw.left(135)
draw.forward(100)
draw.right(95)
draw.forward(95)
draw.left(135)
draw.forward(110)
draw.right(105)
draw.forward(115)
draw.left(135)
draw.forward(145)
draw.right(112)
draw.forward(115)
draw.left(137)
draw.forward(163)
draw.right(110)
draw.forward(115)
draw.left(130)
draw.forward(142)
draw.right(85)
draw.forward(120)
draw.left(130)
draw.forward(128)
draw.right(100)
draw.forward(110)
draw.left(126)
draw.forward(115)
draw.right(73)
draw.forward(82)
draw.left(136)
draw.forward(60)

draw.pensize(3)
draw.left(70)
draw.forward(15)
draw.right(59)

def curve1(a,d):
    for i in range(d):
        draw.right(a)
        draw.forward(1)

def curve2(a,d):
    for i in range(d):
        draw.left(a)
        draw.forward(1)

curve1(0.1,260)
curve1(0.2,80)
draw.left(6)
curve1(0.1,90)
draw.right(60)
draw.forward(11)
draw.end_fill()


draw.begin_fill()
draw.fillcolor('#373737')
draw.pensize(8)
curve1(0.2,72)
draw.pensize(5)
draw.right(80)
curve1(0.01,240)
draw.right(2)
curve1(0.01,100)
draw.right(2)
curve1(0.02,77)
draw.right(75)
draw.pensize(8)
curve1(0.2,65)
draw.pensize(3)
draw.forward(18)
draw.right(63.5)
curve1(0.1,250)
draw.right(5)
curve1(0.1,100)
draw.left(3)
curve1(0.1,83)
draw.right(70)
draw.forward(10)
draw.pensize(5)
draw.forward(73)
draw.end_fill()
draw.fillcolor('#E8BEAC')
draw.begin_fill()
draw.pensize(8)
draw.left(40)
curve1(1,60)
draw.forward(60)
draw.right(60)
curve1(0.3,27)
draw.left(85)
curve1(0.2,85)
draw.right(30)
draw.forward(133)
draw.right(40)
draw.forward(80)
draw.right(37)
draw.forward(150)
draw.right(35)
curve1(0.1,67)
draw.left(80)
draw.forward(32)
draw.right(50)
curve1(0.5,63)
draw.right(10)
curve1(0.1,40)
draw.right(10)
curve1(0.3,20)
draw.right(70)
draw.forward(7)
draw.pensize(5)
curve2(0.01,418)
draw.end_fill()

draw.backward(10)

draw.fillcolor('yellow')
draw.begin_fill()
draw.right(118)
draw.forward(70)
draw.right(150)
draw.forward(64.5)
draw.right(91)
draw.forward(45)
draw.end_fill()


draw.penup()
draw.backward(100)
draw.pendown()
draw.fillcolor('yellow')
draw.begin_fill()
draw.right(155)
draw.forward(90)
draw.right(155)
draw.forward(50)
draw.right(54)
draw.forward(50)
draw.end_fill()

draw.penup()
draw.backward(180)
draw.pendown()

draw.fillcolor('yellow')
draw.begin_fill()
draw.right(41)
draw.forward(65)
draw.right(165)
draw.forward(91)
draw.right(153)
draw.forward(40)
draw.end_fill()

draw.penup()
draw.backward(110)
draw.pendown()

draw.fillcolor('yellow')
draw.begin_fill()
draw.right(90)
draw.forward(62)
draw.right(158)
draw.forward(72)
draw.right(120)
draw.forward(40)
draw.end_fill()

draw.penup()
draw.left(40)
draw.forward(40)
draw.right(34)
draw.pendown()


draw.fillcolor('grey')
draw.begin_fill()
curve2(0.01,247)
draw.left(85)
curve2(0.02,50)
draw.left(3)
curve2(0.1,35)
draw.left(82)
curve2(0.01,140)
draw.left(2)
curve2(0.1,110)
draw.left(77)
curve2(0.1,86)
draw.end_fill()

draw.penup()
draw.left(138)
draw.forward(20)
draw.dot(10)
draw.left(35)
draw.forward(25)
draw.dot(10)
draw.forward(25)
draw.dot(10)

draw.penup()
draw.right(85)
draw.forward(155)
draw.pendown()
draw.right(135)
draw.forward(22)
draw.right(100)
draw.forward(2)
curve2(2.2,110)
curve2(3,45)
curve2(5,30)
draw.penup()
draw.right(130)
draw.forward(25)
draw.left(85)
draw.pendown()
draw.forward(30)
draw.left(112)
draw.forward(35)
draw.penup()
draw.left(25)
draw.forward(120)
draw.pendown()

draw.dot(10)
draw.right(120)
draw.penup()
draw.forward(30)
draw.pendown()
draw.dot(10)
draw.penup()
draw.forward(30)
draw.pendown()
draw.dot(10)
draw.penup()
draw.left(60)
draw.forward(118)
draw.left(120)
draw.pendown()
draw.pensize(4)
draw.forward(20)
curve2(11,15)
draw.forward(35)
curve2(7,8)
draw.right(15)
draw.forward(15)
draw.right(70)
draw.forward(23)
draw.left(40)
draw.forward(15)
curve2(15,10)
draw.forward(20)
draw.penup()
draw.left(20)
draw.forward(43)
draw.pendown()
draw.left(80)
draw.forward(20)

draw.penup()
draw.left(28)
draw.forward(403)
draw.right(95)
draw.pendown()
draw.forward(28)
curve1(10,15)
draw.right(3)
draw.forward(45)
curve1(8,10)
draw.forward(8)
draw.left(3)
curve2(7,12)
draw.left(10)
draw.forward(15)
curve1(12,13)
draw.right(5)
draw.forward(15)
draw.penup()
draw.right(195)
draw.forward(60)
draw.left(90)
draw.pendown()
curve1(1,45)
draw.penup()
draw.right(119)
draw.forward(65)
draw.right(180)
draw.pendown()
curve1(1,50)
draw.penup()
draw.right(110)
draw.forward(55)
draw.right(190)
draw.pendown()
curve1(1,38)
draw.penup()
draw.right(53)
draw.forward(35)
draw.pendown()
draw.left(20)
draw.forward(70)
curve2(0.2,70)
draw.left(30)
draw.forward(20)
draw.penup()
draw.left(130)
draw.forward(109)
draw.right(35)
draw.pendown()
draw.forward(15)
draw.right(90)
curve2(1,30)
draw.penup()
draw.right(76.5)
draw.forward(143)
draw.pendown()
curve1(1,47)
draw.penup()
draw.right(120)
draw.forward(55)
draw.pendown()
draw.right(192)
curve1(1,47)
draw.penup()
draw.right(120)
draw.forward(45)
draw.pendown()
draw.right(220)
curve1(1,41)
draw.penup()
draw.right(170)
draw.forward(153)
draw.right(138)
draw.forward(5)
draw.pendown()
curve2(0.5,65)
draw.penup()
draw.right(5)
draw.backward(35)
draw.left(80)
draw.forward(5)
draw.pendown()
draw.right(75)
draw.forward(10)
draw.fillcolor('white')
draw.begin_fill()
draw.circle(22)
draw.end_fill()
curve2(3,20)
draw.pendown()
draw.fillcolor('white')
draw.begin_fill()
curve2(6,85)
draw.end_fill()
draw.dot(15)
draw.penup()
draw.left(121)
draw.forward(32)
draw.left(80)
draw.pendown()
draw.pensize(10)
draw.forward(30)
draw.left(95)
draw.pensize(8)
draw.forward(20)
draw.pensize(7)
curve2(1,80)

# second eye
draw.right(54)
draw.penup()
draw.forward(115)
draw.pendown()
draw.pensize(4)
draw.backward(4)
curve1(0.5,60)
draw.penup()
draw.backward(27)
draw.right(90)
draw.forward(8)
draw.pendown()
draw.right(90)
draw.fillcolor('white')
draw.begin_fill()
draw.circle(22)
curve2(3,30)
draw.end_fill()
curve2(6,85)
draw.dot(15)
draw.penup()
draw.right(30)
draw.forward(43)
draw.pendown()
draw.right(85)
draw.pensize(10)
draw.forward(27)
draw.pensize(8)
draw.right(85)
draw.forward(20)
draw.pensize(7)
curve1(1,80)
draw.end_fill()

turtle.done()