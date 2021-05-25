import PIL, tkinter,cv2 # adding pillow and tkinter for image draw and canvas
import tkinter as Tk # short name for tkinter
from PIL import Image, ImageDraw, ImageFont # image , imagedraw and imagefont from pillow
import os, re # search library
path = input("enter path of TB directory: ")  #user input for path of TB directory  
root = tkinter.Tk()  #canvas size decider
w = root.winfo_screenwidth()  # depending on screen size set width and height
h = root.winfo_screenheight()
root.geometry(f'{w}x{h}')  # set new canvas size
print("Width & HEIGHT", w, h)  # w and h for user refernce
# create line image of width and height
img = Image.new("RGB",[w,h],"white")
tb = ImageDraw.Draw(img)
lookup = {"keyword":"name"}  #lookup table created for uvm component and name
f = open("tree_data.txt","w")  #create file for writing component and component name
f.truncate(0)  # clean file before writing data
color_fill = "white"

def top():  # drawing top level structure
    top_left = (0,0) # co-ordinate decider
    bottom_right = (w,h)  # co-ordinate decider
    #color_fill = "orange"  #color for block
    label = "top"  #name of default block
    block(top_left,bottom_right,label,color_fill)  #call the rectangle creater function
    font = ImageFont.truetype("arial.ttf", 15)  # basic settings for text
    tb.text((w / 2, 10), label, fill="black", font=font)
    # Interface
     intfs = int(input("enter the number of interfaces"))
    #intfs = 1
    for i in range(intfs):
        top_left = 100 + (i * (w - 200) / intfs), h - 220  # co-ordinate decider
        bottom_right = 100 + ((i + 1) * (w - 200) / intfs) - 10, h - 160  # co-ordinate decider '''(i+1)*(w-100)/intfs'''
        # color_fill = "green"  #color for block
        label = ""
        block(top_left, bottom_right, label, color_fill)  # call the rectangle creater function
        font = ImageFont.truetype("arial.ttf", 20)
        #tb.text((w / 2 - 20, h - 250), "Interface", fill="black", font=font)  # avoid taking default text coordinates'''
        tb.text((100 + (i * (w - 200) / intfs)+20, h - 200), "Interface "+str(i+1), fill="black", font=font)  # avoid taking default text coordinates'''
    # DUT
    top_left = 50, h - 120  # co-ordinate decider
    bottom_right = w - 50, h - 20  # co-ordinate decider
    # color_fill = "blue"  #color for block
    label = ""
    block(top_left, bottom_right, label, color_fill)  # call the rectangle creater function
    font = ImageFont.truetype("arial.ttf", 30)
    tb.text((w / 2, h - 100), "DUT", fill="black", font=font)  # avoid taking default text coordinates'''
def test(name):  #drawing test level structure
    top_left = (50,40)  # co-ordinate decider
    bottom_right = (w-50,h-300)  # co-ordinate decider
    #color_fill = "lightgreen"  #color for block
    label = name #"test"
    block(top_left,bottom_right,label,color_fill)  #call the rectangle creater function
    font = ImageFont.truetype("arial.ttf", 15)  # basic settings for text
    tb.text((w / 2, 10+40), label, fill="black", font=font)
def env(name):
    top_left = (100,70)  # co-ordinate decider
    bottom_right = w-100,h -350  # co-ordinate decider
    #color_fill = "yellow"  #color for block
    label = name #"env"
    block(top_left,bottom_right,label, color_fill)  #call the rectangle creater function
    font = ImageFont.truetype("arial.ttf", 15)  # basic settings for text
    tb.text((w / 2, 10+70), label, fill="black", font=font)

def scoreboard(name):
    top_left = 125,105  # co-ordinate decider
    bottom_right = w - 120,(h - 150)/4.4  # co-ordinate decider
    #color_fill = "cyan"  #color for block
    label = name #"scoreboard"
    block(top_left,bottom_right,label, color_fill)  #call the rectangle creater function
    font = ImageFont.truetype("arial.ttf", 15)  # basic settings for text
    tb.text((w / 2, 10+105), label, fill="black", font=font)

