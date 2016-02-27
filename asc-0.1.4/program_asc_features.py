###
# Extracts all asc features from asc output for a given program
# and breakpoint.
# Usage: ./asc -a <breakpoint> <program binary> <program args> |
#        python program_asc_features.py <program name> <breakpoint> <run number> <output file>
# Outputs features in the following format:
#        [program name, breakpoint, run number, round, hamming, mips, logloss]
# Writes output as a line to outfile csv.
###

import sys
import csv

if len(sys.argv) < 5:
    print "not enough arguments"
    quit()
prog_name = sys.argv[1]
prog_bp = sys.argv[2]
prog_runsdone = sys.argv[3]
outfile = sys.argv[4]

def extract_asc_features(asc_string):
    data_start = asc_string.find("MIPS\n") + 5
    asc_string = asc_string[data_start:]
    data_lines = asc_string.split("\n")
    features = []
    for data_line in data_lines:
        data_list = data_line.split()
        if len(data_list) == 10:
            cur_round = data_list[0]
            hamming = data_list[4]
            mips = data_list[9]
            logloss = data_list[7]
            features.append([prog_name, prog_bp, prog_runsdone, cur_round, hamming, mips, logloss])
    return features
        
asc_string = sys.stdin.read()
features = extract_asc_features(asc_string)

# Write objdump breakpoints to outfile
with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in features:
        writer.writerow(row)

        
    
