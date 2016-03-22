###
# Extracts all features of individual breakpoints from an objdump file.
# Usage: objdump -d <program binary> | python objdump_ip_features.py <outfile>
# Writes output to outfile csv in the following format:
# [ip, jmp, call, mov, lea, cmp, inc, mul, add, or, push,
#  is target of jmp, distance from target of jmp]
###
from collections import OrderedDict
import sys
import csv

if len(sys.argv) < 2:
    print "not enough arguments"
    quit()

jmp_insts = {"jmp", "jmpq",  "je", "jne", "jl", "jg", "jbe", "jb", "ja"}
call_insts = {"callq"}
mov_insts = {"mov", "movl", "movsbq", "movsbl"}
lea_insts = {"lea"}
cmp_insts = {"cmp", "cmpl", "test"}
inc_insts = {"inc"}
mul_insts = {"imul", "div"}
add_insts = {"sub", "subl", "add", "addl"}
push_insts = {"push","pop"}
or_insts = {"or", "xor", "and"}
ret_insts = {"retq"}

insts = [jmp_insts, call_insts, mov_insts, lea_insts, cmp_insts, inc_insts, mul_insts, add_insts, or_insts, push_insts]
    
#objdump_string = "\ncollatz_serena:     file format elf64-x86-64\n\n\nDisassembly of section .text:\n0000000000400144 <_start>:\n  400144:	48 31 ed             	xor    %rbp,%rbp\n  400147:	5f                   	pop    %rdi\n  400148:	48 89 e6             	mov    %rsp,%rsi\n  40014b:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp\n\n\n0000000000400161 <step>:\n  400161:	55                   	push   %rbp\n  400162:	48 89 e5             	mov    %rsp,%rbp\n  40023e:	4c 89 e7             	mov    %r12,%rdi\n  400241:	e8 1b ff ff ff       	callq  400161 <step>\n  400246:	49 89 c4             	mov    %rax,%r12\n  400249:	49 83 fc 01          	cmp    $0x1,%r12\n  40024d:	77 ef                	ja     40023e <main+0x9c>\n"

# Extracts all ip values from an entire objdump output. 
def extract_all_ips(objdump_string):
    # ips is a dictionary with key: ip, value: [list of features]
    ips = OrderedDict()
    jmp_targets = set()
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
        line_end = objdump_string.find("\n")
        if ip_end == -1:
            break
        ip = objdump_string[:ip_end]
        ip_string = objdump_string[:line_end]
        ip_string_split = ip_string.split("\t")
        inst_string = ip_string_split[2]
        inst_string_split = inst_string.split()
        inst = inst_string_split[0]

        # Check for target of jmp instruction
        if inst in jmp_insts:
            jmp_target = inst_string_split[1]
            jmp_targets.add(jmp_target)
        
        # Match instruction with feature index
        ip_features = []
        for inst_set in insts:
            if inst in inst_set:
                ip_features.append(1)
            else:
                ip_features.append(0)
        ips[ip] = ip_features
        # Advance to the next ip_start
        ip_start = objdump_string.find(ip_divider_str)
    return ips, jmp_targets

objdump_string = sys.stdin.read()
ips_dict, jmp_target_set = extract_all_ips(objdump_string)
#print ips_dict
#print jmp_target_set

def add_jmp_features(ips, jmp_targets):
    ips_with_jmp_features = {}
    # Add jmp target features
    i = 0
    # Index of last target of jmp instruction
    last_jmp_target = 0
    for ip, features in ips.items():
        if ip in jmp_targets:
            ips_with_jmp_features[ip] = features + [1,1]
            last_jmp_target = i
        else:
            if last_jmp_target > 0:
                ips_with_jmp_features[ip] = features + [0, i - last_jmp_target + 1]
            else:
                ips_with_jmp_features[ip] = features + [0, 0]
        i += 1
    return ips_with_jmp_features

all_features_dict = add_jmp_features(ips_dict, jmp_target_set)
#print all_features_dict

# Write objdump breakpoints to outfile
outfile = sys.argv[1]
with open(outfile, 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for ip, features in all_features_dict.items():
       writer.writerow([ip] + features)
