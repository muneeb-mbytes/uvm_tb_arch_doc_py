#Choosing the “TURTLE” library
from turtle import *
# Choose Color for rectangle
color("orange")
# Enabling fill to color the shape
begin_fill()
# Traverse in directions, to draw rectangle
#Move forward direction of 300 units (length of rectangle)
forward(300);
#Move right direction of 90 units (For starting the breadth of rectangle)
right(90)
forward(150)
right(90)
forward(300);
right(90)
forward(150)
right(90)
# End the coloring inside that rectangle
end_fill()
#Choose color to write inside rectangle
color("BLACK") # Choose Black color to write
#Enabling the text fill color
begin_fill()
#This penup feature is to enable the pointer
penup()
#Fixing the pointer location from where to start the text inside rectangle
forward (150)
#right (45)
left(65)
backward (20)
#Write the desired text that needs to be written onto the rectangle
write("TEXT INSIDE RECTANGLE USING TURTLE", True, align="center")
