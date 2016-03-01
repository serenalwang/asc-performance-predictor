###
# Extracts all breakpoints from an objdump file.
# Outputs all breakpoints which are between the target of a jump instruction and the jump instruction itself.
# Note: does NOT get breakpoints from "call".
# Usage: objdump -d <program binary> |
# python program_objdump_breakpoints.py <outfile>
# Writes output as a line to outfile csv.
###

import sys
import csv

if len(sys.argv) < 2:
    print "not enough arguments"
    quit()

jmp_instructions = {"jmp", "jmpq",  "je", "jne", "jl", "jg"}

prejmp_test = "40023e:	4c 89 e7             	mov    %r12,%rdi\n  400241:	e8 1b ff ff ff       	callq  400161 <step>\n  400246:	49 89 c4             	mov    %rax,%r12\n  400249:	49 83 fc 01          	cmp    $0x1,%r12\n  40024d:	77 ef                	"

# substring: a substring of objdump from the start of the jump target line
# to the jump instruction column itself. substring usually cuts off inside
# of a line.
# Returns a set of loop bps.
def extract_prejmp_bps(substring):
    loop_bps = set()
    bp_start = 0
    while bp_start != -1:
        if bp_start != 0:
            substring = substring[bp_start + 3:]
        bp_end = substring.find(":")
        if bp_end == -1:
            break
        bp = substring[:bp_end]
        loop_bps.add(bp)
        bp_start = substring.find("\n")
    return loop_bps

test_bps = extract_prejmp_bps(prejmp_test)
print test_bps

def extract_jmp_bps(objdump_string):
    jmp_bps = {}
    for jmp_inst in jmp_instructions:
        # Save a copy of objdump_string for the given jump instruction
        cur_objdump_string = objdump_string
        # Find all instances of jump instruction in objdump
        # Index into the overall objdump string
        global_index = 0
        jmp_start = objdump_string.find(jmp_inst)
        while jmp_start != -1:
            # Find target bp
            cur_objdump_string = cur_objdump_string[jmp_start:]
            global_index += jmp_start
            jmp_end = cur_objdump_string.find("\n")
            jmp_string = cur_objdump_string[:jmp_end]
            jmp_string_split = jmp_string.split()
            target_bp = jmp_string_split[1]

            # Find substring between target bp line and jump instruction
            target_bp_start = objdump_string.find(target_bp+":")
            target_bp_end = global_index

            # Find and add all bps between target and jump instruction bp
            loop_bps = extract_prejmp_bps(objdump_string
                                          [target_bp_start,target_bp_end])
            print loop_bps
            jmp_bps = jmp_bps.union(loop_bps)

            # Find next jump instruction
            cur_objdump_string = cur_objdump_string[jmp_end:]
            global_index += jmp_end
            jmp_start = cur_objdump_string.find(jmp_inst)
    return jmp_bps

objdump_string = sys.stdin.read()
bps = extract_jmp_bps(objdump_string)
# Add the program name to the first column
outline = bps
# Write objdump breakpoints to outfile
outfile = sys.argv[1]
with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(outline)