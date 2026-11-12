"Pag print sa tape"

from tape import read_cell

def format_tape(tape, head):
    # Format sa tape para sa pag print, i show ang head position
    end = max(len(tape) - 1, head)
    index_line = "index: "
    tape_line = "tape:  "
    head_line = "head:  "
    for i in range(end + 1):
        index_line = index_line + str(i).rjust(3)
        tape_line = tape_line + read_cell(tape, i).rjust(3)
        if i == head:
            head_line = head_line + "^".rjust(3)
        else:
            head_line = head_line + "   "
    return index_line + "\n" + tape_line + "\n" + head_line

def format_instruction(ins):
    op = ins["op"]
    if op == "WRITE":
        return "WRITE " + ins["symbol"] 
    elif op == "GOTO":
        return "GOTO " + ins["target"]
    elif op == "IF":
        return "IF " + ins["symbol"] + " GOTO " + ins["target"]
    else:
        return op

#Testing

if __name__ == "__main__":
    print(format_tape(["1", "0", "1"], 0))
    print()
    print(format_tape(["1", "0", "1", "1"], 3))
    print()
    print(format_tape(["1", "0"], 4))
    print()
    print(format_tape([], 0))
    print()

    print(format_instruction({"op": "IF", "symbol": "_", "target": "append", "line": 4}))