class mem_sequencer_1 extends uvm_sequencer#(mem_seq_item);
 
  //Registering sequencer class with uvm factory
  `uvm_component_utils(mem_sequencer_1)
 
  //constructor
  function new(string name, uvm_component parent);
    super.new(name,parent);
  endfunction
   
endclass
