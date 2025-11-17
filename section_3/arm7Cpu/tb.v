`timescale 1ns/1ps
module tb;

    reg clk = 0;

    always #5 clk = ~clk;

    simple_cpu cpu(.clk(clk));

    initial begin
        $dumpfile("wave.vcd");
        $dumpvars(0, tb);

        #200000;
        $display("Timeout");
        $finish;
    end

endmodule
