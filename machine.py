"Ang state, execute sa mga commands/run"

from tape import make_tape, read_cell, write_cell

def reset(machine):
    # Reset the machine state to initial values. head 0, pc 0, steps 0
    machine['tape'] = make_tape(machine["input_text"])
    machine['head'] = 0
    machine['pc'] = 0
    machine['steps'] = 0
    machine["status"] = "READY"

def make_machine(instructions, labels, input_text, step_limit):

    # Create a new machine state with the given instructions, labels, input text, and step limit.
    if step_limit <= 0:
        raise ValueError("Step limit must be a positive number")
    machine = {
        "instructions": instructions,
        "labels": labels,
        "input_text": input_text,
        "step_limit": step_limit,
    }
    reset(machine)
    return machine

def do_left(machine):
    # Move pa left, stay if naa na sa cell 0 (one way tape)
    if machine["head"] > 0:
        machine["head"] = machine["head"] - 1
    machine["pc"] = machine["pc"] + 1

def do_right(machine):
    # Move pa right
    machine["head"] = machine["head"] + 1
    machine["pc"] = machine["pc"] + 1

def do_write(machine, symbol):
    # Write the symbol to the current cell
    write_cell(machine["tape"], machine["head"], symbol)
    machine["pc"] = machine["pc"] + 1

def do_goto(machine, target):
    # GOTOT label, jump sa label
    machine["pc"] = machine["labels"][target]

def do_if(machine, symbol, target):
    # IF symbol GOTO label, jump sa label if the current cell matches the symbol
    if read_cell(machine["tape"], machine["head"]) == symbol:
        machine["pc"] = machine["labels"][target]
    else:
        machine["pc"] = machine["pc"] + 1

def do_halt(machine):
    # HALT, stop the machine
    machine["status"] = "HALTED"

def step(machine):
    # Execute and usa ka instruction based on the current program counter
    instruction = machine["instructions"][machine["pc"]]
    op = instruction["op"]

    if op == "LEFT":
        do_left(machine)
    elif op == "RIGHT":
        do_right(machine)
    elif op == "WRITE":
        do_write(machine, instruction["symbol"])
    elif op == "GOTO":
        do_goto(machine, instruction["target"])
    elif op == "IF":
        do_if(machine, instruction["symbol"], instruction["target"])
    elif op == "HALT":
        do_halt(machine)
    
    machine["steps"] = machine["steps"] + 1

def is_finished(machine):
    # Check if the machine has finished executing 
    status = machine["status"]
    return status == "HALTED" or status == "ERROR" or status == "LIMIt REACHED"

def checked_step(machine):
    # I check ang machine before executing
    if is_finished(machine):
        raise ValueError("Machine has already finished executing. Reset first")
    if machine["pc"] >= len(machine["instructions"]):
        machine["status"] = "ERROR"
        return
    if machine["steps"] >= machine["step_limit"]:
        machine["status"] = "LIMIT REACHED"
        return
    step(machine)

def run(machine):
    # Run the machine until it finishes executing
    if is_finished(machine):
        raise ValueError("Machine has already finished executing. Reset first")
    while not is_finished(machine):
        checked_step(machine)
    

# Testing

if __name__ == "__main__":
    from parser import parse_program

    instructions, labels = parse_program("programs/append_one.txt")
    m = make_machine(instructions, labels, "101", 100)
    print(m["tape"], m["head"], m["pc"], m["steps"], m["status"])
    # ['1', '0', '1'] 0 0 0 READY

    print("\n--- reset ---")
    m["tape"][0] = "X"          # kunohay gi-usab sa program
    m["head"] = 5
    m["steps"] = 9
    reset(m)
    print(m["tape"], m["head"], m["pc"], m["steps"], m["status"])
    # ['1', '0', '1'] 0 0 0 READY   ← nabalik!

    print("\n--- errors ---")
    try:
        make_machine(instructions, labels, "101", 0)
    except ValueError as e:
        print(e)                # Step limit must be a positive number

    print("\n--- do_step ---")
    m = make_machine(instructions, labels, "101", 100)
    for i in range(12):
        step(m)
        print(m["steps"], m["pc"], m["head"], m["tape"], m["status"])

    print("\n--- run ---")
    m = make_machine(instructions, labels, "101", 100)
    run(m)
    print(m["tape"], m["head"], m["pc"], m["steps"], m["status"])

    print("\n--- Run the file that no stop---")
    instructions, labels = parse_program("programs/no_halt.txt")
    m = make_machine(instructions, labels, "10", 100)
    run(m)
    print(m["steps"], m["tape"], m["status"])
