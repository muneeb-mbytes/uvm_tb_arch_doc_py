1.	Script to draw basic Testbench Diagram aimed at 2 AGENTS can be scaled to n agents (needed few change in calculations)

##########METHOD TO DRAW RECTANGLE WITH THE GIVEN CO-ORDINATES AND FILL WITH THE GIVEN COLOR##############
def draw_rect(image,coordinates,fill,color,width=1):
    rect_start = (coordinates[0][0],coordinates[0][1]);
    rect_end = (coordinates[1][0], coordinates [1][1])
    image.rectangle((rect_start,rect_end),fill=fill,outline = color)
#Method to write the text inside the rectangle
def wr_text_in_rect(image,start_wr_w,start_wr_h,str,tfill):
    font = ImageFont.truetype("arial.ttf", 15)
    image.text((start_wr_w,start_wr_h),str, fill = tfill,font = font)
#Method to draw the top,test,env blocks (w.r.t. the value of n chosen)
def call_simple_rect(w,h,n,text,bfill,tfill,img1):
    w1 = w - (n*10); #end of x should be max
    if n != 5:
        h2 = h - (n*10); #end of 'y' should be max
        h1 = n*15 + 10;
        w2 = h1;
    elif n == 5: #The height of the env block should be less; So used like below dimensions
        h2 = h - (n*10*5)
        h1 = n*15 + 10 + 35;
        w2 = n*15 + 10;
    top_right = (w1,h1)
    bottom_left = (w2,h2)
    start_x = w1 - (50);
    start_y = h1 + (n*2);
    outline_width = 10
    outline_color = "black"
    draw_rect(img1,(top_right, bottom_left), fill=bfill ,color=outline_color, width=outline_width)
    wr_text_in_rect(img1,start_x,start_y,text,tfill)
    print ("Dimensions are %0d %0d %0d %0d",top_right, bottom_left)
    return w1;
