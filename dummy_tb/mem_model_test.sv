class mem_model_test extends uvm_test;
 
  `uvm_component_utils(mem_model_test)
 
  mem_model_env env;
  mem_sequence  seq;
 
  function new(string name = "mem_model_test",uvm_component parent=null);
    super.new(name,parent);
  endfunction : new
 
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
 
    env = mem_model_env::type_id::create("env", this);
    seq = mem_sequence::type_id::create("seq");
  endfunction : build_phase
 
  task run_phase(uvm_phase phase);
    phase.raise_objection(this);
      seq.start(env.mem_agnt.sequencer);
    phase.drop_objection(this);
  endtask : run_phase
 
endclass : mem_model_test
