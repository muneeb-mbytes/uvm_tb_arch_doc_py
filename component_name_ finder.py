import os, re, prettytable
path = input("enter path of TB directory: ")  #user input for path of TB directory
open("tree_data.doc","w+")
from prettytable import PrettyTable #to draw table of list
x = PrettyTable()
x.field_names = ["keyword", "class name"]
def component_search(keyword):  # to search for keyword in all files of directory
    root_dir = path
    for root, dirs, files in os.walk(root_dir, onerror=None, topdown=True):  # to loop inside all files of directory
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "rb") as f:  # read file as binary
                for line in f:
                    line = line.decode("utf-8")  #decode to string for read
                    if keyword in line:  # keyword determines the word to be looked into in each of the file
                        #print(file_path,filename)
                        #print(root)
                        #print(root_dir)
                        #print(files)
                        component_name_finder(keyword, line) # call function to  find class name
                        break
def tb_comps():  #generic word in tb components that can be searched to determine presence of comp in TB
    component_search("uvm_test")
    component_search("uvm_env")
    component_search("uvm_scoreboard")
    component_search("uvm_agent")
    component_search("uvm_driver")
    component_search("uvm_monitor")
    component_search("uvm_sequencer")
    component_search("uvm_sequence ")  # added space to accommodate full word matching
    component_search("uvm_sequence_item")
    f = open("tree_data.doc", "a+")  #opens document for append
    f.write("\nname list in table format\n") 
    f.write(str(x))  #draws updated table data
    f.close()
def component_name_finder(keyword,line):
    text = line.split()  #to split line to get class name
    name = text[1]  #class name
    print(keyword+"\t\t\t"+name+"\n")
    f=open("tree_data.doc","a+") #open and save in file tree data
    f.write(keyword+"\t\t"+name+"\n")
    x.add_row([keyword, name]) #adds new row to table
    f.close()
tb_comps()
