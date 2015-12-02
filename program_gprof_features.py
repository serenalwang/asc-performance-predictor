###
# Extracts features from grof output.
# Outputs a list of features of the following format:
# [Num functions, num function calls, total program time,
#  highest % function time, highest % function calls,
#  variance of function time,  variance of num function calls,
#  max num parents for a function, max num children for a function,
#  num recursive calls]
# Returns a list of all  0s if gprof doesn't produce any output.
# Writes output as a line to outfile csv.
###

import numpy as np
import sys
import csv

if len(sys.argv) < 2:
    print "No arguments passed in."
    print "USAGE: gprof <program number> gmon.out -b | program_gprof_features.py <program number>"
    exit()

# Returns a list of features from the Flat profile.
# flatprofile_string should contain only the line starting after name,
# until the last function data line (without a newline at the end) 
def extract_flatprofile_features(flatprofile_string):
    data_lines = flatprofile_string.split("\n")
    num_functions = len(data_lines)
    function_times = []
    function_calls = []
    highest_percent_time = 0.0
    for data_line in data_lines:
        data = data_line.split()
        current_percent_time = float(data[0])
        if current_percent_time > highest_percent_time:
            highest_percent_time = current_percent_time
        function_times.append(float(data[2]))
        if data[3] != "main":
            function_calls.append(int(data[3]))

    total_time = np.sum(function_times)
    num_function_calls = np.sum(function_calls)
    var_function_calls = np.var(function_calls)
    var_function_times = np.var(function_times)
    highest_percent_calls = 0.0
    for calls in function_calls:
        current_percent_calls = float(calls)/float(num_function_calls) * 100
        if current_percent_calls > highest_percent_calls:
            highest_percent_calls = current_percent_calls
    return [num_functions, num_function_calls, total_time,
                highest_percent_time, highest_percent_calls,
                var_function_times, var_function_calls]

# Returns a list of features from the call graph.
# callgraph_string should contain only the line containing the first [1]
# until the last ----- line. 
def extract_callgraph_features(callgraph_string):
    num_recursive_calls = 0
    max_num_parents = 0
    max_num_children = 0
    func_sep = "-----------------------------------------------"
    callgraph_funcs = callgraph_string.split(func_sep)
    for func in callgraph_funcs:
        func = func.strip()
        func_lines = func.split('\n')
        num_func_lines = len(func_lines)
        for i in range(num_func_lines):
            data = func_lines[i].split()
            if len(data) < 1:
                continue
            # Primary line
            if data[0][0] == '[':
                called = data[4].split("+")
                if len(called) == 2:
                    num_recursive_calls += int(called[1])
                cur_num_parents = i
                cur_num_children = num_func_lines - (i + 1)
                if cur_num_parents > max_num_parents:
                    max_num_parents = cur_num_parents
                if cur_num_children > max_num_children:
                    max_num_children = cur_num_children
    return [max_num_parents, max_num_children, num_recursive_calls]

# Extracts all features from gprof output.
# Full string is a string containing the full text of the grof output.
def extract_all_features(full_string):
    # Flat profile
    flatprofile_start = full_string.find("name")
    full_string = full_string[flatprofile_start:]
    flatprofile_start = full_string.find("\n")
    flatprofile_start += 1
    full_string = full_string[flatprofile_start:]
    flatprofile_end = full_string.find("")
    if flatprofile_end == -1:
        print "No flatprofile or callgraph."
        return [0 for i in range(10)]
    flatprofile_string = full_string[:flatprofile_end]
    flatprofile_string = flatprofile_string.strip()
    flatprofile_features = extract_flatprofile_features(flatprofile_string)

    # Call graph
    full_string = full_string[flatprofile_end:]
    callgraph_start = full_string.find("name\n") + 5
    full_string = full_string[callgraph_start:]
    callgraph_end = full_string.find("")
    callgraph_string = full_string[:callgraph_end]
    callgraph_string = callgraph_string.strip()
    callgraph_features = extract_callgraph_features(callgraph_string)

    return flatprofile_features + callgraph_features

gprof_string = sys.stdin.read()
features = extract_all_features(gprof_string)
# Add the program name to the first column
features = [sys.argv[1]] + features
# Write gprof features to outfile
outfile = "program_gprof_features.csv"
with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(features)
