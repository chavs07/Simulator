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

def describe_next(machine):
    # Describe the next instruction to be executed
    status = machine["status"]
    if status == "HALTED":
        return "Machine has halted"
    if status == "ERROR":
        return "Machine has encountered an error, no HALT instruction found"
    if status == "LIMIT REACHED":
        return f"Machine has reached the step limit of {machine['step_limit']}"
    if machine["pc"] >= len(machine["instructions"]):
        return "(end of the program)"
    return format_instruction(machine["instructions"][machine["pc"]])

def show_machine(machine):
    # Print whole config
    print(format_tape(machine["tape"], machine["head"]))
    print(f"head={machine['head']} pc={machine['pc']} steps={machine['steps']}")
    print("next: " + describe_next(machine))

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

#format_instruction
    print(format_instruction({"op": "IF", "symbol": "_", "target": "append", "line": 4}))

print(" - -  -showw machinee -- - -")
from parser import parse_program
from machine import make_machine, checked_step, run

instruction, labels = parse_program("programs/append_one.txt")
m = make_machine(instruction, labels, "101", 100)
show_machine(m)
print()
checked_step(m)
checked_step(m)
show_machine(m)
print()
run(m)
show_machine(m)