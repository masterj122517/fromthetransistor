module simple_cpu(
    input clk
);

    // ROM: byte-addressable
    reg [7:0] rom [0:1023];     // 1KB ROM

    // 16 registers, 32-bit
    reg [31:0] regfile [0:15];

    reg [31:0] pc;

    // temporary bytes
    reg [7:0] opcode;
    reg [7:0] b1, b2, b3;

    integer i;

    initial begin
        $readmemh("program.mem", rom);

        for (i = 0; i < 1024; i = i + 1) begin
          if (rom[i] === 8'hxx || rom[i] === 8'hXX) begin
            rom[i] = 8'h00;
          end
        end

        pc = 0;

        for (i = 0; i < 16; i = i + 1)
            regfile[i] = 0;

        for (i = 0; i < 100; i = i + 1)
           $display("%0d: %02x", i, rom[i]);
    end


    always @(posedge clk) begin
        opcode = rom[pc];

        case (opcode)

        8'h01: begin
            // MOV Rd, #imm
            b1 = rom[pc + 1];
            b2 = rom[pc + 2];
            regfile[b1[3:0]] <= {24'b0, b2};
            pc <= pc + 3;
        end

        8'h02: begin
            // ADD Rd, Rn, Rm
            b1 = rom[pc + 1];
            b2 = rom[pc + 2];
            b3 = rom[pc + 3];
            regfile[b1[3:0]] <= regfile[b2[3:0]] + regfile[b3[3:0]];
            pc <= pc + 4;
        end

        8'h03: begin
            // SUB Rd, Rn, Rm
            b1 = rom[pc + 1];
            b2 = rom[pc + 2];
            b3 = rom[pc + 3];
            regfile[b1[3:0]] <= regfile[b2[3:0]] - regfile[b3[3:0]];
            pc <= pc + 4;
        end

        8'h04: begin
            // OUT Rn
            b1 = rom[pc + 1];
            $write("%c", regfile[b1[3:0]][7:0]);
            pc <= pc + 2;
        end

        8'h10: begin
            // B offset
            b1 = rom[pc + 1];
            // 做了符号扩展，保证计算的正确
            pc <= pc + 2 + $signed({{24{b1[7]}}, b1});
        end

        8'hff: begin
            $display("\n[CPU halted]");
            $finish;
        end

        default: begin
            $display("Invalid opcode %02x at PC %0d", opcode, pc);
            $finish;
        end

        endcase
      // $display("PC=%d opcode=%02x", pc, opcode);
    end

endmodule
