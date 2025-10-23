module uart_tx(
  input wire clk,
  input wire tick,
  input wire tx_start,
  input wire [7:0] data_in,
  output reg tx,
  output reg tx_done
);

typedef enum reg [1:0] {IDLE, START, DATA, STOP} state_t;

state_t state = IDLE;

reg [7:0] shift_reg = 0;
reg [3:0] bit_index = 0;

always @(posedge clk) begin
  tx_done = 0;
  case (state) 
    IDLE: begin
      tx <= 1;
      if (tx_start) begin
        shift_reg <= data_in;
        bit_index <= 0;
        state <= START;
      end
    end
    START: begin 
    if (tick) begin 
      tx <= 0;
      state <= DATA;
      end
    end
    DATA: begin 
      if (tick) begin 
        tx <= shift_reg[0];
        shift_reg <= shift_reg >> 1;
        bit_index <= bit_index + 1;
        if (bit_index == 7) begin 
          state <= STOP;
        end
      end
    end
    STOP: begin 
      if (tick) begin 
        tx <= 1;
        tx_done <= 1;
        state <= IDLE;
      end
    end
  endcase
end
endmodule


