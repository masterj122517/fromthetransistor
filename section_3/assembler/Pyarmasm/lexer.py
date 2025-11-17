# lexer.py
import re

class Lexer:
    def __init__(self) -> None:
        TOKEN_SPEC = [
            ("COMMENT",     r";[^\n]*"),                     # 注释
            ("LABEL_DEF",   r"[A-Za-z_]\w*:"),               # 标签定义 e.g. loop:
            ("INSTR",       r"\b(?:MOV|ADD|SUB|B|OUT|HALT)\b"), # 指令
            ("REG",         r"\bR(?:1[0-5]|[0-9])\b"),       # R0~R15
            ("IMM",         r"#-?\d+"),                     # 立即数 #5, #-3
            ("ID",          r"\b[A-Za-z_]\w*\b"),           # 标识符（标签名引用）
            ("SEP",         r","),                          # 逗号
            ("NEWLINE",     r"\n"),                         # 换行
            ("SKIP",        r"[ \t\r]+"),                   # 空格或 Tab 或 回车
            ("MISMATCH",    r"."),                          # 其他
        ]
        # re.Scanner 需要 (pattern, action) 列表
        self.scanner = re.Scanner([
            (regex, (lambda s, t, name=name: (name, t)))
            for name, regex in TOKEN_SPEC
        ], flags=re.IGNORECASE)

    def tokenize(self, input_text):
        tokens, unknown = self.scanner.scan(input_text)
        # 过滤 SKIP 和 COMMENT，保证 NEWLINE 保留
        result = [(t.upper(), v) for t, v in tokens if t not in ("SKIP", "COMMENT")]
        return result
