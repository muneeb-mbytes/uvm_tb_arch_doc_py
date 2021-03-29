class mem_model_test extends uvm_test;
 
  //Registering test class with uvm factory
  `uvm_component_utils(mem_model_test)
  
  //Handle of env  and seq class
  mem_model_env env;
  mem_wr_seq    seq;
 
  function new(string name = "mem_model_test",uvm_component parent=null);
    super.new(name,parent);
  endfunction : new
 
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
 
    //Creating the snv and seq class
    env = mem_model_env ::type_id::create("env", this);
    seq = mem_wr_seq::type_id::create("seq");
  endfunction : build_phase
 
  task run_phase(uvm_phase phase);
    phase.raise_objection(this);
      //Starting the seq
      seq.start(env.mem_agnt.sequencer);
    phase.drop_objection(this);
  endtask : run_phase
 
endclass : mem_model_test
