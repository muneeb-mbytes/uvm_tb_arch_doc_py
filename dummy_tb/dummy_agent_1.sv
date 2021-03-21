class mem_agent_1 extends uvm_agent;
  //declaring agent components
  mem_driver_1    driver;
  mem_sequencer_1 sequencer;
  mem_monitor_1   monitor;
 
  // UVM automation macros for general components
  `uvm_component_utils(mem_agent_1)
 
  // constructor
  function new (string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new
 
  // build_phase
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);

  //Creating driver and sequencer when the agent is active.
    if(get_is_active() == UVM_ACTIVE) begin
      driver = mem_driver_1::type_id::create("driver", this);
      sequencer = mem_sequencer_1::type_id::create("sequencer", this);
    end
  
  //Creating monitor.
    monitor = mem_monitor_1::type_id::create("monitor", this);
  endfunction : build_phase
 
  // connect_phase:TLM port connection between sequencer and driver.
  function void connect_phase(uvm_phase phase);
    if(get_is_active() == UVM_ACTIVE) begin
      driver.seq_item_port.connect(sequencer.seq_item_export);
    end
  endfunction : connect_phase
 
endclass : mem_agent_1
