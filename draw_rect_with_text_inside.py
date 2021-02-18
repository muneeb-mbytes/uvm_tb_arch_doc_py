import docx
from PIL import Image,ImageDraw
doc = docx.Document()
img = Image.new("RGB", (500, 500),"white") 
# create a image draw handle
img1 = ImageDraw.Draw(img)
img1.rectangle((200,125,300,200),fill ="orange", outline = "black",width = 1)
img1.text((210, 150), "CHECK TEXT", fill = "black",align = "center")
img.show()
img.save('C:\\Users\\path \\line.jpg');
doc.add_picture('C:\\path \\line.jpg');
doc.save('C:\\path\\pattern_printing_ex.docx');
