import turtle
turtle.color('black', 'red')
turtle.begin_fill()
for i in range(0,4):
 turtle.right(90*i)
 turtle.penup()
 turtle.forward(38)
 turtle.pendown()
 turtle.right(45)
 turtle.forward(200)
 turtle.right(90)
 turtle.forward(253.53)
 turtle.right(90)
 turtle.forward(56.57)
 turtle.right(90)
 turtle.forward(200)
 turtle.left(90)
 turtle.forward(143.43)
 turtle.penup()
 turtle.home()
turtle.end_fill()
turtle.done()