def agent(a,i,name):
    if (10>a>5):
        x = 110+((i)*(w-200)/a)
        x1 = x+((w-200)/5)-200
        y = 180  # co-ordinate decider wrt to number of agents
        y1 = h - 360  # co-ordinate decider wrt to number of agents
    elif(a>9):
        x = 160 + ((i) * (w - 200) / a)  # co-ordinate decider wrt to number of agents
        x1 = x + ((w - 200) / a) - 100  # co-ordinate decider wrt to number of agents
        #y = 180  # co-ordinate decider wrt to number of agents
        if((i+1)%2== 1):
            y =380
            y1 = h - 360  # co-ordinate decider wrt to number of agents
        else:
            y1 = h - 560  # co-ordinate decider wrt to number of agents
            y= 180

    else :
        x =200+((i)*(w-200)/a)  # co-ordinate decider wrt to number of agents
        x1 = x + ((w - 200) / a) - 200  # co-ordinate decider wrt to number of agents
        y = 180  # co-ordinate decider wrt to number of agents
        y1 = h - 360  # co-ordinate decider wrt to number of agents

    top_left = (int(x),int(y))  # co-ordinate decider
    bottom_right = (int(x1),int(y1))  # co-ordinate decider
    #color_fill = "coral"  #color for block
    label = ""
    block(top_left, bottom_right, label, color_fill)  #call the rectangle creater function
    font = ImageFont.truetype("arial.ttf", 15)  #text settings
    if (5<a<=9): #if number of agents are greater than 5 draw sub-components small
        label = name #"AGT"+str(i+1)
        tb.rectangle([x + (x1 - x) / 2, y + 30, (x1 - 40 / a), int(y1 - 180)], "white", "black", 5)  # default values for all instance
        tb.rectangle([x + 40 / a, y + 170, -10 + x + (x1 - x) / 2, int(y1 - 40)], "white", "black", 5)  # default values for all instance
        tb.rectangle([x + (x1-x)/2, y + 170,x1-40/a, y1 - 40], "white", "black", 5)
        tb.text(((x + (x1 - x) / 2) + 40, y + 40), "SQR", fill="black", font=font)  # for sequencer
        tb.text((x -40+ 40 / a, y + 180), "DRV", fill="black", font=font)  # for driver
        tb.text(((x + (x1 - x) / 2) + 40, y + 180), "MON", fill="black", font=font)  # for monitor
        # connections

        tb.line((((x + 10 + 40 / a), (y1 - 40)), ((x + 10 + 40 / a), h - 218)), "black", 5)  # driver to VIF
        tb.polygon(((x + 10 + 40 / a - 10, h - 238), (x + 10 + 40 / a + 10, h - 238), (x + 10 + 40 / a, h - 218)),fill="white", outline="black")  # port connection
        tb.line((((x + 10 + (x1 - x) / 2), (y1 - 40)), ((x + (x1 - x) / 2 + 10), h - 218)), "black",5)  # VIF to monitor
        tb.polygon(((x + (x1 - x) / 2, y1-20), (x + 20 + (x1 - x) / 2, y1-20), (x + 10 + (x1 - x) / 2, y1-40)),fill="white", outline="black")  # port connection
        tb.line((((x1 - 40 / a), (y1 - 100)), ((x1 + 50), y1 - 100)), "black", 5)  # monitor to scoreboard
        tb.polygon((x1 - 40 / a + 20, y1 - 100, x1 - 40 / a + 10, y1 - 90, x1 - 40 / a, y1 - 100, x1 - 40 / a + 10, y1 - 110),fill="white", outline="black")  # analysis connection
        tb.line((((x1 + 50), (y1 - 100)), ((x1 + 50), 160)), "black", 5)  # monitor to scoreboard
        tb.ellipse((x1 + 40, 160, x1 + 60, 180), fill="white", outline="black")  # export connection
        tb.line((((x + 10 + 40 / a), (y + 100)), (x + 10 + 40 / a, y + 170)), "black", 5)  # sequencer to driver
        tb.rectangle((x + 10 + 40 / a - 10, y + 170, x + 10 + 40 / a + 10, y + 150), fill="white", outline="black")  # port connection
        tb.line((((x + 10 + +40 / a), (y + 100)), (((x + (x1 - x) / 2)), y + 100)), "black", 5)  # sequencer to driver
        tb.ellipse((x + (x1 - x) / 2 - 20, y + 90, x + (x1 - x) / 2, y + 110), fill="white",outline="black")  # export connection
        # agent label
        tb.text((x+10, y + 10), label, fill="black", font = font)

    elif (a>9): #if number of agents are greater than 10 draw sub-components small
        label = name #"AGT"+str(i+1)
        mark = x +10
        #port connection
        tb.line((((x + (x1 - x) / 2), y1 ), ((x + (x1 - x) / 2 ), h - 218)), "black", 5)  # Agent to interface
        tb.polygon(((x -10+ (x1 - x) / 2, h - 238), (x + 10 + (x1 - x) / 2, h - 238), (x + (x1 - x) / 2, h - 218)),fill="white", outline="black")  # port connection
        tb.polygon(((x -10+ (x1 - x) / 2, y1+20), (x + 10 + (x1 - x) / 2, y1+20), (x + (x1 - x) / 2, y1)),fill="white", outline="black")
        tb.line((x1-1, y, x1-1, 160), "black", 5)  # monitor to scoreboard
        tb.ellipse((x1 -10, 160, x1 + 10, 180), fill="white", outline="black")  # export connection
        # agent label
        font = ImageFont.truetype("arial.ttf", 12)  # text settings
        tb.text((mark-10, y -15), "A "+str(i+1), fill="black", font=font)
        img1 = Image.new("RGB", [w, h], "white")
        tb1 = ImageDraw.Draw(img1)
        font = ImageFont.truetype("arial.ttf", 12)  # text settings
        tb1.text((w/2,50), "AGENT " + str(i + 1), fill="black", font=font)
        #sequencer
        top_left=100,100
        bottom_right=700,200
        tb1.rectangle([top_left, bottom_right], color_fill, "black", 5)  # default values for all instance
        tb1.text((110,110), "sequencer "+str(i+1), fill="black", font=font)  # for sequencer
        #driver
        top_left=100,300
        bottom_right=700,400
        tb1.rectangle([top_left, bottom_right], color_fill, "black", 5)  # default values for all instance
        tb1.text((110,310), "driver "+str(i+1), fill="black", font=font)  # for driver
        #monitor
        top_left=800,300
        bottom_right=1400,400
        tb1.rectangle([top_left, bottom_right], color_fill, "black", 5)  # default values for all instance
        tb1.text((910,310), "monitor "+str(i+1), fill="black", font=font)  # for monitor
        img1.show()
        # edit this line and add path where you have created a agents folder,do not change \agent_"+str(i+1)+".jpg")
        path_filename = (r"C:\Users\ashik\Desktop\mirafra training\pythonProject2\agents\agent_"+str(i+1)+".jpg")
        print(path_filename)
        img1.save(path_filename)

    elif(a<=5):
        label = name #"agent"+str(i+1)
        mark = x + 10
        block( top_left=(x + (x1-x)/2,y + 30), bottom_right=(int(x1 -40/a), int(y1 - 180)), label=" ", color_fill="white")#"grey")  #for sequencer
        block( top_left=(x + 40/a,y + 170), bottom_right=(-10+x + (x1-x)/2 , y1 - 40), label="", color_fill="white")#"violet")  #for driver
        block( top_left=(x + (x1-x)/2,y + 170), bottom_right=(int(x1 -40/a), int(y1 - 40)), label="", color_fill= "white") #"skyblue")  #for monitor
        tb.text(((x+(x1-x)/2)+35,y+40), "sequencer", fill="black", font=font)  #for sequencer
        tb.text((x-50 + 40/a,y + 180), "driver", fill="black", font=font)  #for driver
        tb.text(((x+(x1-x)/2)+35,y+180), "monitor", fill="black", font=font)  #for monitor
        #connections

        tb.line((((x + 10 + 40 / a), (y1 - 40)), ((x + 10 + 40 / a), h - 218)), "black", 5)  # driver to VIF
        tb.polygon(((x+10+40/a-10,h-238),(x+10+40/a+10,h-238),(x+10+40/a,h-218)), fill="white", outline="black")  #port connection
        tb.line((((x + 10 + (x1 - x) / 2), (y1 - 40)), ((x + (x1 - x) / 2 + 10), h - 218)), "black",5)  # VIF to monitor
        tb.polygon(((x + (x1-x)/2, y1-20), (x +20+ (x1-x)/2, y1-20), (x + 10+(x1-x)/2, y1-40)),fill="white", outline="black")  #port connection
        tb.line((((x1 - 40/a), (y1 - 100)), ((x1 + 50), y1 - 100)), "black", 5)  # monitor to scoreboard
        tb.polygon((x1-40/a+20, y1 - 100,x1-40/a+10,y1-90,x1-40/a, y1-100,x1-40/a+10,y1-110), fill="white", outline="black")  #analysis connection
        tb.line((((x1 + 50), (y1 - 100)), ((x1 + 50), 160)), "black", 5)  # monitor to scoreboard
        tb.ellipse((x1 +40, 160, x1 +60, 180), fill="white", outline="black")  #export connection
        tb.line((((x+10+40/a),(y + 100)),( x+10+40/a, y + 170)), "black", 5)  # sequencer to driver
        tb.rectangle((x+10+40/a-10, y +170, x+10+40/a+10, y+150), fill="white", outline="black")  #port connection
        tb.line((((x+10++40/a), (y + 100)), (((x+(x1-x)/2)), y + 100)), "black", 5)  # sequencer to driver
        tb.ellipse((x+(x1-x)/2-20,y+90,x+(x1-x)/2, y+110), fill="white", outline="black")  #export connection
    #agent label
        tb.text((mark,y+10),label, fill="black", font=font)


