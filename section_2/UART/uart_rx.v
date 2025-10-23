module uart_rx(
  input wire clk,
  input wire tick,
  input wire rx,
  input wire reset,
  output reg [7:0] rx_data,
  output reg rx_done
);

typedef enum reg[1:0]{IDLE, START, DATA, STOP} state_t;

reg [7:0] shift_data = 0;
reg [3:0] bit_index = 0;
state_t state = IDLE;

always @(posedge clk or posedge reset) begin
    if (reset) begin
        state      <= IDLE;
        shift_data <= 0;
        bit_index  <= 0;
        rx_data    <= 0;
        rx_done    <= 0;
    end else begin
        rx_done <= 0; // 每个时钟周期默认不拉高，只有接收完成时拉高
        case (state)
            IDLE: begin
                if (rx == 0) begin          // 检测到起始位
                    state <= START;
                end
            end
            START: begin
                if (tick) begin             // 等待比特中点采样
                    state <= DATA;
                    bit_index <= 0;
                end
            end
            DATA: begin
                if (tick) begin
                    shift_data <= {rx, shift_data[7:1]}; 
                    // 右移并接收当前比特 每一轮过后，最低位都会被移出 相当于一个一个的存数据到shift_data里
                    bit_index <= bit_index + 1;
                    if (bit_index == 7) begin
                        state <= STOP;
                    end
                end
            end
            STOP: begin
                if (tick) begin
                    if (rx == 1) begin       // 停止位正确
                        rx_data <= shift_data;
                        rx_done <= 1;        // 一帧数据接收完成
                    end
                    state <= IDLE;            // 回到空闲状态
                end
            end
        endcase
    end
end

endmodule
