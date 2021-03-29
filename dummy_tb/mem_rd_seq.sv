class mem_rd_seq extends uvm_sequence#(mem_seq_item);
   
  //Registering sequence with uvm factory
  `uvm_object_utils(mem_rd_seq)
    
  //Constructor
  function new(string name = "mem_rd_seq");
    super.new(name);
  endfunction
   
  virtual task body();
    `uvm_do_with(req,{req.rd_en == 1;})
  endtask
   
endclass
