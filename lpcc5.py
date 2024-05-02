class macro_processor:
    def __init__(self):
        self.macro_table = {}

    def pass_one(self,source_code):
        lines = source_code.split('\n')
        macro_name = None
        macro_definition = None
        for line in lines:
            tokens = line.split()
            if len(tokens) == 0:
                continue
            if tokens[0] == 'MACRO':
                macro_name = tokens[1]
                macro_definition = []
            elif tokens[0] == 'MEND':
                self.macro_table[macro_name] = macro_definition
                macro_name = None
                macro_definition = None
            elif macro_definition is not None:
                macro_definition.append(line)
    
    def pass_two(self,source_code):
        intermediate_code = []
        lines = source_code.split('\n')
        for line in lines:
            tokens = line.split()
            if len(tokens) == 0:
                continue
            if tokens[0] in self.macro_table:
                macro_definition = self.macro_table[tokens[0]]
                arguments = tokens[1:]
                for macro_line in macro_definition:
                    macro_tokens = macro_line.split()
                    if len(macro_tokens) == 0:
                        continue
                    for i,token in enumerate(macro_tokens):
                        if token == 'ARG':
                            macro_tokens[i] = arguments.pop(0)
                    intermediate_code.append(" ".join(str(token) for token in macro_tokens))
            else:
                intermediate_code.append(line)
        return intermediate_code

if __name__ == "__main__":
    macro = macro_processor()
    source_code = """"
    LOAD A
MACRO ABC
LOAD p
SUB q
MEND
STORE B
MULT D
MACRO ADD1 ARG
LOAD X
STORE ARG
MEND
LOAD B
MACRO ADD5 A1, A2, A3
STORE A2
ADD1 5
ADD1 10
LOAD A1
LOAD A3
MEND
END
"""
    macro.pass_one(source_code)
    intermediate_code = macro.pass_two(source_code)
    print("Intermediate Code:")
    for code in intermediate_code:
        print(code)