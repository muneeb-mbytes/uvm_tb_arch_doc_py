#Refer basic.docx for detailed explanation
import turtle
s=turtle.Screen()
s.bgcolor("light blue")
ptr = turtle.Turtle()
ptr.pencolor("black")
def draw_square(x,y,l,color):
 ptr.fillcolor(color)
 ptr.penup()
 ptr.goto(x,y)
 ptr.pendown()
 ptr.begin_fill()
 for i in range(4):
  ptr.forward(l)
  ptr.left(90)
 ptr.end_fill()
def draw_arrow():
 ptr.left(45)
 ptr.backward(10)
 ptr.forward(10)
 ptr.right(90)
 ptr.backward(10)
 ptr.forward(10)
 ptr.left(45)
def write_text(x,y,text):
 ptr.penup()
 ptr.goto(x,y)
 ptr.pendown()
 ptr.write(text,align="center")
  
draw_square(-200,0,100,"red")
draw_square(100,0,100,"red")
ptr.penup()
ptr.goto(-100,50)
ptr.pendown()
ptr.forward(200)
draw_arrow()
write_text(0,50,"connect")
