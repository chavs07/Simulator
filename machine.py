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