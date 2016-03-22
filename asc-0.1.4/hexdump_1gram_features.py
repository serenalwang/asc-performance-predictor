###
# Extracts 1-gram features from a hexdump file.
# Usage: hexdump -d <program binary> | python hexdump_1gram_features.py <program name> <outfile>
# Writes output to outfile csv in the following format:
# [progname, ... (256 1gram features) ...]
###

from collections import Counter
import sys
import csv

if len(sys.argv) < 3:
    print "not enough arguments"
    quit()

hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

def get_ngrams(strg, n):
    counter = Counter()
    for i in xrange(len(strg) - n + 1):
        gram = strg[i:i+n]
        counter[gram] += 1
    return counter

hexdump_string = sys.stdin.read()
gram_counter = get_ngrams(hexdump_string, 1)

# Iterate through all possible 1 grams and record their counts.
outfeatures = []
for char1 in hex_chars:
    for char2 in hex_chars:
        gram = char1 + char2
        outfeatures.append(gram_counter[gram])

progname = sys.argv[1]
outfile = sys.argv[2]
with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([progname] + outfeatures)