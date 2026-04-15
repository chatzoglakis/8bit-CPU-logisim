# 8bit-CPU-logisim
This is a basic 8 bit CPU design project that I made to better understand computer architecture. The repository includes the logisim circuit file, an assembler written in python, and a few small assembly programs that can run on the CPU.
## The Datapath
The CPUs datapath includes 6 8 bit registers: PC, IR, MAR, MDR, ACC, OUT, an ALU with 8 options, 2 flip flops used as flags to implement branching instructions, as well as 2 hex displays for output. Finally, it includes a Control Unit, that sends the appropriate signals to each component of the CPU in order for each instruction to be properly executed.

<img width="1094" height="782" alt="{86E5D2F6-C4F6-46F0-8940-70857B8B1C7E}" src="https://github.com/user-attachments/assets/e7c95c0a-a119-4bcd-ba46-a3272711994b" />

## The ALU
The ALU is comprised by 8 smaller 1 bit ALUs that allow a specific operation between A and B to pass to C, depending on the selection bits (the 3 bit input on the top right). 
- The 1 bit input on the top is the sub signal. It is used to toggle between addition and subtraction, since they share the same circuitry, and hence the same select bits.
- The messy wires that connect the "Nright" and "Nleft" are used for shift operations
- The 1 bit input at the left bottom is the "ash" signal. It is used to toggle between logical and arithmetic shifts (the latter are used in signeed numbers, allowing them to retain their sign bit during shifts)
<img width="776" height="821" alt="{54A11552-550F-4561-8B95-6C48C1418330}" src="https://github.com/user-attachments/assets/346962ed-3aea-4e10-a177-b7bc74e6120b" />

The operations supported by each 1 bit ALU are the following:
- Addition (B + A)
- Subtraction (B - A)
- NAND
- AND
- OR
- XOR
- Left Shift
- Right Shift
- NOT (NOT B)

<img width="837" height="817" alt="{EAC9C4ED-B94D-40F2-BB7F-407475E02A64}" src="https://github.com/user-attachments/assets/befe343d-52b7-4ab2-acb3-619af72c5796" />