#This “docx” module is to manipulate with docs like MS Word. Used it to add TB diagram to the document
import docx
#This “opencv” module in python ease us to draw arrowed line in the image
import cv2
# This “pillow” module to import Image draw module
from PIL import Image,ImageDraw,ImageFont
#Taking the handle “doc” for docx
doc = docx.Document()
#This Module is used to measure the whole screen size
import tkinter
root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print ("Width & HEIGHT",width,height)
# create line image of width and height
w = width
h = height
img = Image.new("RGB", (w, h),"white")
img1 = ImageDraw.Draw(img)
#Create first outer rectangle top n=1
n = 1;
top_dim = call_simple_rect(w,h,n,"TOP","orange","black",img1);
#Create second inner rectangle test n=3
n = 3;
test_dim = call_simple_rect(w,h,n,"TEST","pink","black",img1);
#Create third inner rectangle env n=5
n = 5;
env_dim = call_simple_rect(w,h,n,"ENV","yellow","black",img1);
#Create fifth inner rectangle SCOREBOARD
top_right = (w-140,150)
bottom_left = (400,230)
start_x = ((w-140)+400)/2 + 12;
start_y = 180;
draw_rect(img1,(top_right, bottom_left), fill="gray" ,color="black", width=10)
wr_text_in_rect(img1,start_x,start_y,"SCOREBOARD","BLACK")
#Create fourth inner rectangle sequences DUT
top_right = (90,h-80)
bottom_left = (w-40,h-50)
start_x_dut = (90 + (w-40))/2;
start_y_dut = (((h - 80) + (h - 50))/2) - 12;
draw_rect(img1,(top_right, bottom_left), fill="grey" ,color="black", width=10)
wr_text_in_rect(img1,start_x_dut,start_y_dut,"DUT","BLACK")
#Create fourth inner rectangle Interface
top_right = (90,h-120)
bottom_left = (w-40,h-150)
start_x_if = (90 + (w-40))/2;
start_y_if = ((h-120)+(h-150))/2 - 12;
draw_rect(img1,(top_right, bottom_left), fill="green" ,color="black", width=10)
wr_text_in_rect(img1,start_x_if,start_y_if,"INTERFACE","BLACK")
#Create fourth inner rectangle VIF
top_right = (90,h-190)
bottom_left = (w-40,h-220)
start_x_vif = (90 + (w-40))/2;
start_y_vif = ((h-190)+(h-220))/2 - 12;
draw_rect(img1,(top_right, bottom_left), fill="gray" ,color="black", width=10)
wr_text_in_rect(img1,start_x_vif,start_y_vif,"VIF","BLACK")
print(env_dim);
#Check for number of agents
n = 7;
agnt_cnt = int(input("Enter no. of agents"))
w1 = (env_dim/agnt_cnt)
h1 = (env_dim/agnt_cnt)
tx = 40;
x0 = 0;
diff = 0;
m1 = 1;
m2 = 0;
#To draw the number of agents w.r.t. agent count
for val in range(agnt_cnt):
    print("VALUE OF X0 IS",x0)
    x1 = tx + 55;
    print("VALUE OF X1 IS",x1)
    y0 = (n*4*10)
    if agnt_cnt == 1:
        x0 = (env_dim/agnt_cnt) - 20;
    elif agnt_cnt != 1:
        x0 = (m1*(env_dim/agnt_cnt))+(m2*(x1 + diff));
    print("VALUE OF X0 LATER IS",x0)
    y1 = h - (4*n*10)
    tx = x0;
    diff = x0 - x1;
    top_right = (x0,y0);
    bottom_left = (x1,y1);
    start_x = x0 - 50;
    start_y = y0 + 5;
    outline_width = 10
    print(top_right);
    print(bottom_left);
    draw_rect(img1,(top_right, bottom_left), fill="cyan" ,color="black", width=outline_width)
    wr_text_in_rect(img1,start_x,start_y,"AGENT","BLACK")
    #Start another rectangle MONITOR inside the agent
    x3 = x1 + 10
    y3 = y0 + 20
    x2 = x0 - 350
    y2 = y0 + 100
    top_right = (x2,y2);
    bottom_left = (x3,y3);
    start_x_mon = (x2 + x3)/2;
    start_y_mon = y3 + 15;
    outline_width = 10
    draw_rect(img1,(top_right, bottom_left), fill="orange" ,color="black", width=outline_width)
    wr_text_in_rect(img1,start_x_mon,start_y_mon,"MONITOR","BLACK")
    #Start another rectangle DRIVER inside the agent
    x5 = x3 + 300
    y5 = y3 + 100
    x4 = x2 + 300
    y4 = y2 + 100
    top_right = (x4,y4);
    bottom_left = (x5,y5);
    start_x_drv = (x4 + x5)/2;
    start_y_drv = y5 + 5;
    outline_width = 10
    draw_rect(img1,(top_right, bottom_left), fill="green" ,color="black", width=outline_width)
    wr_text_in_rect(img1,start_x_drv,start_y_drv,"DRIVER","BLACK")
    m2 = 1;
    m1 = 0;
    print("DRIVER",start_x_drv,start_y_drv)
    #Start another rectangle SEQUENCER inside the agent
    x5 = x3 + 300
    y5 = y3
    x4 = x2 + 300
    y4 = y2
    top_right = (x4,y4);
    bottom_left = (x5,y5);
    start_x_sqr = (x4 + x5)/2;
    start_y_sqr = y5 + 5;
    outline_width = 10
    draw_rect(img1,(top_right, bottom_left), fill="grey" ,color="black", width=outline_width)
    wr_text_in_rect(img1,start_x_sqr,start_y_sqr,"SEQUENCER","BLACK")
    m2 = 1;
    m1 = 0;
    img.show()
    img.save('C:\\Users\\goushik\\Desktop\\New folder\\tb_arch.jpg');
    # Arrow Drawing 
    path = 'C:\\Users\\goushik\\Desktop\\New folder\\tb_arch.jpg'
    # Reading an image in default mode  
    image = cv2.imread(path)  
    # Window name in which image is displayed  
    window_name = 'Image'
    ######################DRAW ARROW BETWEEN DRIVER AND VIF#################################
    start_point = (int(start_x_drv - 15),int(start_y_drv) + 75)  
    # End coordinate 
    end_point = (int(start_x_drv - 15),int(start_y_drv + 25) + 115) 
    color = (0, 0, 0)  
    thickness = 3
    # Using cv2.arrowedLine() method  
    image = cv2.arrowedLine(image, start_point, end_point,color, thickness)
    cv2.imshow(window_name, image)
    cv2.imwrite("C:\\Users\\goushik\\Desktop\\New folder\\tb_arch.jpg",image)
######################DRAW ARROW BETWEEN VIF AND INTERFACE###################################
# Start coordinate
start_point = (int(start_x_vif - 15),int(start_y_vif + 25))  
# End coordinate 
end_point = (int(start_x_if - 15),int(start_y_if - 5))
color = (0, 0, 0)  
thickness = 3
# Using cv2.arrowedLine() method 
image = cv2.arrowedLine(image, start_point, end_point,color, thickness)
cv2.imshow(window_name, image)
######################DRAW ARROW BETWEEN INTERFACE AND DUT#################################
start_point = (int(start_x_if - 15),int(start_y_if + 25))  
# End coordinate 
end_point = (int(start_x_dut - 15),int(start_y_dut - 5)) 
color = (0, 0, 0)  
thickness = 3
# Using cv2.arrowedLine() method  
image = cv2.arrowedLine(image, start_point, end_point,color, thickness)
cv2.imshow(window_name, image)
######################DRAW ARROW BETWEEN DRIVER1 AND VIF#################################
start_point = (506,482)  
# End coordinate 
end_point = (506,547) 
color = (0, 0, 0)  
thickness = 3
# Using cv2.arrowedLine() method  
image = cv2.arrowedLine(image, start_point, end_point,color, thickness)
cv2.imshow(window_name, image)
cv2.imwrite("C:\\Users\\goushik\\Desktop\\New folder\\tb_arch.jpg",image)
doc.add_picture('C:\\Users\\goushik\\Desktop\\New folder\\tb_arch.jpg')
doc.save('C:\\Users\\goushik\\Desktop\\New folder\\pattern_printing_ex.docx')
