import turtle
f=open("tb_info.txt",'r')
content = f.readline()
agent=content.split()
agent_number=agent[2]
f.close()
print(agent_number)
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(30)        #setting the drawing speed
def top():
 t.fillcolor("grey")   #setting the color
 t.penup()             #penup before moving to desired co-ordinates
 t.goto(-650,330)      #moving to these co-ordinates to draw the shape
 t.pendown()           #pendown to start drawing
 for i in range(2):
  t.begin_fill()       #to start filling the color
  t.forward(1300)      #drawing a rectangle
  t.right(90)
  t.forward(480)
  t.right(90)
  t.end_fill()
 t.penup()
 t.goto(-630,310)     #moving to these co-ordinates to label the rectangle
 t.pendown()          #pendown before writing
 t.write("top",align="center",font=10)   #writing text "top" at the center of the turtle pointer
 t.hideturtle()
def test():
 t.fillcolor("light blue")
 t.penup()
 t.goto(-630,300)
 t.pendown()
 for i in range(2):
  t.begin_fill()
  t.forward(1260)
  t.right(90)
  t.forward(420)
  t.right(90)
  t.end_fill()
 t.penup()
 t.goto(-600,280)
 t.pendown()
 t.write("test",align="center",font=10)
 #t.hideturtle()
def env():
 t.fillcolor("light green")    #setting color for env block
 t.penup()
 t.goto(-600,270)              #moving to these co-ordinates before drawing the shape
 t.pendown()
 for i in range(2):
  t.begin_fill()
  t.forward(1200)              #drawing a rectangle
  t.right(90)
  t.forward(360)
  t.right(90)
  t.end_fill()
 t.penup()
 t.goto(-580,250)               #moving to these co-ordinates to label the block
 t.pendown()
 t.write("env",align="center",font=10)  #writing text "top" at the center of the turtle pointer
 scoreboard()
 for i in range(int(agent_number)):      #calling these functions to draw the agent and its sub blocks
  agent(i)
  sequencer(i)
  driver(i)
  monitor(i)
  virtual_interface(i)
def scoreboard():
 t.fillcolor("light yellow")   #setting color for scoreboard block
 t.penup()
 t.goto(-280,240)              #moving to these co-ordinates to draw the shape
 t.pendown()
 for i in range(2):
  t.begin_fill()
  t.forward(570)                #starting to draw a rectangle
  t.right(90)
  t.forward(50)
  t.right(90)
  t.end_fill()
 t.penup()
 t.goto(-10,205)                #moving to these co-ordinates to label the block
 t.pendown()
 t.write("Scoreboard",align="center",font=12)  #writing text "scoreboard" at the center of the turtle pointer
def agent(y):
 t.fillcolor("pink")            #setting color for the agent block
 t.penup()
 print(y,int(agent_number))
 x = y * ((1120/int(agent_number)) + 10)
 t.goto(-560 + x,180)           #moving to these co-ordinates to draw the shape
 t.pendown()
 for i in range(2):             #drawing same size rectangles for i number of agents
  t.begin_fill()
  t.forward(1120/int(agent_number))
  t.right(90)
  t.forward(250)
  t.right(90)
  t.end_fill()
 t.penup()
 t.goto(-500 + x,120)            #moving to these co-ordinates to label the shape
 t.pendown()
 t.write("Agent"+ str(y+1),align="center",font=10)
def sequencer(y):
 t.penup()
 print(y,int(agent_number))
 x = y * ((1120/int(agent_number)) + 10)
 t.goto(-550 + x,100)
 t.pendown()
 for i in range(2):
  t.forward(260/int(agent_number))
  t.right(90)
  t.forward(80)
  t.right(90)
 t.penup()
 t.goto((-545 + 130/int(agent_number))+ x,60)
 t.pendown()
 t.write("Sequencer",align="center",font=10)
 t.penup()
 t.goto(-550 + x + (260/int(agent_number)) ,60)  #moving to these co-ordinates to draw the horizontal arrow line
 t.pendown()                                     #pendown before drawing the arrow line
 z = (300/int(agent_number)) + 10
 t.goto((-540 + z + x),60)                       #drawing the arrow line by moving to these co-ordinates with pendown
 t.left(45)                                      #drawing the arrow head
 t.backward(10)
 t.forward(10)
 t.right(90)
 t.backward(10)
 t.forward(10)
 t.left(45)
