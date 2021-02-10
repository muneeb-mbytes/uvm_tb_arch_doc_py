from turtle import *
# Choose Color for rectangle
color("orange")
begin_fill() # Enabling fill to color the shape
# Traverse in directions, to draw rectangle
forward(300);
right(90)
forward(150)
right(90)
forward(300);
right(90)
forward(150)
right(90)
# End the coloring
end_fill()
color("BLACK") # Choose Black color to write
begin_fill()
penup()
forward (150)
#right (45)
left(65)
backward (20)
write("TEXT INSIDE RECTANGLE USING TURTLE", True, align="center")
#write("TEXT", True, align="center")
