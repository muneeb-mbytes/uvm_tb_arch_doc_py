import os, turtle, re, tkinter, PIL
from tkinter import *
path = input("enter path of TB directory: ")  #user input for path of TB directory
import tkinter as tk
from PIL import ImageGrab  #pillow library Image grab will help to capture image drawn with turtle
root = tk.Tk()
canvas = tk.Canvas(root, width=1500, height=800) #width of Tkinter canvas
canvas.pack()
t = turtle.RawTurtle(canvas)  #turtle to canvas pointer
def component_search(keyword):  # to search for keyword in all files of directory
    root_dir = path
    for root, dirs, files in os.walk(root_dir, onerror=None):  # to loop inside all files of directory
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "rb") as f:  # read file as binary
                for line in f:
                    line = line.decode("utf-8")  #decode to string for read
                    if keyword in line:  #keyword determines the word to be looked into in each of the file
                        print(filename)
                        print(file_path)  # print the file path
                        if keyword == "package":  # add case statements to call shape w.r.t keyword
                            uvm_tb(file_path)
                            break
                        else: break
def tb_comps():  #generic word in tb components that can be searched to determine presence of comp in TB
    component_search("uvm_test")
    component_search("uvm_env")
    component_search("uvm_scoreboard")
    component_search("uvm_agent")
    component_search("uvm_driver")
    component_search("uvm_monitor")
    component_search("uvm_sequencer")
    component_search("uvm_sequence")
    component_search("uvm_sequence_item")
    component_search("interface")
    component_search("package")
def rectangle(x,y,l,b,title):  ## draw rectangle with inputs co-ordinates , dimentions text
    t.goto(x,y)  #co-ordinates to go to
    t.penup()  #pen movement without write
    t.speed(10)  #pen speed setup
    t.color("black")  #pen color
    t.pensize(5)  #pen thickness
    t.pendown()  #start draw
    for i in range(2): #draw rectangle with dimentions
        t.forward(l)
        t.right(90)
        t.forward(b)
        t.right(90)
    t.penup()
    t.goto(x+20, y-20)  # new value for text
    t.pendown()
    t.write(title, align="left", font=("Arial", "10", "bold"))  #text to be written , font size alignment type
    t.penup()
def top():
    t.penup()
    rectangle(-700,380,1400,700,"top")
def test():
    t.penup()
    rectangle(-670,350,1350,650,"test")
def env():
    t.penup()
    rectangle(-640,320,1300,600,"env")
def scoreboard():
    t.penup()
    rectangle(30,300,620,50,"scoreboard")
def agent(x,agent_number):
    y = (x) * 700*(2/agent_number)
    t.goto(-620 + y, 200)
    t.pendown()
    for i in range(2):
        t.forward(900/(agent_number))
        t.right(90)
        t.forward(450)
        t.right(90)
    t.penup()
    t.goto(-630 + y, 210)
    t.pendown()
    t.write("Agent " + str(x+1), align="left", font=("Arial", "10", "bold"))
    #t.color("white")
    t.penup()
    sequencer(x,agent_number)
    driver(x,agent_number)
    monitor(x,agent_number)
def sequencer(x,agent_number):
    y = (x) * 700 * (2 / agent_number)
    t.goto(-610 + y, 160)
    t.pendown()
    for i in range(2):
        t.forward(800 / (agent_number))
        t.right(90)
        t.forward(80)
        t.right(90)
    t.penup()
    t.goto(-610 + y, 170)
    t.pendown()
    t.write("Sequencer " + str(x + 1), align="left", font=("Arial", "10", "bold"))
    #t.color("white")
    t.penup()
def driver(x,agent_number):
    y = (x) * 700 * (2 / agent_number)
    t.goto(-610 + y, 20)
    t.pendown()
    for i in range(2):
        t.forward(800 / (agent_number))
        t.right(90)
        t.forward(80)
        t.right(90)
    t.penup()
    t.goto(-610 + y, 30)
    t.pendown()
    t.write("Driver " + str(x + 1), align="left", font=("Arial", "10", "bold"))
    #t.color("white")
    t.penup()
def monitor(x,agent_number):
    y = (x) * 700 * (2 / agent_number)
    t.goto(-610 + y, -140)
    t.pendown()
    for i in range(2):
        t.forward(800 / (agent_number))
        t.right(90)
        t.forward(80)
        t.right(90)
    t.penup()
    t.goto(-610 + y, -130)
    t.pendown()
    t.write("Monitor " + str(x + 1), align="left", font=("Arial", "10", "bold"))
    #t.color("white")
    t.penup()
def uvm_tb(file_path):
    #f = open((path)+str(r"\fifo_pkg.sv"),"r")
    #print(file_path)
    f = open(file_path, "r") #opens package
    if f.mode == "r":
        package = f.read()
       # print(package)
        if(re.search("..env.sv",package)):
            #print("top test env")
            top()
            test()
            env()
            scoreboard()
            if(re.search(".agent.sv",package)):
                agent_number =package.count("agent.sv")
                #print(agent_number)
                for i in range(agent_number):
                    agent(i,agent_number)

    f.close()
tb_comps()
def dump_gui():
    print('...dumping gui window to png')
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    x1 = x0 + root.winfo_width()*1.27
    y1 = y0 + root.winfo_height()*1.2
    ImageGrab.grab().crop((x0, y0, x1, y1)).save("gui_image_grabbed.png")
dump_gui()
t.exitonclick()
#########
