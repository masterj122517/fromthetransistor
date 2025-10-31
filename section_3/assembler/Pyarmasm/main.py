from parser import Parser

INPUT = '''
MOV R0, R1, R2
MOV R0, R1, R2
'''

parser = Parser(INPUT)

program = parser.parse_program()

for instr in program.instructions:
    print(instr.opcode, [(type(op).__name__, getattr(op, 'name', getattr(op, 'value', None))) for op in instr.operands])
