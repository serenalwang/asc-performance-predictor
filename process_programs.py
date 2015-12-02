# Replaces all instances of scanf in infile with actual
# variable assignments, and writes the new file to outfile.
# Does not modify infile.

import random, string
import sys

# Returns a random string of length between 1 and 20.
def randomstring():
    length = random.randint(1,20)
    return ''.join(random.choice(string.lowercase) for i in range(length))

# Returns a random hex string of length between 1 and 20.
def randomhex():
    length = random.randint(1,20)
    return ''.join(random.choice('0123456789abcdef') for i in range(length))

# Returns a random string of a given type. Type should be a string
# passed into scanf, such as 'd' or 's'.
def get_random(type):
    if type == 'd' or type == 'u' or type == 'i':
        return str(random.randint(1,1000))
    elif type == 's':
        print "SCANF TYPE STRING NOT HANDLED. Exiting."
        exit()
        # return "\"" + randomstring() + "\""
    elif type == 'c':
        return "\"" + random.choice(string.lowercase) + "\""
    elif type == 'x':
        return randomhex()
    elif type == 'f':
        return str(random.uniform(1, 1000))
    else:
        print "SCANF TYPE NOT RECOGNIZED. Exiting."
        exit()

# Converts scanf command into a line with arguments.
# Returns the converted line as a string.
def process_scanf(command):
    splitcommand = command.split("\"")
    input_args = splitcommand[1]
    input_vars = splitcommand[2]

    # Separates input_vars into a list of variable names as strings.
    input_vars = input_vars.replace(" ", "")
    input_vars_end = input_vars.find(")")
    input_vars = input_vars[1:input_vars_end]
    input_vars = input_vars.split(",")

    # Separates input_args into a list of scanf types as strings.
    input_types = []
    next_arg = input_args.find("%")
    while next_arg != -1:
        next_type = input_args[next_arg + 1]
        input_types.append(next_type)
        input_args=  input_args[next_arg + 1:]
        next_arg = input_args.find("%")

    assert(len(input_types) == len(input_vars))
    
    output_line = ""
    for i in range(len(input_types)):
        assignment = "*(" + input_vars[i] + ")=" + get_random(input_types[i])
        output_line += assignment + ";"

    return output_line

# Test for process_scanf
# print "Processing scanf(\"%f, %s\", &temp, 2);", process_scanf("scanf(\"%f, %s\", &temp, 2);")

# Replaces all instances of scanf in infile with actual
# variable assignments, and writes the new file to outfile.
# Does not modify infile.
def process_file(infile, outfile):
    print infile
    file_string = ""
    with open(infile, 'r') as f:
        file_string = f.read()

    # Modify file_string to replace instances of scanf
    next_scanf = file_string.find("scanf(")
    while next_scanf != -1:
        if file_string[next_scanf - 1] == "f":
            print "fscanf FOUND! DELETE THIS FILE."
            exit()
        # Get index of end of scanf line.
        scanf_end = file_string[next_scanf:].find(";")
        scanf_command = file_string[next_scanf : next_scanf + scanf_end]
        # Remove newlines and tabs.
        scanf_command = scanf_command.replace('\n','')
        scanf_command = scanf_command.replace('\t','')
        print "scanf_command found:", scanf_command

        # Replace scanf with variable assignments
        replacement_line = process_scanf(scanf_command)
        file_string = file_string[:next_scanf] + replacement_line \
                      + file_string[1 + next_scanf + scanf_end:]
        next_scanf = file_string.find("scanf(")

    # Write file_string to outfile
    with open(outfile, 'w') as f:
        f.write(file_string)

if len(sys.argv) < 3:
    print "Not enough arguments."
    print "USAGE: process_programs.py <infile> <outfile> "
    exit()

process_file(sys.argv[1], sys.argv[2])
