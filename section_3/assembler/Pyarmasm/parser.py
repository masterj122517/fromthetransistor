from ast import Program, InstrNode, RegNode, ImmNode, LabelNode
from lexer import Lexer

class Parser: 
    def __init__(self, input): 
        self.lexer = Lexer()
        self.tokens = self.lexer.tokenize(input) 
        self.pos = 0
    
    def parse_program(self):
        statement
        

        
