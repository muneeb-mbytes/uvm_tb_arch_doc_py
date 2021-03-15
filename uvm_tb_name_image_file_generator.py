import PIL, tkinter
import tkinter as Tk
from PIL import Image, ImageDraw, ImageFont
import os, re
path = input("enter path of TB directory: ")  #user input for path of TB directory
root = tkinter.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'{w}x{h}')
print("Width & HEIGHT", w, h)
# create line image of width and height
img = Image.new("RGB",[w,h],"white")
tb = ImageDraw.Draw(img)
lookup = {"keyword":"name"}
f = open("tree_data.txt","w")
f.truncate(0)
def top():
    n=0
    top_left = (n * 50, n * 50)
    bottom_right = (w - (n * 50), h - (n * 50))
    color_fill = "yellow"
    label = "top"
    block(n,top_left,bottom_right,label,color_fill)
def test(name):
    n=1
    top_left = (n * 50, n * 50)
    bottom_right = (w - (n * 50), h - (n * 50))
    color_fill = "orange"
    label = name #"test"
    block(n,top_left,bottom_right,label,color_fill)
def env(name):
    n=2
    top_left = (n * 50, n * 50)
    bottom_right = (w - (n * 50), h - (n * 90))
    color_fill = "yellow"
    label = name #"env"
    block(n,top_left,bottom_right,label, color_fill)
    #DUT
    top_left = (n*50, h - (n*90)+10)
    bottom_right = (w - (n * 50), h - (n * 50))
    color_fill = "green"
    label = ""
    block(n,top_left,bottom_right,label, color_fill)
    font = ImageFont.truetype("arial.ttf", 20)
    tb.text((w/2,h - (n * 75) ), "DUT", fill="black", font=font)
def scoreboard(name):
    n= 3
    top_left = (n * 50, n * 50)
    bottom_right = (w - (n * 50), (h - (n * 50))/3)
    color_fill = "red"
    label = name #"scoreboard"
    block(n,top_left,bottom_right,label, color_fill)
def agent(a,i,name):
    n=4
    x =200+((i)*(w-200)/a)
    y = (n * 75)
    x1 =x+((w-200)/a)-200
    y1 = (h - (n * 50))
    top_left = (x, y)
    bottom_right = (x1,y1)
    color_fill = "blue"
    label = ""
    block(n, top_left, bottom_right, label, color_fill)
    font = ImageFont.truetype("arial.ttf", 15)
    if (a>5):
        label = name #"AGT"+str(i+1)
        mark = x - 50
        block(5, top_left=(x , y + 30), bottom_right=(x1 , y1 - 250), label=" ", color_fill="grey")
        block(6, top_left=(x , y + 140), bottom_right=(x1, y1 - 130), label="", color_fill="violet")
        block(7, top_left=(x , y + 260), bottom_right=(x1, y1 - 30), label="", color_fill="indigo")
        tb.text((mark + 10, (4 * 75) + 35), "SQR", fill="black", font=font)
        tb.text((mark + 10, 145 + (4 * 75)), "DRV", fill="black", font=font)
        tb.text((mark + 10, 265 + (4 * 75)), "MON", fill="black", font=font)
    else:
        label = name #"agent"+str(i+1)
        mark = x + 5
        block(5, top_left=(x + 30, y + 30), bottom_right=(x1 - 20, y1 - 250), label=" ", color_fill="grey")
        block(6, top_left=(x + 30, y + 140), bottom_right=(x1 - 20, y1 - 130), label="", color_fill="violet")
        block(7, top_left=(x + 30, y + 260), bottom_right=(x1 - 20, y1 - 30), label="", color_fill="indigo")
        tb.text((mark + 35, (4 * 75) + 35), "sequencer", fill="black", font=font)
        tb.text((mark + 35, 145 + (4 * 75)), "driver", fill="black", font=font)
        tb.text((mark + 35, 265 + (4 * 75)), "monitor", fill="black", font=font)
    tb.text((mark,10+(n*75)),label, fill="black", font=font)
def block(n,top_left,bottom_right,label,color_fill): # draw block, fill color and label
    tb.rectangle([top_left,bottom_right],color_fill,"black",5)
    font = ImageFont.truetype("arial.ttf", 15)
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
                        if (keyword == "interface"):
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

    for key, value in lookup.items():
        print(key, ' : ', value)

def component_name_finder(keyword,line):
    text = line.split()
    name = text[1]
    #print(keyword,name)
    lookup [keyword] = name
    f = open("tree_data.txt","a+")
    f.write(keyword+"\t\t\t\t"+name+"\n")
    f.close()
def read_file_draw():
    f = open("tree_data.txt","r")
    file = f.read()
    #print (file)
    if (re.search("uvm_test",file)):
        top()
        test(lookup['uvm_test'])
        env(lookup['uvm_env'])
        scoreboard(lookup['uvm_scoreboard'])
        a =file.count("uvm_agent")
        print ("number of agents : "+str(a))
        # a=3
        for i in range(a):
            agent(a,i,lookup['uvm_agent'])
    f.close()
tb_comps()
read_file_draw()
#block(top_left,bottom_right,color_fill)

img.show()
