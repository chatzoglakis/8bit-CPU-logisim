import sys

opcodes =\
    {"ADD": "00",
     "SUB": "01",
     "AND": "02",
     "OR": "03",
     "XOR": "04",
     "NAND": "05",
     "SLL": "06",
     "SRL": "07",
     "SRA": "08",
     "NOT": "09",
     "NANDI": "0a",
     "ADDI": "0b",
     "ANDI": "0c",
     "ORI": "0d",
     "XORI": "0e",
     "LDA": "0f",
     "STA": "10",
     "LDI": "11",
     "CMP": "12",
     "CMPI": "13",
     "JEQ": "14",
     "JNE": "15",
     "JMP": "16",
     "JGT": "17",
     "JLT": "18",
     "OUT": "19",
     "HLT": "1a"}

if len(sys.argv) != 2:
    print("SYNTAX ERROR\n correct format should be \"python assembler.py <filename>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = "code.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

machine_code = []

for line in lines:
    line = line.split("//")[0].strip().upper()
    if not line:
        continue

    fields = line.split(" ")
    instruction = fields[0]

    if instruction in opcodes:
        machine_code.append(opcodes[instruction] + ' ')

        if len(fields) > 1:
            operand = fields[1]
            machine_code.append(operand + ' ')

    else:
        print("ERROR: UNKNOWN INSTRUCTION: " + instruction)
        sys.exit(1)

with open(output_file, 'w') as file:
    file.write("v2.0 raw\n")
    for element in machine_code:
        file.write(element)

print("ASSEMBLY SUCCESSFUL")

