from lexer import Lexer 

INPUT = "ADD R0, R1, R2"

lexer = Lexer()

print(lexer.tokenize(INPUT))

# [('INSTR', 'ADD'), ('REG', 'R0'), ('SEP', ','), ('REG', 'R1'), ('SEP', ',
# '), ('REG', 'R2')]


# SyntaxError: Unexpected operand ,
