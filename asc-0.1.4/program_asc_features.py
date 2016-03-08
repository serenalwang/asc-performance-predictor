###
# Extracts all asc features from asc output for a given program
# and breakpoint.
# Usage: ./asc -a <breakpoint> <program binary> <input args> |
#        python program_asc_features.py <program name> <IP> <input args> <run number> <output file>
# Outputs features in the following format:
#        [program name, breakpoint, input parameter, run number, total rounds,
#         current round, hamming, mips, logloss]
# Writes output as a line to outfile csv.
###

import sys
import csv

if len(sys.argv) < 5:
    print "not enough arguments"
    quit()
prog_name = sys.argv[1]
prog_bp = sys.argv[2]
prog_input = sys.argv[3]
prog_runsdone = sys.argv[4]
outfile = sys.argv[5]
# minimum number of ASC output lines that will be written to a file. 
min_rounds = 5

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
            features.append([prog_name, prog_bp, prog_input, prog_runsdone, cur_round, hamming, mips, logloss])
    return features
        
asc_string = sys.stdin.read()
features = extract_asc_features(asc_string)
nrounds = len(features)

if nrounds > min_rounds:
    # Write objdump breakpoints to outfile
    with open(outfile, 'ab') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in features:
            row.insert(4,nrounds)
            writer.writerow(row)
            
