//This Program implements the Russian Peasant Algorithm to multiply the numbers 5 and 3

LDI 00
STA FD     // FD holds the final result

LDI 05     // Multiplier
STA FF
LDI 03     // Multiplicand
STA FE

loop:
LDA FF
CMPI 00
JEQ exit     //jump at the end if one

ANDI 01    // AND A with 1. (If A is odd, result is 1. If even, result is 0)
CMPI 00
JEQ shifts     // If the result was 0 (A is even), skip the addition

//ADDITION
LDA FD
ADD FE
STA FD

shifts:
LDA FE
SLL
STA FE

LDA FF
SRL
STA FF

JMP loop

exit:
//OUTPUT RESULT
LDA FD
OUT
HLT
