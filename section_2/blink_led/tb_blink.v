`timescale 1ns/1ps // 指定 单位和精度 单位/精度 精度不能超过单位

module tb_blink_led;
    //声明 testbench 中的信号
    reg clk;
    wire led;

    //实例化blink_led模块

    blink_led uut (
        .clk(clk),
        .led(led)
    );
    // initial begin ... end 块在仿真开始时执行一次 clk = 0; 初始化时钟 
    // forever #5 clk = ~clk; 无限循环每隔 5ns 翻转一次
    //一个完整周期 = 5ns 上升 + 5ns 下降 = 10ns
    //频率 = 1 / 10ns = 100MHz

    initial begin
        clk = 0;
        forever #5 clk = ~clk;  // 产生一个周期为10ns的时钟
    end

    initial begin
        $dumpfile("blink.vcd"); // 输出波形文件
        $dumpvars(0, tb_blink_led);
        #200 $finish;
    end
endmodule