def driver(y):
 t.penup()
 print(y,int(agent_number))
 x = y * ((1120/int(agent_number)) + 10)
 z = (300/int(agent_number)) + 10
 t.goto((-540 + z + x),100)                  #moving to these co-ordinates to draw the shape
 t.pendown()
 for i in range(2):                          #drawing same size rectangle inside all agents
  t.forward(300/int(agent_number))
  t.right(90)
  t.forward(80)
  t.right(90)
 t.penup()
 t.goto(-540 + z + x + 150/int(agent_number),60)  #moving to these co-ordinates to label the shape
 t.pendown()
 t.write("Driver",align="center",font=10)    #wrinting text "driver" at the center of the turtle pointer
 t.penup()
 t.goto(-540 + z + x + 150/int(agent_number),20)  #moving to these co-ordinates to draw the arrow
 t.pendown()
 t.right(90)
 t.pendown()
 t.forward(30)                             #drawing the vertical arrow line
 t.left(45)                                #drawing the arrow head
 t.backward(10)
 t.forward(10)
 t.right(90)
 t.backward(10)
 t.forward(10)
 t.left(45)
 t.left(90)
def monitor(y):
 t.penup()
 print(y,int(agent_number))
 x = y * ((1120/int(agent_number)) + 10)
 z= 2 * (300/int(agent_number)) + 20
 t.goto((-540 + z + x),100)              #moving to these co-ordinates to draw the shape
 t.pendown()
 for i in range(2):                      #drawing same sized rectangles inside all agents
  t.forward(300/int(agent_number))
  t.right(90)
  t.forward(80)
  t.right(90)
 t.penup()
 t.goto(-540 + z + x + 150/int(agent_number),60)
 t.pendown()
 t.write("Monitor",align="center",font=10)
 t.penup()
 t.goto(-540 + z + x + 150/int(agent_number),-60)      #moving to these co-ordinates to draw the arrow and arrow head
 t.pendown()
 t.right(90)
 t.pendown()
 t.forward(70)
 t.backward(70)
 t.left(180)
 t.left(45)
 t.backward(10)
 t.forward(10)
 t.right(90)
 t.backward(10)
 t.forward(10)
 t.left(45)
 t.right(90)
def virtual_interface(y):
 t.penup()
 print(y, int(agent_number))
 x = y * ((1120 / int(agent_number)) + 10)
 z = (300 / int(agent_number)) + 10
 t.goto((-540 + z + x),-10)                  #moving to these co-ordinates to draw the shape
 t.pendown()
 for i in range(2):                          #drawing same sized rectangles inside all agents
  t.forward(600 / int(agent_number))
  t.right(90)
  t.forward(50)
  t.right(90)
 t.penup()
 t.goto(-540 + z + x + 280 / int(agent_number), -50)   #moving to these co-ordinates to label the block
 t.pendown()
 t.write("Virtual Interface", align="center", font=10)
 t.penup()
 t.goto(-540 + z + x + 150 / int(agent_number), -60)   #moving to these co-ordinates to draw the arrow
 t.pendown()
 t.right(90)
 t.pendown()
 t.forward(70)
 t.left(45)
 t.backward(10)
 t.forward(10)
 t.right(90)
 t.backward(10)
 t.forward(10)
 t.left(45)
 t.left(90)
 t.penup()
 x = y * ((1120 / int(agent_number)) + 10)
 z = 2 * (300 / int(agent_number)) + 20
 t.goto(-540 + z + x + 150 / int(agent_number), 20)  #moving to these co-ordinates to draw the arrow
 t.pendown()
 t.right(90)
 t.pendown()
 t.forward(30)
 t.backward(30)
 t.left(180)
 t.left(45)
 t.backward(10)
 t.forward(10)
 t.right(90)
 t.backward(10)
 t.forward(10)
 t.left(45)
 t.right(90)

top()
test()
env()
