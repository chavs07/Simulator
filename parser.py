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
    else:
        raise ValueError(f"Line {line}: unknown instruction '{op}'")

    return instruction

     
# My testing
if __name__ == "__main__":
    #lines = read_program_file("programs/append_one.txt")
    #for line in lines:
    #    print(line)

    lines = read_program_file("programs/append_one.txt")
    for item in parse_lines(lines):
        print(item)

    # clean_line
    print(repr(clean_line("RIGHT  # move")))
    print(repr(clean_line(" # comment only ")))

    # split_label
    print(split_label("start: RIGHT"))
    print(split_label("RIGHT"))

    # check_symbol
    check_symbol("1", 2)
    try:
        check_symbol("10", 4)
    except ValueError as e:
        print(e)

    # check_instruction
    print(check_instruction({"line": 5, "label": None, "tokens": ["RIGHT"]}))
    # {'op': 'RIGHT', 'symbol': None, 'target': None, 'line': 5}

    try:
        check_instruction({"line": 3, "label": None, "tokens": ["Right"]})
    except ValueError as e:
        print(e) #line 3: unknown instruction 'Right'