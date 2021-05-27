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

1) open the Pycharm editor.

2) click File -> New Project.

3) Create the project in a specific directory.

4) Configure the base interpreter of python if it is already installed on the system. If python is not present in the system, install Pycharm and then there will be an option     provided to set a base interpreter.

5) Create a virtual environment for your project. ( This setup will take 2-3 minutes). 

6) Open the Pycharm terminal and install the packages one after another as mentioned in point 4) of the Requirements section.

7) Create a folder named  log in the project directory.

8) Copy all the files into the Prject directory that has been created. (For example, the path I have created is C:\User\

9) Make sure to copy the log file into the log folder in the project.(For example, suppose the log file has a name testbench.log, then the file should be in the d

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

