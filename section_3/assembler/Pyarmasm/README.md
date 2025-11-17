
# I would call making a hello world and make a verilog cpu that could run the "hello world"  is a win


| 阶段                   | 输入       | 输出       | 功能                    |
| -------------------- | -------- | -------- | --------------------- |
| **1. 词法分析（Lexing）**  | 汇编源码字符串  | token 列表 | 把源代码拆成最小的语法单位         |
| **2. 语法分析（Parsing）** | token 列表 | 指令抽象结构   | 确定每条指令的组成和操作数         |
| **3. 编码（Encoding）**  | 指令结构     | 机器码（整数）  | 按 ARM7 编码规则翻译成二进制     |
| **4. 输出（Writing）**   | 机器码列表    | 文件       | 写入 `.bin` 或 `.obj` 文件 |



Lex 

接受内容

输出为Tokens

先定义Tokens有哪些

TOKEN_SPEC = [
    ("COMMENT" , r"" )
    ("REGISTER", )
    ("INSTR", )
    ("CONDITION")
    ("SEP")
    ("SKIP", )
    ("IMM", )
    ("LABEL") ;; normal label 
    ("LABEL_DEF") ;; end with : 
    ("NEWLINE")
    ("MISMATH")

]

Parser: from tokens -> AST 

Program

 ├── InstrNode(opcode="MOV", operands=[
 │      RegNode("R0"),
 │      ImmNode(1)
 │  ])


 ├── InstrNode(opcode="MOV", operands=[
 │      RegNode("R0"),
 │      ImmNode(1)
 │  ])
 └── InstrNode(opcode="ADD", operands=[
        RegNode("R1"),
        RegNode("R0"),
        ImmNode(2)
    ])

Parser 

take the tokens -> AST

How?

写一个遍历tokens的方法
写一个更新当前指针位置的方法


# from Tokens -> AST

# Program(Instructions) -> Instruction[op, operands] -> parse_operand


ask myself some problems 
how to turn tokens in to ast
simple, write some ast classes and use recursion to put Instructions into program , put instruction to the instructions list, parse opcode(MOV) and operands(REG, IMM...)
The final Program(instructions) is the ast tree

how to turn ast input machine code 

PC program counter(下一条要执行的指令的地址)

CPU 工作流程
1. 从内存地址 = PC 的位置取指令
2. 执行该指令
3. PC += 指令长度
4. 回到步骤 1

PC 决定 CPU 去哪里取指令

PC 决定程序的执行顺序

So i need to record pc

当前指令的 PC = 前面所有指令长度的累加


