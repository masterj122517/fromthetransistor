// 创建所有module 的 instant
module uart_top(
    input wire clk,
    input wire reset,
    input wire [7:0] data_in,
    input wire tx_start,
    output wire tx,
    output wire rx_done,
    output wire [7:0] rx_data
);

wire tick;

// 波特率发生器
baud_gen #(
    .CLK_FRE(50000000),
    .BAUD_RATE(115200)
) baudgen_inst (
    .clk(clk),
    .tick(tick)
);

// UART 发送
uart_tx uart_tx_inst (
    .clk(clk),
    .tick(tick),
    .tx_start(tx_start),
    .data_in(data_in),
    .tx(tx),
    .tx_done()
);

// UART 接收，回环测试：rx 直接接 tx
uart_rx uart_rx_inst (
    .clk(clk),
    .tick(tick),
    .rx(tx),       // loopback 测试
    .reset(reset),
    .rx_data(rx_data),
    .rx_done(rx_done)
);

endmodule
