###
# Extracts all breakpoints from an objdump file.
# Usage: objdump -d <program binary> |
# python getallips.py <outfile>
# Writes output as a line to outfile csv.
###

import sys
import csv

if len(sys.argv) < 2:
    print "not enough arguments"
    quit()

#objdump_string = "\ncollatz_serena:     file format elf64-x86-64\n\n\nDisassembly of section .text:\n0000000000400144 <_start>:\n  400144:	48 31 ed             	xor    %rbp,%rbp\n  400147:	5f                   	pop    %rdi\n  400148:	48 89 e6             	mov    %rsp,%rsi\n  40014b:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp\n\n\n0000000000400161 <step>:\n  400161:	55                   	push   %rbp\n  400162:	48 89 e5             	mov    %rsp,%rbp\n"

# Extracts all ip values from an entire objdump output
def extract_all_ips(objdump_string):
    ips = set()
    start_str = "<_start>:"
    ip_divider_str = "\n  "
    # Initialize start of listed ips
    ip_start = objdump_string.find(start_str)
    assert(ip_start != -1)
    objdump_string = objdump_string[ip_start + len(start_str):]
    ip_start = 0
    while ip_start != -1:
        objdump_string = objdump_string[ip_start + len(ip_divider_str):]
        ip_end = objdump_string.find(":")
        if ip_end == -1:
            break
        ip = objdump_string[:ip_end]
        ips.add(ip)
        ip_start = objdump_string.find(ip_divider_str)
    return ips

objdump_string = sys.stdin.read()
bps = extract_all_ips(objdump_string)
print bps
# Add the program name to the first column
outline = bps
# Write objdump breakpoints to outfile
outfile = sys.argv[1]
with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(outline)