class mem_model_env extends uvm_env;
   
  //---------------------------------------
  // agent and scoreboard instance
  //---------------------------------------
  
  //Taking 6 instances of mem_agent
  mem_agent      mem_agnt_1;
  mem_agent      mem_agnt_2;
  mem_agent      mem_agnt_3;
  mem_agent      mem_agnt_4;
  mem_agent      mem_agnt_5;
  mem_agent      mem_agnt_6;

  //Taking instance of mem_agent_1
  mem_agent_1    mem_agent_new;

  //Taking scoreboard instance
  mem_scoreboard mem_scb;
   
  //Registering the environment class with the factory
  `uvm_component_utils(mem_model_env)
   
  //---------------------------------------
  // constructor
  //---------------------------------------
  function new(string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new
 
  //---------------------------------------
  // build_phase - crate the components
  //---------------------------------------
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
 
    //Creating agents and scoreboard
    mem_agent_new= mem_agent_1::type_id::create("mem_agent_new", this);


    mem_agnt_1= mem_agent::type_id::create("mem_agnt_1", this);
    mem_agnt_2= mem_agent::type_id::create("mem_agnt_2", this);
    mem_agnt_3= mem_agent::type_id::create("mem_agnt_3", this);
    mem_agnt_4= mem_agent::type_id::create("mem_agnt_4", this);
    mem_agnt_5= mem_agent::type_id::create("mem_agnt_5", this);
    mem_agnt_6= mem_agent::type_id::create("mem_agnt_6", this);
    mem_scb  = mem_scoreboard::type_id::create("mem_scb", this);
  endfunction : build_phase
   
  //---------------------------------------
  // connect_phase - connecting monitor and scoreboard port
  //---------------------------------------
  function void connect_phase(uvm_phase phase);

  //Connecting the analysis port of monitor and scoreboard

  mem_agent_new.monitor.item_collected_port.connect(mem_scb.item_collected_export);

    mem_agnt_1.monitor.item_collected_port.connect(mem_scb.item_collected_export);
mem_agnt_2.monitor.item_collected_port.connect(mem_scb.item_collected_export);
mem_agnt_3.monitor.item_collected_port.connect(mem_scb.item_collected_export);
mem_agnt_4.monitor.item_collected_port.connect(mem_scb.item_collected_export);
mem_agnt_5.monitor.item_collected_port.connect(mem_scb.item_collected_export);
mem_agnt_6.monitor.item_collected_port.connect(mem_scb.item_collected_export);

 
   
  endfunction : connect_phase
 
endclass : mem_model_env
