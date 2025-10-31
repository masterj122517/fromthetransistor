from lexer import Lexer
from ast import Program, InstrNode, RegNode, ImmNode

class Parser:
    def __init__(self, input):
        lexer = Lexer()
        self.tokens = lexer.tokenize(input)
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def advance(self):
        self.pos += 1

    def parse_program(self):
        instructions = []
        while self.peek():
            instr = self.parse_instruction()
            if instr:  
                instructions.append(instr)
        return Program(instructions)

    def parse_instruction(self):
        while self.peek() and self.peek()[0] == "NEWLINE":
            self.advance()

        tok = self.peek()
        if tok is None:
            return None
        token_type, value = tok
        if token_type != "INSTR":
            raise SyntaxError(f"Expected instruction, got {token_type}")

        opcode = value
        self.advance()
        operands = self.parse_operands()

        # 消耗当前行末尾的 NEWLINE
        if self.peek() and self.peek()[0] == "NEWLINE":
            self.advance()

        return InstrNode(opcode, operands)

    def parse_operands(self):
        operands = []
        while self.peek() and self.peek()[0] not in ("NEWLINE",):
            operands.append(self.parse_operand())
            if self.peek() and self.peek()[0] == "SEP":
                self.advance()
        return operands

    def parse_operand(self):
        tok = self.peek()
        if tok is None:
            return None

        token_type, value = tok
        if token_type == "REG":
            self.advance()
            return RegNode(value)
        elif token_type == "IMM":
            self.advance()
            return ImmNode(int(value[1:]))
        else:
            raise SyntaxError(f"Unexpected operand {value}")
