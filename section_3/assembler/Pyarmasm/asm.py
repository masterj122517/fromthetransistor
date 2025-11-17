# assemble.py
import sys
from parser import Parser
from codegen import CodeGen

def to_hex_lines(bytearr):
    return [f"{b:02x}\n" for b in bytearr]

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 assemble.py input.asm output.mem")
        sys.exit(1)
    src = sys.argv[1]
    out = sys.argv[2]

    text = open(src, 'r', encoding='utf8').read()
    p = Parser(text)
    prog = p.parse_program()

    cg = CodeGen(prog)
    machine = cg.assemble()

    with open(out, 'w', encoding='utf8') as f:
        f.writelines(to_hex_lines(machine))

    print(f"Wrote {len(machine)} bytes to {out}")

if __name__ == "__main__":
    main()
