###
# Extracts features from callgrind output.
# Outputs a list of features of the following format:
# [Ir, Dr, I1mr, d1mr, D1mw, ILmr, DLmr, DLmw, I1missrate, D1missread, D1misswrite, LLmissrate]
# The interpretation of these features can be found here:
# http://web.stanford.edu/class/cs107/guide_callgrind.html
# Writes output as a line to outfile csv.
###
import sys
import csv

# collected_string should be the line beginning with "Collected" and
# ending right before the newline.
def extract_raw_features(collected_string):
    data_start = collected_string.find(":") + 1
    data_string = collected_string[data_start:]
    data = data_string.split()
    data = [float(i) for i in data]
    return data

def extract_all_features(full_string):
    collected_start = full_string.find("Collected")
    collected_string = full_string[collected_start:]
    collected_end = collected_string.find("\n")
    collected_string = collected_string[:collected_end]
    features = extract_raw_features(collected_string)
    I1missrate = features[3]/features[0]
    D1missread = features[1]/features[4]
    D1misswrite = features[2]/features[5]
    LLmissrate = (features[3] + features[4] + features[5]) / (features[6] + features[7] + features[8])
    features += [I1missrate, D1missread, D1misswrite, LLmissrate]
    return features

callgrind_string = sys.stdin.read()
features = extract_all_features(callgrind_string)
# Add the program name to the first column
features = [sys.argv[1]] + features
# Write callgrind features to outfile
outfile = "program_callgrind_features.csv"
with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(features)
