###
# Extracts all breakpoints from an objdump file.
# Outputs all breakpoints which are the target of a jump instruction.
# Usage: objdump -d <program binary> |
# python program_objdump_breakpoints.py <program name>
# Writes output as a line to outfile csv.
###

import sys
import csv

jmp_instructions = {"jmp", "jmpq",  "je", "jne", "jl", "jg"}

def extract_jmp_bps(objdump_string):
    jmp_bps = []
    for jmp_inst in jmp_instructions:
        jmp_start = objdump_string.find(jmp_inst)
        while jmp_start != -1:
            objdump_string = objdump_string[jmp_start:]
            jmp_end = objdump_string.find("\n")
            jmp_string = objdump_string[:jmp_end]
            jmp_string_split = jmp_string.split()
            jmp_bp = jmp_string_split[1]
            jmp_bps.append(jmp_bp)
            objdump_string = objdump_string[jmp_end:]
            jmp_start = objdump_string.find(jmp_inst)
    return jmp_bps

objdump_string = sys.stdin.read()
bps = extract_jmp_bps(objdump_string)
# Add the program name to the first column
features = [sys.argv[1]] + features
# Write objdump breakpoints to outfile
outfile = "program_object_breakpoints.csv"
with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(features)

        
    
