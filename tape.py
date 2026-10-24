"Pag create sa tape/mo pataas, read and write"


BLANK = '_'

def make_tape(input_text):
    #Himoon ang input test nga tape (list sa letters)
    for char in input_text:
        if char.isspace():
            raise ValueError("Input string cannot contain whitespace.")
    return list(input_text)    

if __name__ == "__main__":
    print(make_tape("101"))
    print(make_tape(""))