def block(top_left,bottom_right,label,color_fill): # draw rectangle block, fill color and label
    tb.rectangle([top_left,bottom_right],color_fill,"black",5)  #default values for all instance

    #tb.text((w/2,10+(35*n)),label,fill="black", font=font)

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
    #all_keys = lookup.keys()
    #print (all_keys)

def component_name_finder(keyword,line):
    f = open("tree_data.txt", "a+")  # add found name to file : open write and close
    text = line.split()  #split line where text found
    name = text[1]  # get name from split line
    if keyword+"_1" in lookup:  #if keyword already exists in lookup
        for i in range(10):    # take next count of lookup
            key = keyword+"_"+str(i+2)
            #print (key)
            lookup[key]=name
            f.write(keyword+"_"+str(i+2)+"\t\t\t\t"+name+"\n")
            break
    else:# keyword not in lookup:  #if keyword does not exist in lookup
        if (keyword=="uvm_agent"):  # make it first instance of agent
            key = keyword +"_1"
            lookup[key] = name
            f.write(keyword + "_1"+ "\t\t\t\t" + name + "\n")
        else:
            lookup[keyword] = name  # add name to lookup table
            f.write(keyword + "\t\t\t\t" + name + "\n")
    f = open("tree_data.txt","a+")  #add found name to file : open write and close
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
        a =file.count("uvm_agent_")  # find number of agents
        '''a= int(input ("number of Agents:"))  # uncomment this to add number of agents manually 
        #a = 15 #uncomment and add values for agents explicitly
        print("number of agents : " + str(a))  # print number of agents
        for i in range(a):
            agent(a,i,"uvm_agent_"+str(i+1))  # draw agent with agent names''' # comment this to add number of agents manually
        print("number of agents : " + str(a))  # print number of agents
        for i in range(a):
            agent(a,i,lookup["uvm_agent_"+str(i+1)])  # draw agent with agent names
            #agent(a,i,"uvm_agent_"+str(i+1))  # draw agent with agent names'''
    f.close()
