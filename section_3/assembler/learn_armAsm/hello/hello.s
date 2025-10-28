.global _start

.data
msg:    .asciz "Hello, world!\n"

.text
_start:
    LDR R0, =1          @ 文件描述符 1 = stdout
    LDR R1, =msg        @ R1 = 字符串地址
    LDR R2, =14         @ R2 = 字符串长度
    MOV R7, #4          @ 系统调用号 4 = sys_write
    SVC 0               @ 调用内核（打印）

    MOV R7, #1          @ 系统调用号 1 = sys_exit
    MOV R0, #0          @ 返回值 0
    SVC 0
