"Load, Step, Run,Reset, Quit"

from parser import parse_program
from tape import make_tape
from machine import make_machine, checked_step, run, reset
from display import show_machine

def ask_program():
    # ask program file
    while True:
        path = input ("Program file: ")
        try:
            return parse_program(path)
        except FileNotFoundError:
            print("File not found: ", path)
        except ValueError as e:
            print ("Invalid program:", e)

def ask_input():
    #ask input tape
    while True:
        text = input("Input tape (press Enter for empty): ")
        try:
            make_tape(text)
            return text
        except ValueError as e:
            print(e)

def ask_limit():
    #ask step limit
    while True:
        text = input("Step limit: ")
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("Step limit must be a positive number")

#Test
if __name__ == "__main__":
    instructions, labels = ask_program()
    input_text = ask_input()
    step_limit = ask_limit()
    print (len(instructions), "instructions,", repr(input_text), ",", step_limit)