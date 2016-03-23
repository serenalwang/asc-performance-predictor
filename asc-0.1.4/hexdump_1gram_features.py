###
# Extracts 1-gram features from a hexdump file.
# Usage: hexdump -C <program binary> > <program name>-dump.out; python hexdump_1gram_features.py <program name>-dump.out <program name> <outfile>
# Writes output to outfile csv in the following format:
# [progname, ... (256 1gram features) ...]
###

from collections import Counter
import sys
import csv

if len(sys.argv) < 4:
    print "not enough arguments"
    quit()

hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

def get_ngrams(hexdump_filename):
    hexdump_inf = open(hexdump_filename, "r")
    counter = Counter()
    for line in hexdump_inf:
        line_split = line.split()
        if len(line_split) > 3:
            # in full hexdump line
            for i in range(1, len(line_split)):
                gram = line_split[i]
                if gram[0] == "|":
                    break
                counter[gram] += 1
    return counter

hexdump_filename = sys.argv[1]
gram_counter = get_ngrams(hexdump_filename)

# Iterate through all possible 1 grams and record their counts.
outfeatures = []
for char1 in hex_chars:
    for char2 in hex_chars:
        gram = char1 + char2
        outfeatures.append(gram_counter[gram])
        
progname = sys.argv[2]
outfile = sys.argv[3]
with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([progname] + outfeatures)
