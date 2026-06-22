import sys

def find_labels(lines):
    label_addresses = {}
    curr_byte = 0

    for line in lines:
        # check for comments
        line = line.split("//")[0].strip().upper()
        if not line:
            continue

        fields = line.split(" ")

        if ":" in line:
            label = line.split(":")[0]
            num_string = str(hex(curr_byte))
            num_string = num_string.replace("0x", "") #remove 0x so that only the hex number remains
            label_addresses[label] = num_string

            if len(fields) > 2:
                curr_byte += 2
            elif len(fields) > 1:
                curr_byte += 1
        else:
            if len(fields) > 1:
                curr_byte += 2
            else:
                curr_byte += 1


    return label_addresses

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

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("SYNTAX ERROR\n correct format should be \"python assembler.py <src filename> <dst filename>(optional)")
    sys.exit(1)

input_file = sys.argv[1]
if len(sys.argv) == 3:
    output_file = sys.argv[2]
else:
    output_file = "code.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

labels = find_labels(lines)

machine_code = []

for line in lines:
    #check for comments
    line = line.split("//")[0].strip().upper()
    if not line:
        continue

    # check if there is a label "declaration"
    has_label_declaration = False
    declared_label = ""
    if ":" in line:
        has_label_declaration = True
        declared_label = line.split(":")[0]

    fields = line.split(" ")
    index = 0
    if has_label_declaration:
        index += 1
        if len(fields) == 1:
            continue

    instruction = fields[index]

    if instruction in opcodes:
        machine_code.append(opcodes[instruction] + ' ')

        if len(fields) > 1:
            index += 1
            operand = fields[index]
            if operand in labels and operand != declared_label:
                operand = labels[operand]
            machine_code.append(operand + ' ')
    else:
        print("ERROR: UNKNOWN INSTRUCTION: " + instruction)
        sys.exit(1)

with open(output_file, 'w') as file:
    file.write("v2.0 raw\n")
    for element in machine_code:
        file.write(element)

print("ASSEMBLY SUCCESSFUL")
