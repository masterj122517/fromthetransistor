from lexer import Lexer

lexer = Lexer()
source = "ADD R0, R1, R2"

tokens = lexer.tokenize(source)

print(tokens)
