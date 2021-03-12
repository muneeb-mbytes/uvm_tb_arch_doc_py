class mem_wr_seq extends uvm_sequence#(mem_seq_item);
   
  `uvm_object_utils(mem_wr_seq)
    
  //Constructor
  function new(string name = "mem_wr_seq");
    super.new(name);
  endfunction
   
  virtual task body();
    `uvm_do_with(req,{req.wr_en == 1;})
  endtask
   
endclass
