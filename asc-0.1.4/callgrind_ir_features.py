###
# Extracts ir features from a callgrind file.
# Usage: python callgrind_ir_features.py <callgrind infile> <objdump dwarf infile> <objdump assembly file> <program name> <outfile>
# To generate callgrind infile: valgrind --tool=callgrind --dump-instr=yes <program name> <random seed>
# To generate objdump dwarf infile: objdump --dwarf=decodedline <program name>
# Writes output to outfile csv in the following format:
# [progname, ip, ir count, ir %]
###

from collections import OrderedDict
import sys
import csv

if len(sys.argv) < 6:
    print "not enough arguments"
    quit()

# Maps lines and functions to ir counts.
# Returns two dictionaries:
# 1. key: line num, value: ir
# 2. key: function name, value: ir
def callgrind_ir_dicts(callgrind_filename):
    callgrind_inf = open(callgrind_filename, 'r')
    total_ir = 0
    function_dict = {}
    line_num_dict = {}
    passed_program_totals = False
    started_functions = False
    passed_functions = False
    started_lines = False
    passed_lines = False
    line_num = 0
    for line in callgrind_inf:
        line_split = line.split()
        # First get program totals
        if not passed_program_totals and len(line_split) == 3 and line_split[1] == "PROGRAM":
            total_ir = int(line_split[0].replace(',', ''))
            passed_program_totals = True
        # function lines
        elif passed_program_totals and not passed_functions:
            if len(line_split) == 3:
                started_functions = True
                function_name_start = line_split[1].find(":") + 1
                function_name = line_split[1][function_name_start:]
                function_ir = int(line_split[0].replace(',', ''))
                function_dict[function_name] = function_ir
            elif started_functions:
                    passed_functions = True
        elif passed_program_totals and passed_functions and not passed_lines:
            if not started_lines:
                if len(line_split) == 4 and line_split[1] == "line":
                    # Get start line
                    line_num = int(line_split[2])
                    started_lines = True
            else:
                if len(line_split) == 0 or line_split[0] == "--":
                    passed_lines = True
                    continue
                else:
                    # yay we've started lines!
                    # Skip arrows
                    if len(line_split) >= 3 and line_split[1] == "=>":
                        continue
                    ir = line_split[0]
                    line_num_dict[line_num] = (0 if ir == "." else int(ir.replace(',', '')))
                    line_num += 1
    return line_num_dict, function_dict, total_ir

# Returns map: key: ip value, value: line num
def line_nums_to_ips(objdump_dwarf_filename):
    ip_to_line = OrderedDict()
    dwarf_inf = open(objdump_dwarf_filename, 'r')
    started_crt0 = False
    passed_crt0 = False
    for line in dwarf_inf:
        line_split = line.split()
        if not passed_crt0:
            if len(line_split) == 3 and line_split[0] == "crt0.s":
                started_crt0 = True
            elif started_crt0 and len(line_split) == 0:
                passed_crt0 = True
        elif passed_crt0:
            if len(line_split) == 3:
                line_num = line_split[1]
                ip = line_split[2][2:]
                ip_to_line[ip] = line_num
    return ip_to_line

# Returns two maps:
# 1. key: line num, value: list of ip values
# 2. key: func name, value: list of ip values
def objdump_ip_dicts(ip_to_line, objdump_filename):
    objdump_inf = open(objdump_filename, 'r')
    line_num_to_ips = {}
    func_name_to_ips = {}
    cur_func_name = ""
    next_ip_index = 0
    ip_to_line_items = ip_to_line.items()
    next_ip, next_line_num = ip_to_line_items[next_ip_index]
    for line in objdump_inf:
        line_split = line.split()
        # Function call line
        if len(line_split) == 2 and line_split[1].find(">:") != -1:
            cur_func_name = line_split[1][1:line_split[1].find(">:")]
        else:
            # We know we're in an instruction line
            if cur_func_name != "" and len(line_split) > 0:
                ip_end = line_split[0].find(":")
                assert(ip_end != -1)
                ip = line_split[0][:ip_end]

                # Add ip to function dict
                if cur_func_name in func_name_to_ips:
                    func_name_to_ips[cur_func_name].append(ip)
                else:
                    func_name_to_ips[cur_func_name] = [ip]

                # add ip to line nums
                # Find closest line_num, but not if we've already iterated to the last element of the dwarf list.
                # Iterate next_ip just past ip
                while next_ip_index < len(ip_to_line_items) and int(ip, 16) >= int(next_ip, 16):
                    next_ip, next_line_num = ip_to_line_items[next_ip_index]
                    next_ip_index += 1
                    
                # If ip is within the range of the dictionary
                if next_ip_index > 0 and next_ip_index < len(ip_to_line_items):
                    cur_ip, cur_line_num = ip_to_line_items[next_ip_index - 2]
                    # Add ip to line_num    
                    if cur_line_num in line_num_to_ips:
                        line_num_to_ips[cur_line_num].append(ip)
                    else:
                        line_num_to_ips[cur_line_num] = [ip]
    return line_num_to_ips, func_name_to_ips

# Returns a mapping from ip to ir
# key: ip, value: ir
def ip_to_ir(line_num_to_ir, function_to_ir, line_num_to_ips, func_name_to_ips):
    ip_to_ir = {}
    # First map all function irs
    for function_name, ir in function_to_ir.items():
        if function_name in func_name_to_ips:
            ips = func_name_to_ips[function_name]
            for ip in ips:
                ip_to_ir[ip] = ir
    # Overwrite function irs with line_num irs
    for line_num, ir in line_num_to_ir.items():
        if str(line_num) in line_num_to_ips:
            ips = line_num_to_ips[str(line_num)]
            for ip in ips:
                ip_to_ir[ip] = ir
    return ip_to_ir
    
callgrind_filename = sys.argv[1]
line_num_dict, function_dict, total_ir = callgrind_ir_dicts(callgrind_filename)

objdump_dwarf_filename = sys.argv[2]
ip_to_line = line_nums_to_ips(objdump_dwarf_filename)

objdump_filename = sys.argv[3]
line_num_to_ips, func_name_to_ips = objdump_ip_dicts(ip_to_line, objdump_filename)

ip_to_ir_dict = ip_to_ir(line_num_dict, function_dict, line_num_to_ips, func_name_to_ips)

progname = sys.argv[4]
outfile = sys.argv[5]

with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for ip, ir in ip_to_ir_dict.items():
        ir_percent = round(float(ir)/float(total_ir) * 100.,2)
        writer.writerow([progname, ip, ir, ir_percent])
