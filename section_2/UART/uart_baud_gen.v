module baud_gen(
  input wire  clk,
  output reg tick
);

  parameter CLK_FRE = 50000000;
  parameter BAUD_RATE = 115200;
  localparam integer COUNT_MAX = CLK_FRE / BAUD_RATE;
  reg [12:0] count = 0;

  always @(posedge clk) begin
    if (count >= COUNT_MAX - 1) begin
      count <= 0;
      tick <= 1;
    end else begin
      count <= count + 1;
      tick <= 0;
    end
  end

endmodule 
