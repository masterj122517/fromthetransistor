`timescale 1ns / 1ps

module uart_tb;

reg clk = 0;
reg reset = 1;
reg [7:0] data_in = 0;
reg tx_start = 0;

wire tx;
wire [7:0] rx_data;
wire rx_done;

uart_top uut (
    .clk(clk),
    .reset(reset),
    .data_in(data_in),
    .tx_start(tx_start),
    .tx(tx),
    .rx_data(rx_data),
    .rx_done(rx_done)
);

always #10 clk = ~clk;  // 20ns 一个周期

initial begin
    #50 reset = 0;

    // 发送第一个字节
    data_in = 8'hA5;
    tx_start = 1;
    #20 tx_start = 0;

    // 等待接收完成
    wait(rx_done);
    $display("Received data: %h", rx_data);

    // 再发送第二个字节
    #2000;   // 等待一段时间确保前一帧完成
    data_in = 8'h5B;
    tx_start = 1;
    #20 tx_start = 0;

    wait(rx_done);
    $display("Received data: %h", rx_data);

    #5000;
    $finish;
end

endmodule
