"Read the program file/ validate if  valid"

def read_program_file(path):
    # I read ang program file, ehatag ang list sa lines
    with open(path) as f:           #open the file
        return f.read().splitlines()

def clean_line(line):
    # I clean ang line, e remove ang comments and whitespace
    line = line.split('#')[0]      # remove comments
    return line.strip()              # remove whitespace

def split_label(text):
    # I split ang label sa command
    tokens = text.split()
    if tokens[0].endswith(':'):
        label = tokens[0][:-1]  # remove the colon
        return label, tokens[1:]  # return label and ang nabilin
    return None, tokens

def parse_lines(lines):
    # Himuon ang mgs linya nga list sa dicts; laktawan and blank line and comment
    result = []
    for number, line in enumerate(lines, start=1): #count line, from 1
        text = clean_line(line)
        if text == '':
            continue
        label, tokens = split_label(text)
        result.append({'line': number, 'label': label, 'tokens': tokens})
    return result

def check_symbol(symbol, line):
    # I check if ang symbol is valid / must 1 letter
    if len(symbol) != 1:
        raise ValueError(f"Line{line}: symbol must be one character, got '{symbol}'")

def check_instruction(item):
    # E check ang usa ka line, i give ang intruction dict kung valid
    tokens = item['tokens']
    line = item['line']

    if len(tokens) == 0:
        raise ValueError(f"Line {line}: no instruction found")
    
    op = tokens[0]
    instruction = {'op': op, "symbol": None, "target": None, "line": line}

    if op == "LEFT" or op == "RIGHT" or op == "HALT":
        if len(tokens) != 1:
            raise ValueError(f"Line {line}: '{op}' takes no arguments")
    elif op == "WRITE":
        if len(tokens) != 2:
            raise ValueError(f"Line {line}: use WRITE symbol")
        check_symbol(tokens[1], line)
        instruction['symbol'] = tokens[1]
    
    elif op == "GOTO":
        if len(tokens) !=2:
            raise ValueError(f"Line {line}: use GOTO label")
        instruction['target'] = tokens[1]
    
    elif op == "IF":
        if len(tokens) != 4 or tokens[2] != "GOTO":
            raise ValueError(f"Line {line}: use IF symbol GOTO label")
        check_symbol(tokens[1], line)
        instruction['symbol'] = tokens[1]
        instruction['target'] = tokens[3]

    else:
        raise ValueError(f"Line {line}: unknown instruction '{op}'")

    return instruction

def build_labels(items):
    # Himuon ang labels table, name sa label to index sa instruction
    labels = {}
    for index, item in enumerate(items):
        label = item['label']
        if label is not None:
            if label in labels:
                raise ValueError(f"Line {item['line']}: duplicate label '{label}'")
            labels[label] = index
    return labels

def check_targets(instructions, labels):
    # checks if all the targets in the instructions are valid labels or naa ba sa labels table
    for item in instructions:
        target = item['target']
        if target is not None and target not in labels:
            raise ValueError(f"Line {item['line']}: undefined label '{target}'")

def parse_program(path):
    # Basahon ug i validate anf tibuok program file, return the instructions and labels table
    lines = read_program_file(path)
    items = parse_lines(lines)

    if len(items) == 0:
        raise ValueError("Program is empty")
    
    instructions = []
    for item in items:
        instructions.append(check_instruction(item))

    labels = build_labels(items)
    check_targets(instructions, labels)
    return instructions, labels


# My testing
if __name__ == "__main__":
    lines = read_program_file("programs/append_one.txt")
    for line in lines:
        print(line)

    lines = read_program_file("programs/append_one.txt")
    for item in parse_lines(lines):
        print(item)

    print()
    # clean_line
    print(repr(clean_line("RIGHT  # move")))
    print(repr(clean_line(" # comment only ")))

    print()
    # split_label
    print(split_label("start: RIGHT"))
    print(split_label("RIGHT"))

    print()
    # check_symbol
    check_symbol("1", 2)
    try:
        check_symbol("10", 4)
    except ValueError as e:
        print(e)

    print()
    # check_instruction
    print(check_instruction({"line": 5, "label": None, "tokens": ["RIGHT"]}))
    # {'op': 'RIGHT', 'symbol': None, 'target': None, 'line': 5}

    try:
        check_instruction({"line": 3, "label": None, "tokens": ["Right"]})
    except ValueError as e:
        print(e) #line 3: unknown instruction 'Right'

    print(check_instruction({"line": 7, "label": None, "tokens": ["WRITE", "1"]}))

    print(check_instruction({"line": 4, "label": None, "tokens": ["IF", "_", "GOTO", "end"]}))

    try:
        check_instruction({"line": 6, "label": None, "tokens": ["IF", "_", "GOTO"]}) #error kay 3 ra kabuok walay label
    except ValueError as e:
        print(e) #line 6: unknown instruction 'IF _ GOTO' walay label s

    print()
    #build_labels
    items = parse_lines(read_program_file("programs/append_one.txt"))
    print(build_labels(items))
    try:
        build_labels([{'line': 1, 'label': 'loop', 'tokens': ['RIGHT']},
                  {'line': 2, 'label': 'loop', 'tokens': ['HALT']}])
    except ValueError as e:
        print(e) #line 2: duplicate label 'loop'

    #check_targets

    
    print("\n--- parse_program ---")
    instructions, labels = parse_program("programs/append_one.txt")
    for item in instructions:
        print(item)
    print(labels)

    try:
        parse_program("programs/bad_label.txt")
    except ValueError as e:
        print(e) #line 1: undefined label 'nowhere'
