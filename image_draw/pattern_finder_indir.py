# A function to search and identify the name of uvm components 
#change the root directory name to use with respect to your files 
import os
def component_search(keyword):
    root_dir = r"\Users\ashik\Desktop\VLSI docx\FIFO"
    for root, dirs, files in os.walk(root_dir, onerror=None):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, "rb") as f:  # read the file line by line
                    for line in f:
                        try:
                            line = line.decode("utf-8")
                        except ValueError:
                            continue
                        if keyword in line:
                            print(filename)
                            print(file_path)  # print the file path
                            break  # no need to iterate over the rest of the file
            except (IOError, OSError):
                pass
def tb_comps(): #function to search the componenet names from log file 
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
tb_comps()
