import csv, os.path, sys

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

def read_from_csv(filename):
    result =''
    with open(filename, newline='') as f:
        csv_reader = csv.reader(f)
        try:
            for row in csv_reader:
                if result =='':
                    result = row
                else:
                    result = result + "\n" + row
        except csv.Error as ce:
            sys.exit(f"the line {csv_reader.line_num} in the file {filename} has error: {ce} ")

def write_to_csvfile(filename, list2write):
    with open(filename, 'w', newline='') as f:
        try:
            csv_writer = csv.writer(f)
            csv.writerrows(list2write)
        except csv.Error as ce:
            sys.exit(f"error in writing to the file {filename}: {ce}")
