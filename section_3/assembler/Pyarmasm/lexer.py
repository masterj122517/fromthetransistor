import re
class Lexer:
    def __init__(self) -> None:
        TOKEN_SPEC = [
            ("COMMENT", r";.*"),                    # 注释
            ("LABEL_DEF", r"[A-Za-z_]\w*:"),        # 标签定义（以冒号结尾）
            ("INSTR", r"\b(ADD|SUB|MOV|B)\b"),      # 指令（可扩展）
            ("REG", r"\bR(1[0-5]|[0-9])\b"),        # R0~R15
            ("IMM", r"#-?\d+"),                     # 立即数 #5, #-3
            ("SEP", r","),                          # 逗号分隔符
            ("LABEL", r"[A-Za-z_]\w*"),             # 普通标识符
            ("NEWLINE", r"\n"),                     # 换行
            ("SKIP", r"[ \t]+"),                    # 空格或 Tab
            ("MISMATCH", r"."),                     # 其他不匹配字符
        ]
        self.scanner = re.Scanner([
            (regex, (lambda s, t, name = name:(name, t)))
            for name, regex in TOKEN_SPEC
        ])

    def tokenize(self, input):
        tokens, unknown = self.scanner.scan(input)
        return [(t, v) for t, v in  tokens  if t != "SKIP"]

