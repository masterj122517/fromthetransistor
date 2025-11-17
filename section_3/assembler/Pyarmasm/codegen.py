# codegen.py
from ast_nodes import InstrNode, LabelNode, RegNode, ImmNode, LabelRefNode

class CodeGen:
    def __init__(self, program):
        self.program = program
        self.labels = {}   # name -> pc
        self.output = bytearray()

    def instr_size(self, instr: InstrNode):
        op = instr.op
        if op == "MOV":   # MOV Rd, #imm  -> opcode, rd, imm
            return 3
        if op == "ADD":   # ADD Rd, Rn, Rm -> opcode, rd, rn, rm
            return 4
        if op == "SUB":
            return 4
        if op == "OUT":   # OUT Rn -> opcode, rn
            return 2
        if op == "B":     # B label -> opcode, offset
            return 2
        if op == "HALT":
            return 1
        raise Exception("Unknown op in size calc: " + op)

    def pass1(self):
        # compute pc for each instr/label
        pc = 0
        for node in self.program.instructions:
            if isinstance(node, LabelNode):
                node.pc = pc
                self.labels[node.name] = pc
            else:
                node.pc = pc
                node.size = self.instr_size(node)
                pc += node.size

    def pass2(self):
        for node in self.program.instructions:
            if isinstance(node, LabelNode):
                continue
            self.emit_instr(node)

    def emit_instr(self, instr: InstrNode):
        op = instr.op
        if op == "MOV":
            # expect operands: Rd, #imm
            rd = instr.operands[0]
            imm = instr.operands[1]
            if not isinstance(rd, RegNode) or not isinstance(imm, ImmNode):
                raise Exception("MOV operands wrong")
            self.output += bytes([0x01, rd.num & 0xFF, imm.value & 0xFF])

        elif op == "ADD":
            # Rd, Rn, Rm
            rd, rn, rm = instr.operands
            if not (isinstance(rd, RegNode) and isinstance(rn, RegNode) and isinstance(rm, RegNode)):
                raise Exception("ADD expects three regs")
            self.output += bytes([0x02, rd.num & 0xFF, rn.num & 0xFF, rm.num & 0xFF])

        elif op == "SUB":
            rd, rn, rm = instr.operands
            if not (isinstance(rd, RegNode) and isinstance(rn, RegNode) and isinstance(rm, RegNode)):
                raise Exception("SUB expects three regs")
            self.output += bytes([0x03, rd.num & 0xFF, rn.num & 0xFF, rm.num & 0xFF])

        elif op == "OUT":
            rn = instr.operands[0]
            if not isinstance(rn, RegNode):
                raise Exception("OUT expects a reg")
            self.output += bytes([0x04, rn.num & 0xFF])

        elif op == "B":
            # operand is a label reference
            target = instr.operands[0]
            if not isinstance(target, LabelRefNode):
                raise Exception("B expects label")
            if target.name not in self.labels:
                raise Exception(f"Undefined label: {target.name}")
            target_pc = self.labels[target.name]
            # offset relative to next instr byte (PC-relative)
            offset = target_pc - (instr.pc + instr.size)
            # encode as signed 8-bit
            off_byte = offset & 0xFF
            self.output += bytes([0x10, off_byte])

        elif op == "HALT":
            self.output += bytes([0xFF])

        else:
            raise Exception("Unknown op in emit: " + op)

    def assemble(self):
        self.pass1()
        self.pass2()
        return self.output
