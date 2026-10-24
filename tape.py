"Pag create sa tape/mo pataas, read and write"


BLANK = '_'

def make_tape(input_text):
    #Himoon ang input text nga tape (list sa letters)
    for char in input_text:
        if char.isspace():
            raise ValueError("Input string cannot contain whitespace.")
    return list(input_text)    

def read_cell(tape, head):
    # I hatag and symbol sa position sa head. kung lapas ba sa tumoy, e hatag ang BLANK
    if head >= len(tape):
        return BLANK
    return tape[head]

def write_cell(tape, head, symbol):
    # I sulat ang symbol sa position sa head. kung lapas sa tumoy, e extend ang tape
    while head >= len(tape):
        tape.append(BLANK)        # append BLANK
    tape[head] = symbol


# My testing
if __name__ == "__main__":
    #make_tape test         
    print(make_tape("101"))
    print(make_tape(""))

    #read cell
    print(read_cell(['1', '0', '1'], 1))
    print(read_cell([],0))

    #write_cell 
    t = ['1', '0', '1']
    write_cell(t, 5, 'X')
    print(t) 

    t = ['1', '0', '1']
    write_cell(t, 2, 'X')
    print(t)

    t = ['1', '0', '1']
    write_cell(t, 0, BLANK)
    print(t)