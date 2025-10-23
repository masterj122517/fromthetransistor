
module blink_led (
    input clk,
    output reg led = 0
);
    reg [3:0] counter;

    always @(posedge clk) begin
        counter <= counter + 1;
        if (counter == 9) begin
            counter <= 0;
            led <= ~led;
        end
    end
endmodule