tb_comps()  #to search for component name
read_file_draw()  #read file

def connection_finder(keyword = ".connect("):  # to search for keyword in all files of directory
    root_dir = path
    for root, dirs, files in os.walk(root_dir, onerror=None, topdown=True):  # to loop inside all files of directory
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "rb") as f:  # read file as binary
                for line in f:
                    line = line.decode("utf-8")  # decode to string for read
                    if keyword in line:  # keyword determines the word to be looked into in each of the file
                        #print (keyword,line)
                        text = line
                        if (re.search("_port",text)):
                            if(re.search("export",text)):
                               print ("drawing port and export")
                               print(line)
                               f = open("tree_data.txt", "a+")  # add found name to file : open write and close
                               f.write(str(line)+"\n")
                               f.write("drawing port and export")
                               f.close()
                            else:
                                print("drawing port")
                                print(line)
                                f = open("tree_data.txt", "a+")  # add found name to file : open write and close
                                f.write(line + "\n")
                                f.write("drawing port"+"\n")
                                f.close()
connection_finder()
#block(top_left,bottom_right,color_fill)

#img.show()  #show image before save
img.save(r"C:\Users\ashik\Desktop\mirafra training\pythonProject2\tb_arc.jpg")  # saving image 
image = cv2.imread(r"C:\Users\ashik\Desktop\mirafra training\pythonProject2\tb_arc.jpg")  #reading saved image to draw arrows using CV2 library
image = cv2.arrowedLine(image, (int(w/4), h - 160), (int(w / 4), h - 120), (000), 2)  #arrows from Interface to DUT
image = cv2.arrowedLine(image, (int(w/2), h - 160), (int(w / 2), h - 120), (000), 2)  #arrows from interface to DUT
image = cv2.arrowedLine(image,(int(w*3/4),h-160),(int(w*3/4),h-120),(000),2)   # arrows from interface to DUT
cv2.imshow('abc',image)  # name for python window showing final image
cv2.waitKey(0)  #waiting for click before closing image abc window
cv2.destroyAllWindows()  #close all image windows on click
cv2.imwrite(r"C:\Users\ashik\Desktop\mirafra training\pythonProject2\tb_arc.jpg",image)  #save final image
