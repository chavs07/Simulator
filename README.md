# Turing tape simulator

# Requirements
 - Python 3.14.7
# How to run
  - From the project folderr:
    python main.py

  The simulator asks for three things:
  1. *Program file: path to program, for example 'programs/append_one.txt'
  2. *Input tape: the starting tape as text, for example '101'. Press enter with nothing types for an empty input.
  3. *Step limit: a positive whole number

  - Controls
  'S' = Step: execute one instruction
  'R' = Run: execute until halt, an error, or the limit
  'X' = Reset: restore the original input, head 0, pc 0, steps 0
  'Q' = Quit
   Keys are not case-sensitive

# AI disclosure
- What AI did
   Explained turing machines basics, and the Syntax of the functions
   Made step-by-step roadmap
   Provided example code
- What I did
   Wrote and tested the code each step
   Ran sample program to test 

# Design
Each file has one job