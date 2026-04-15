LDI 00
STA FD     // FD holds the final result

LDI 05     // Multiplier (A)
STA FF
LDI 03     // Multiplicand (B)
STA FE

//LOOP START (starts at byte 0C)
LDA FF
CMPI 00
JEQ 2A     //jump at the end if one

ANDI 01    // AND A with 1. (If A is odd, result is 1. If even, result is 0)
CMPI 00
JEQ 1E     // If the result was 0 (A is even), skip the addition

//ADDITION
LDA FD
ADD FE
STA FD

//SHIFTS (starts at byte 1E)
LDA FE
SLL
STA FE

LDA FF
SRL
STA FF

JMP 0C

//OUTPUT RESULT
LDA FD
OUT
HLT
