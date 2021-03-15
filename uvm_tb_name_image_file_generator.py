import PIL, tkinter # adding pillow and tkinter for image draw and canvas
import tkinter as Tk # short name for tkinter
from PIL import Image, ImageDraw, ImageFont # image , imagedraw and imagefont from pillow
import os, re # search library
path = input("enter path of TB directory: ")  #user input for path of TB directory
root = tkinter.Tk()  #canvas size decider
w = root.winfo_screenwidth() # depending on screen size set width and height
h = root.winfo_screenheight()
root.geometry(f'{w}x{h}')  # set new canvas size
print("Width & HEIGHT", w, h)  # w and h for user refernce
# create line image of width and height
img = Image.new("RGB",[w,h],"white")
tb = ImageDraw.Draw(img)
lookup = {"keyword":"name"}  #lookup table created for uvm component and name 
f = open("tree_data.txt","w")  #create file for writing component and component name
f.truncate(0)  # clean file before writing data
def top():  # drawing top level structure
    n=0  # value to simplify calculations
    top_left = (n * 50, n * 50) # co-ordinate decider
    bottom_right = (w - (n * 50), h - (n * 50))  # co-ordinate decider
    color_fill = "yellow"  #color for block
    label = "top"  #name of default block
    block(n,top_left,bottom_right,label,color_fill)  #call the rectangle creater function
def test(name):  #drawing test level structure
    n=1  #value to simplify calculations
    top_left = (n * 50, n * 50)  # co-ordinate decider
    bottom_right = (w - (n * 50), h - (n * 50))  # co-ordinate decider
    color_fill = "orange"  #color for block
    label = name #"test"
    block(n,top_left,bottom_right,label,color_fill)  #call the rectangle creater function
def env(name):
    n=2  # value to simplify calculations
    top_left = (n * 50, n * 50)  # co-ordinate decider
    bottom_right = (w - (n * 50), h - (n * 90))  # co-ordinate decider
    color_fill = "yellow"  #color for block
    label = name #"env"
    block(n,top_left,bottom_right,label, color_fill)  #call the rectangle creater function
    #DUT
    top_left = (n*50, h - (n*90)+10)  # co-ordinate decider
    bottom_right = (w - (n * 50), h - (n * 50))  # co-ordinate decider
    color_fill = "green"  #color for block
    label = ""
    block(n,top_left,bottom_right,label, color_fill)  #call the rectangle creater function
    font = ImageFont.truetype("arial.ttf", 20)
    tb.text((w/2,h - (n * 75) ), "DUT", fill="black", font=font)  #avoid taking default text coordinates
def scoreboard(name):
    n= 3  # value to simplify calculations
    top_left = (n * 50, n * 50)  # co-ordinate decider
    bottom_right = (w - (n * 50), (h - (n * 50))/3)  # co-ordinate decider
    color_fill = "red"  #color for block
    label = name #"scoreboard"
    block(n,top_left,bottom_right,label, color_fill)  #call the rectangle creater function
