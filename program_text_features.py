# Extracts text features from a single program.
# Appends a line to the output file program_text_features.csv
# with the following format:
# program file name, number of lines, number of words, number of chars

import sys
import csv

if len(sys.argv) < 2:
    print "No arguments passed in."
    print "USAGE: program_text_features.py <program>"
    print "Note: make sure program_text_features.py is in the same directory as the program files if using relative paths."
    exit()

SERENAPROGRAMSDIR = "asc-0.1.4/serena-programs-processed"
    
# Returns a list of features for the given program
def get_features(program):
    lines = 0
    words = 0
    chars = 0
    with open(program, 'rb') as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
    program_number = program[len(SERENAPROGRAMSDIR) + 1:program.find(".c")]
    features = [program_number, lines, words, chars]
    return features

features = get_features(sys.argv[1])

# Write text features to outfile
outfile = 'program_text_features.csv'
with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(features)
