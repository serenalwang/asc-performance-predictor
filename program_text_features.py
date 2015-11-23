# Extracts text features from a program.
# Produces an output file program_text_features.csv with the following format:
# program file name, number of lines, number of words, number of chars

import sys
import csv

if len(sys.argv) < 2:
    print "No arguments passed in."
    print "-c: add this flag before the program arguments to clear the program_text_features.csv file."
    print "USAGE: program_text_features.py [-c] <program 1> <program 2> ..."
    print "Note: make sure program_text_features.py is in the same directory as the program files if using relative paths."
    exit()

programs = []
write_protocol = 'ab'
program_arg_start = 1
if sys.argv[1] == '-c':
    write_protocol = 'wb'
    program_arg_start = 2

for filename in sys.argv[program_arg_start:]:
    programs.append(filename)

allfeatures = []
for program in programs:
    lines = 0
    words = 0
    chars = 0
    with open(program, 'rb') as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
    features = [program, lines, words, chars]
    allfeatures.append(features)

# Write text features to outfile
outfile = 'program_text_features.csv'
with open(outfile, write_protocol) as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in allfeatures:
        writer.writerow(row)