def agent(a,i,name):
    n=4  # value to simplify calculations
    x =200+((i)*(w-200)/a)  # co-ordinate decider wrt to number of agents
    y = (n * 75)  # co-ordinate decider wrt to number of agents
    x1 =x+((w-200)/a)-200  # co-ordinate decider wrt to number of agents
    y1 = (h - (n * 50))  # co-ordinate decider wrt to number of agents
    top_left = (x, y)  # co-ordinate decider
    bottom_right = (x1,y1)  # co-ordinate decider
    color_fill = "blue"  #color for block
    label = ""
    block(n, top_left, bottom_right, label, color_fill)  #call the rectangle creater function
    font = ImageFont.truetype("arial.ttf", 15)  #text settings
    if (a>5): #if number of agents are greater than 5 draw sub-components small
        label = name #"AGT"+str(i+1)
        mark = x - 50
        block(5, top_left=(x , y + 30), bottom_right=(x1 , y1 - 250), label=" ", color_fill="grey")  #for sequencer
        block(6, top_left=(x , y + 140), bottom_right=(x1, y1 - 130), label="", color_fill="violet")  #for driver
        block(7, top_left=(x , y + 260), bottom_right=(x1, y1 - 30), label="", color_fill="indigo")  #for monitor
        tb.text((mark + 10, (4 * 75) + 35), "SQR", fill="black", font=font)  #naming for Sqr
        tb.text((mark + 10, 145 + (4 * 75)), "DRV", fill="black", font=font)  #naming for drv
        tb.text((mark + 10, 265 + (4 * 75)), "MON", fill="black", font=font)  #naming for mon
    else:
        label = name #"agent"+str(i+1)
        mark = x + 5
        block(5, top_left=(x + 30, y + 30), bottom_right=(x1 - 20, y1 - 250), label=" ", color_fill="grey")  #for sequencer
        block(6, top_left=(x + 30, y + 140), bottom_right=(x1 - 20, y1 - 130), label="", color_fill="violet")  #for driver
        block(7, top_left=(x + 30, y + 260), bottom_right=(x1 - 20, y1 - 30), label="", color_fill="indigo")  #for monitor
        tb.text((mark + 35, (4 * 75) + 35), "sequencer", fill="black", font=font)  #for sequencer
        tb.text((mark + 35, 145 + (4 * 75)), "driver", fill="black", font=font)  #for driver
        tb.text((mark + 35, 265 + (4 * 75)), "monitor", fill="black", font=font)  #for monitor
    tb.text((mark,10+(n*75)),label, fill="black", font=font)
def block(n,top_left,bottom_right,label,color_fill): # draw rectangle block, fill color and label
    tb.rectangle([top_left,bottom_right],color_fill,"black",5)  #default values for all instance
    font = ImageFont.truetype("arial.ttf", 15)  #basic settings for text
    tb.text((w/2,10+(50*n)),label,fill="black", font=font) 

def component_search(keyword):  # to search for keyword in all files of directory
    root_dir = path
    for root, dirs, files in os.walk(root_dir, onerror=None):  # to loop inside all files of directory
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "rb") as f:  # read file as binary
                for line in f:
                    line = line.decode("utf-8")  #decode to string for read
                    if keyword in line:  #keyword determines the word to be looked into in each of the file
                        #print(filename)
                        #print(file_path)  # print the file path
                        #print(line)
                        if (keyword == "interface"):  # to avoid psedo interface name error
                            #print("yes interface")
                            text =line.split()
                            if len(text) != 2:
                                #print("not match")
                                break
                            else:
                                component_name_finder(keyword, line)
                        else:
                            component_name_finder(keyword,line)
                        break
def tb_comps():  #generic word in tb components that can be searched to determine presence of comp in TB
    component_search("uvm_test")
    component_search("uvm_env")
    component_search("uvm_scoreboard")
    component_search("uvm_agent")
    component_search("uvm_driver")
    component_search("uvm_monitor")
    component_search("uvm_sequencer")
    component_search("uvm_sequence ")
    component_search("uvm_sequence_item")
    component_search("interface")
    #component_search("package")

    for key, value in lookup.items():  #saving component names into lookup table
        print(key, ' : ', value)

def component_name_finder(keyword,line):
    text = line.split()  #split line where text found
    name = text[1]  # get name from split line
    #print(keyword,name)
    lookup [keyword] = name  #add name to lookup table 
    f = open("tree_data.txt","a+")  #add found name to file : open write and close
    f.write(keyword+"\t\t\t\t"+name+"\n")
    f.close()
def read_file_draw():
    f = open("tree_data.txt","r")  #read file written with names
    file = f.read()
    #print (file)
    if (re.search("uvm_test",file)): # find keyword in file
        top()  # draw top
        test(lookup['uvm_test']) #draw test with found name
        env(lookup['uvm_env'])  # draw env with found name
        scoreboard(lookup['uvm_scoreboard'])  # draw scb with found name
        a =file.count("uvm_agent")  # find number of agents
        print ("number of agents : "+str(a))  #print number of agents
        # a=3 '''uncomment and add values for agents explicitly'''
        for i in range(a):
            agent(a,i,lookup['uvm_agent'])  # draw agent with agent names
    f.close()
tb_comps()
read_file_draw()
#block(top_left,bottom_right,color_fill)

img.show()  #show image before save
