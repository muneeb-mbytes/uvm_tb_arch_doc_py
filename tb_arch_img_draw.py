# Refer tb_arch_img_draw.docx for detailed explanation
from PIL import ImageDraw,Image
f=open("tb_info.txt",'r')
content = f.readline()
agent=content.split()
agent_number=agent[2]
f.close()
print(agent_number)
img=Image.new("RGB",(500,500),"white")
draw=ImageDraw.Draw(img)
def top():
 draw.rectangle((5,5,495,360),fill="blue",outline="black")
 draw.text((8,8),"top",fill="black")
def test():
 draw.rectangle((20,20,480,340),fill="green",outline="black")
 draw.text((22,22),"test",fill="black")
def env():
 draw.rectangle((35,35,465,320),fill="grey",outline="black")
 draw.text((38,38),"env",fill="black")
 scoreboard()
 for i in range(int(agent_number)):
  agent(i)
  sequencer(i)
  driver(i)
  monitor(i)
def scoreboard():
 draw.rectangle((150,40,350,80),fill="yellow",outline="black")
 draw.text((225,50),"Scoreboard",fill="black")
def agent(y):
 x = y * ((380/int(agent_number)) + 10)
 z=380/int(agent_number)
 draw.rectangle((50+x,90,z+50+x,300),fill="pink",outline="black")
 draw.text((55+x,90),"agent",fill="black")
def sequencer(y):
 x = y * ((380/int(agent_number)) + 10)
 z=200/int(agent_number)
 draw.rectangle((60+x,100,z+60+x,140),fill="pink",outline="black")
 draw.text((60+x,115),"sequencer",fill="black")
def driver(y):
 x = y * ((380/int(agent_number)) + 10)
 z=160/int(agent_number)
 draw.rectangle((60+x,180,z+60+x,220),fill="pink",outline="black")
 draw.text((65+x,190),"driver",fill="black")
def monitor(y):
 x = y * ((380/int(agent_number)) + 10)
 z=160/int(agent_number) 
 draw.rectangle((60+x+z+10,180,((z*2)+60+x),220),fill="pink",outline="black")
 draw.text((65+x+z,190),"monitor",fill="black")
top()
test()
env()
img.show()
