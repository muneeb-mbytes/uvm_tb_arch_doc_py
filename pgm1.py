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
def draw_rect(x,y,l,w,color):
 ptr.fillcolor(color)
 ptr.penup()
 ptr.goto(x,y)
 ptr.pendown()
 ptr.begin_fill()
 for i in range(2):
  ptr.forward(l)
  ptr.left(90)
  ptr.forward(w)
  ptr.left(90)
 ptr.end_fill()
draw_square(-200,50,100,"red")
draw_rect(200,50,100,200,"green")
