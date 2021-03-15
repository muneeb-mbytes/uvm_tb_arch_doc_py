class mem_driver extends uvm_driver #(mem_seq_item);
 
  // Virtual Interface
  virtual mem_if vif;
 
  `uvm_component_utils(mem_driver)
     
  //uvm_analysis_port #(mem_seq_item) Drvr2Sb_port;
 
  // Constructor
  function new (string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new
 
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
     if(!uvm_config_db#(virtual mem_if)::get(this, "", "vif", vif))
       `uvm_fatal("NO_VIF",{"virtual interface must be set for: ",get_full_name(),".vif"});
  endfunction: build_phase
 
  // run phase
  virtual task run_phase(uvm_phase phase);
    forever begin
    seq_item_port.get_next_item(req);
    //respond_to_transfer(req);
    drive();
    seq_item_port.item_done();
    end
  endtask : run_phase
 
  // drive
  virtual task drive();
    req.print();
      `DRIV_IF.wr_en <= 0;
      `DRIV_IF.rd_en <= 0;
      @(posedge vif.DRIVER.clk);
      `DRIV_IF.addr <= req.addr;
    if(req.wr_en) begin
        `DRIV_IF.wr_en <= req.wr_en;
        `DRIV_IF.wdata <= req.wdata;
      //$display("\tADDR = %0h \tWDATA = %0h",req.addr,trans.wdata);
        @(posedge vif.DRIVER.clk);
      end
    if(req.rd_en) begin
        `DRIV_IF.rd_en <= req.rd_en;
        @(posedge vif.DRIVER.clk);
        `DRIV_IF.rd_en <= 0;
        @(posedge vif.DRIVER.clk);
        req.rdata = `DRIV_IF.rdata;
       // $display("\tADDR = %0h \tRDATA = %0h",trans.addr,`DRIV_IF.rdata);
      end
      $display("-----------------------------------------");
  endtask : drive
 
endclass : mem_driver
