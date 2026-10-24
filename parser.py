"Read the program file/ validate if  valid"

def read_program_file(path):
    # I read ang program file, ehatag ang list sa lines
    with open(path) as f:           #open the file
        return f.read().splitlines()


# My testing
if __name__ == "__main__":
    lines = read_program_file("programs/append_one.txt")
    for line in lines:
        print(line)
