# 8bit-CPU-logisim
This is a basic 8 bit CPU design project that I made to better understand computer architecture. The repository includes the logisim circuit file, an assembler written in python, and a few small assembly programs that can run on the CPU.
## The Datapath
The CPUs datapath includes 6 8 bit registers: PC, IR, MAR, MDR, ACC, OUT, an ALU with 8 options, 2 flip flops used as flags to implement branching instructions, as well as 2 hex displays for output. Finally, it includes a Control Unit, that sends the appropriate signals to each component of the CPU in order for each instruction to be properly executed.

<img width="1094" height="782" alt="{86E5D2F6-C4F6-46F0-8940-70857B8B1C7E}" src="https://github.com/user-attachments/assets/e7c95c0a-a119-4bcd-ba46-a3272711994b" />

## The ALU
The ALU is comprised by 8 smaller 1 bit ALUs that allow a specific operation between A and B to pass to C, depending on the selection bits (the 3 bit input on the top right). 
- The 1 bit input on the top is the sub signal. It is used to toggle between addition and subtraction, since they share the same circuitry, and hence the same select bits.
- The messy wires that connect the "Nright" and "Nleft" of each 1 bit ALU are used for shift operations
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

## The Registers
The CPU has 6 specific purpose registers, that communicate via a data bus:
| Register | Mnemonic | Description |
|----------|----------|-------------|
| **`Memory Address Register`** | **`MAR`** | Holds memory addresses that are used to read/write to RAM |
| **`Memory Data Register`** | **`MDR`** | Holds data that are read/written to RAM |
| **`Program Counter`** | **`PC`** | Keeps track of the current instruction address. It's value is incremented by 1 at the start of every instruction (unless it's a branching instruction), in order to access the next |
| **`Accumulator`** | **`ACC`** | Is used as an operand for every arithmetic or logical operation |
| **`Instruction Register`** | **`IR`** | Holds the current instruction that's being executed and passes it as input to the control unit |
| **`Out Register`** | **`OUT`** | Holds the value that is shown by the 2 hex displays |

## The Instruction Set
The CPU includes 26 instructions. Those with an operand (like "ADD x" or "JMP x") are 16 bits long, with the upper 8 bits being used for the opcode and the 8 lower for the memory address. This allows the CPU to access 256 bytes of memory, but requires 2 separate memory fetches for each 16 bit instruction, since the data bus and the registers are only 8 bits long. Instructions without an operand (like "OUT" or "HLT") are 8 bits long and only require a single fetch before executing. The table below describes the 26 instructions: 
| Opcode | Mnemonic | Description |
| :--- | :--- | :--- |
| **`0x00`** | **`ADD`** | Adds a value from a specific memory address to the Accumulator. |
| **`0x01`** | **`SUB`** | Subtracts a value at a specific memory address from the Accumulator. |
| **`0x02`** | **`AND`** | Performs a bitwise AND operation between memory and the Accumulator. |
| **`0x03`** | **`OR`** | Performs a bitwise OR operation between memory and the Accumulator. |
| **`0x04`** | **`XOR`** | Performs a bitwise XOR operation between memory and the Accumulator. |
| **`0x05`** | **`NAND`** | Performs a bitwise NAND operation between memory and the Accumulator. |
| **`0x06`** | **`SLL`** | Shift Left Logical: Shifts all Accumulator bits left by 1. (Multiplies by 2). |
| **`0x07`** | **`SRL`** | Shift Right Logical: Shifts all Accumulator bits right by 1, filling the left bit with 0. |
| **`0x08`** | **`SRA`** | Shift Right Arithmetic: Shifts right by 1, but preserves the sign bit (Bit 7). |
| **`0x09`** | **`NOT`** | Bitwise NOT: Inverts all bits currently inside the Accumulator. |
| **`0x0A`** | **`NANDI`** | Performs a bitwise NAND operation with an 8-bit constant value. |
| **`0x0B`** | **`ADDI`** | Adds an 8-bit constant value directly to the Accumulator. |
| **`0x0C`** | **`ANDI`** | Performs a bitwise AND operation with an 8-bit constant value. |
| **`0x0D`** | **`ORI`** | Performs a bitwise OR operation with an 8-bit constant value. |
| **`0x0E`** | **`XORI`** | Performs a bitwise XOR operation with an 8-bit constant value. |
| **`0x0F`** | **`LDA`** | Load Accumulator: Loads the value from a specific memory address into the Accumulator. |
| **`0x10`** | **`STA`** | Store Accumulator: Saves the current Accumulator value into a specific memory address. |
| **`0x11`** | **`LDI`** | Load Immediate: Loads an 8-bit constant value directly into the Accumulator. |
| **`0x12`** | **`CMP`** | Compare: Subtracts a memory value from the Accumulator to set flags, discarding the result. |
| **`0x13`** | **`CMPI`** | Compare Immediate: Compares the Accumulator against an 8-bit constant value. |
| **`0x14`** | **`JEQ`** | Jump if Equal: Jumps to an address if the Zero flag is set (ACC == Operand). |
| **`0x15`** | **`JNE`** | Jump if Not Equal: Jumps to an address if the Zero flag is cleared (ACC != Operand). |
| **`0x16`** | **`JMP`** | Jump: Unconditionally sets the Program Counter to the specified memory address. |
| **`0x17`** | **`JGT`** | Jump if Greater Than: Jumps to an address if ACC > Operand (Zero & Negative flags are clear). |
| **`0x18`** | **`JLT`** | Jump if Less Than: Jumps to an address if ACC < Operand (Negative flag is set). |
| **`0x19`** | **`OUT`** | Output: Pushes the current Accumulator value to the Hexadecimal Display. |
| **`0x1A`** | **`HLT`** | Halt: Stops the CPU clock completely. |
