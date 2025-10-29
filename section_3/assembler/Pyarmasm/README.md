

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

