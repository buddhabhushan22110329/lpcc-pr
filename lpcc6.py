# Assembly code with macro definitions
assembly_code = [
    #Q 6
    # "LOAD A",
    # "STORE B",
    # "MACRO ABC",
    # "LOAD p",
    # "SUB q",
    # "MEND",
    # "MACRO ADD1 ARG",
    # "LOAD X",
    # "STORE ARG",
    # "MEND",
    # "MACRO ADD5 A1, A2, A3",
    # "STORE A2",
    # "ADD1 5",
    # "ADD1 10",
    # "LOAD A1",
    # "LOAD A3",
    # "MEND",
    # "ABC",
    # "ADD5 D1, D2, D3",
    # "END",
    
    #Q 7
    "LOAD J",
    "STORE M",
    "MACRO EST1",
    "LOAD e",
    "ADD d",
    "MEND",
    "MACRO EST ABC",
    "EST1",
    "STORE ABC",
    "MEND",

    "MACRO ADD7 P4, P5, P6"
    "LOAD P5",
    "EST 8",
    "SUB4 2",
    "STORE P4",
    "STORE P6",
    "MEND",
    "EST",
    "ADD7 C4, C5, C6",
    "END",
]

# Define Macro Definition Table (MDT) and Macro Name Table (MNT)
macro_definition_table = []
macro_name_table = {}

current_macro_name = None
current_macro_start = None

# Parse the assembly code to find macro definitions
for line in assembly_code:
    parts = line.split()
    if len(parts) == 0:  # it checks if there is any meaningful tokens to process, if no just continue to next line
        continue

    if parts[0] == "MACRO":
        # Start of a new macro definition
        current_macro_name = parts[1]
        current_macro_start = len(macro_definition_table)  # Starting index in MDT
    elif parts[0] == "MEND":
        # End of the current macro definition
        if current_macro_name:
            # Update the MNT with macro name and start index in MDT
            macro_name_table[current_macro_name] = current_macro_start
            current_macro_name = None
            current_macro_start = None
    else:
        if current_macro_name:
            # Add macro body lines to the MDT
            macro_definition_table.append(line)

# Display the Macro Name Table (MNT)
print("Macro Name Table (MNT):")
print("Macro Name\tMDT Index")
for macro_name, mdt_index in macro_name_table.items():
    print(f"{macro_name}\t\t{mdt_index}")

# Display the Macro Definition Table (MDT)
print("\nMacro Definition Table (MDT):")
print("MDT Index\tInstruction")
for index, instruction in enumerate(macro_definition_table):
    print(f"{index}\t\t{instruction}")
