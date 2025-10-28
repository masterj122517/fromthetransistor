.global _start 

.data 
fib_array: .space 40 

.text 
_start: 
  LDR R4, = fib_array  
  ; 假如 R4 = 0x1000 

  MOV R0, #0
  STR R0, [R4], #4 
  ; [0x1000] = 0
  ; R4 -> Ox1004
  MOV R1, #1
  STR R1, [R4], #4
  ; [0x1004] = 1
  ; R4 -> Ox1008

  MOV R2, #2
  MOV R3, #10

loop: 
  CMP R2, R3 
  BGE end_loop 

  ADD R5, R0, R1 
  STR R5, [R4], #4 
  ; [0x1008] = R5
  ; R4 -> Ox1012
  MOV R0, R1
  MOV R1, R5 
  ADD R2, R2, #1
  B loop

end_loop: 
  MOV R7, #1
  MOV R0, #0 
  SVC 0 




