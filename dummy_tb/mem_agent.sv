class mem_agent extends uvm_agent;
  //declaring agent components
  mem_driver    driver;
  mem_sequencer sequencer;
  mem_monitor   monitor;
 
  // UVM automation macros for general components
  `uvm_component_utils(mem_agent)
 
  // constructor
  function new (string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new
 
  // build_phase
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
 
    if(get_is_active() == UVM_ACTIVE) begin
      driver = mem_driver::type_id::create("driver", this);
      sequencer = mem_sequencer::type_id::create("sequencer", this);
    end
 
    monitor = mem_monitor::type_id::create("monitor", this);
  endfunction : build_phase
 
  // connect_phase
  function void connect_phase(uvm_phase phase);
    if(get_is_active() == UVM_ACTIVE) begin
      driver.seq_item_port.connect(sequencer.seq_item_export);
    end
  endfunction : connect_phase
 
endclass : mem_agent
