# parser.py
from ast_nodes import Program, InstrNode, LabelNode, RegNode, ImmNode, LabelRefNode
from lexer import Lexer

class Parser:
    def __init__(self, input_text):
        self.lexer = Lexer()
        self.tokens = self.lexer.tokenize(input_text)
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def peek(self, offset):
        p = self.pos + offset
        if p < len(self.tokens):
            return self.tokens[p]
        return None

    def advance(self):
        self.pos += 1

    def expect(self, tok_type):
        tok = self.current_token()
        if tok is None or tok[0] != tok_type:
            raise Exception(f"Expect {tok_type}, but got {tok}")
        self.advance()
        return tok

    def parse_program(self):
        instrs = []
        while self.current_token() is not None:
            tok = self.current_token()
            if tok[0] == "NEWLINE":
                self.advance()
                continue
            if tok[0] == "LABEL_DEF":
                name = tok[1][:-1]  
                instrs.append(LabelNode(name))
                self.advance()
                # 可能标签后面直接接指令在同一行，继续循环
                continue

            # must be instruction
            instr = self.parse_instruction()
            instrs.append(instr)
        return Program(instrs)

    def parse_instruction(self):
        tok = self.current_token()
        if tok is None:
            raise Exception("Unexpected EOF while parsing instruction")
        if tok[0] != "INSTR":
            raise Exception(f"Expected INSTR, got {tok}")
        op = tok[1].upper()
        self.advance()

        operands = []
        # parse operands if present until newline or none
        # Some ops have zero operands (HALT), some have 1..3
        if self.current_token() and self.current_token()[0] == "NEWLINE":
            self.advance()
            return InstrNode(op, operands)

        # else parse first operand if exists
        if self.current_token() and self.current_token()[0] not in ("NEWLINE",):
            operands.append(self.parse_operand())

        # further operands by comma
        while self.current_token() and self.current_token()[0] == "SEP":
            self.advance()
            operands.append(self.parse_operand())

        # consume optional newline
        if self.current_token() and self.current_token()[0] == "NEWLINE":
            self.advance()

        return InstrNode(op, operands)

    def parse_operand(self):
        tok = self.current_token()
        if tok is None:
            raise Exception("Unexpected EOF in operand")
        ttype, val = tok
        if ttype == "REG":
            # REG like R10 or r3
            self.advance()
            num = int(val[1:])  # strip 'R'
            return RegNode(val.upper(), num)
        elif ttype == "IMM":
            self.advance()
            num = int(val[1:])  # skip '#'
            return ImmNode(num)
        elif ttype == "ID":
            # label reference
            self.advance()
            return LabelRefNode(val)
        else:
            raise Exception(f"Unexpected token in operand: {tok}")
