from parser import Parser

INPUT = '''start:
  MOV R0, #5
  ADD R1, R0, #2
  B start
'''

parser = Parser(INPUT)

program = parser.parse_program()

for instr in program.instructions:
    print(instr.opcode, [(type(op).__name__, getattr(op, 'name', getattr(op, 'value', None))) for op in instr.operands])
