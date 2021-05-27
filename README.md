# UVM Testbench Flow diagram with Python 
  
## Introduction 
  uvm_tb_arch_doc_py is a python script to automatically generate the UVM testbench Architecture.
  
  It reads a UVM simulation log file and converts in to a JPEG  diagram.

## What you Achieve
  A UVM Testbench Architecture Template using the PythonScript.
  
  Refer the pdf file attached in the main directory - uvm_tb_arch_doc_py_diagram.pdf
  
## Requirements
  For generating the UVM TB Architecture we have to write an example testbench code (top, test, env, agent etc) in UVM Methodology.
  
  1) UVM Testbench log file in .txt format
  
  2) Pycharm Editor 
  
  3) Libraries required:
 
     -OpenCV ( To help with plotting the image and to also save the generated testbench image)
     -PIL (Includes functions like Image, ImageDraw. ImageFont)
     -Tkinter (Help with setting up the canvas for plotting the image)
     
  4) Packages to be installed:
     
     - pip install pillow 
     - pip install opencv-python
     - pip install python-docx 


# Usage
The PyCharm Editor is suitable to run this project as it provides an environment to install packages within a terminal present in the editor.

First, open the Pycharm terminal.

We are using Pycharm version to run the project 
Open the Pycharm Terminla wondow
File -> New project
create location 
Configure the base interepreter for Python (use the latest intrepreter)
Create a Virtual envronment (this takes around 2-3 minutes)
Install the following packages by running the following command
pip install pillow
pip install opencv-pythom
pip install python-docx
Now the installation is completed 
Create a new folder named log in the respective folder of the project
Copy the respective files in to the pycharm project directory (Eg: i have created a director \priya\Pycharm\UVM_TB_ARCH)

execute the script by run 

Enter the name of log directory
Enter the interfaces
Enter the agents
Enter the interfaces 

We get the TB diagram as per the number of interfaces we want and how many interfaces we want 

