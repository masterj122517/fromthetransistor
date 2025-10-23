
`timescale 1ns/1ps

module tb_xor2;
    reg a, b;      // 输入
    wire y;        // 输出

    // 实例化 XOR 模块
    xor2 uut (
        .a(a),
        .b(b),
        .y(y)
    );

    // 波形生成
    initial begin
        $dumpfile("xor2.vcd");      // 波形文件名
        $dumpvars(0, tb_xor2);      // 记录 tb_xor2 下的所有信号
    end

    // 测试序列
    initial begin
        // 监视输出变化
        $monitor("Time=%0t | a=%b b=%b y=%b", $time, a, b, y);

        // 生成输入组合
        a = 0; b = 0; #10;
        a = 0; b = 1; #10;
        a = 1; b = 0; #10;
        a = 1; b = 1; #10;

        $finish; // 仿真结束
    end
endmodule
