import turtle

t = turtle.Turtle()
t.penup()

#Huruf G
t.goto(-30,50)
t.pendown()
t.pensize(7)
t.pencolor("red")
t.right(180)
t.circle(50,180)
t.left(90)
t.forward(50)
t.goto(-50,0)
t.right(90)


#Angka 9 
t.pensize(7)
t.color("black")
t.penup()
t.goto(47,2)
t.pendown()
t.circle(30,-180)
t.left(90)
t.forward(90)
t.circle(-20,180)


#Angka 2
t.pensize(7)
t.color("black")
t.penup()
t.goto(200,-40)
t.pendown()
t.setheading(-180)
t.forward(100)
t.right(120)
t.forward(100)
t.circle(30,180)

#Angka 4
t.pensize(7)
t.color("black")

t.penup()
t.goto(300,-45)
t.pendown()
t.setheading(90)
t.forward(100)
t.setheading(45)
t.forward(-100)
t.setheading(180)
t.forward(-100)

#Huruf S
t.pensize(7)
t.color("red")
t.penup()
t.setpos(400,-50)
t.pendown()
t.forward(20)
t.backward(20)
t.circle(-25, -185)
t.circle(25,-250)
t.hideturtle








