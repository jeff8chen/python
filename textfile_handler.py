

def read_to_string(filename):
    with open(filename) as input_file:
        return input_file.read()

def write_to_file(filename, *content):
    with open(filename, 'w') as output_file:
        for c in content:
            output_file.write(c +"\n")

def append_to_file(filename, *content):
    with open(filename, 'a') as output_file:
        for c in content:
            output_file.write(c +"\n")

def readbyte_from_file(filename):
    with open(filename, "rb") as input_file:
        return input_file.read()

def writebyte_to_file(filename, bytes[])
    with open(filename, "wb") as output_file:
        for b in bytes:
            output_file.write(b)

    
