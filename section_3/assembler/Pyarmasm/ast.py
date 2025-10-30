class Program:
    def __init__(self, instructions):
        self.instructions = instructions

class InstrNode:
    def __init__(self, opcode, operands):
        self.opcode = opcode
        self.operands = operands

class RegNode:
    def __init__(self, name):
        self.name = name

class ImmNode:
    def __init__(self, value):
        self.value = value


