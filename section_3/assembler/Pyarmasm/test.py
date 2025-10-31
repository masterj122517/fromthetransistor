from lexer import Lexer 

INPUT = '''start:
  MOV R0, #5
  ADD R1, R0, #2
  B start
'''

lexer = Lexer()

print(lexer.tokenize(INPUT))

# [('INSTR', 'ADD'), ('REG', 'R0'), ('SEP', ','), ('REG', 'R1'), ('SEP', ',
# '), ('REG', 'R2')]


# SyntaxError: Unexpected operand ,
