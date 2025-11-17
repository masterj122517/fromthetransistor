
// BootROM 模块
module bootrom #(
    parameter ADDR_WIDTH = 8,      // 地址线宽度，256 字节 ROM
    parameter DATA_WIDTH = 8       // 数据宽度
)(
    input  wire                 clk,   // 时钟
    // addr = CPU 发给 BootROM 的“取指令地址”
    input  wire [ADDR_WIDTH-1:0] addr, // CPU 提供的地址(PC的值)
    output reg  [DATA_WIDTH-1:0] data  // ROM 输出数据(指令)
);

    // ROM 内存数组
    reg [DATA_WIDTH-1:0] mem [0:(1<<ADDR_WIDTH)-1];

    integer i;

    // 初始化 ROM 内容
    initial begin
        // 从 hex 文件加载启动程序
        $readmemh("bootrom.hex", mem);

        // 可选：初始化其余地址为 0
        for (i = 0; i < (1<<ADDR_WIDTH); i = i + 1) begin
            if (mem[i] === 8'hxx)  // $readmemh 中未赋值的地方
                mem[i] = 8'h00;
        end
    end

    // ROM 读取逻辑（同步输出）
    always @(posedge clk) begin
        data <= mem[addr];
    end

endmodule
