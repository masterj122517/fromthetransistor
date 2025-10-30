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
        else:
            return None

    def advance(self): 
        self.pos += 1

    def parse_program(self):
        instructions = [] 
        
        while (self.peek()):
            instr = self.parse_instruction()
            instructions.append(instr)
        return Program(instructions)


    def parse_instruction(self):
        tok = self.peek()
        if tok is None: 
            return None
        token_type, value = tok 

        assert token_type == "INSTR"
        opcode = value
        self.advance()
        operands = self.parse_operands()
        return InstrNode(opcode, operands)


    def parse_operands(self):
        operands = []
        while self.peek() and self.peek()[0] != "NEWLINE":
            operands.append(self.parse_operand())
            if self.peek() and self.peek()[0] == "SEP":
                self.advance()
            if self.peek() and self.peek()[0] == "NEWLINE":
                self.advance()
        return operands 

    def parse_operand(self):
        token_type, value = self.peek()
        if token_type == "REG":
            self.advance()
            return RegNode(value)
        elif token_type == "IMM":
            self.advance()
            return ImmNode(int(value[1:]))  # 去掉 #
        else:
            raise SyntaxError(f"Unexpected operand {value}")


