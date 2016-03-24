#!/bin/bash

###
# Gets all callgrind ir features from all programs. 
# Make sure to run this from within the directory containing the serenaprogram binaries.
# Assumes that serenaprogram binaries are already built.
# Also assumes that callgrind infiles already exist in the format <program name>-callgrind.out
# To generate callgrind infile:
# $ valgrind --tool=callgrind --dump-instr=yes ./<program name> <random seed>
# $ callgrind_annotate --auto=yes callgrind.out.pid > <program name>-callgrind.out
#
# USAGE: bash callgrind_ir_features.sh <program name>
###

program=$1

OUTFILE=callgrind_ir_features.csv

# clear outfile
# rm -f $OUTFILE

    objdump --dwarf=decodedline $program > $program-dwarf.out
    objdump -d $program > $program-objdump.out
    python callgrind_ir_features.py $program-callgrind.out $program-dwarf.out $program-objdump.out $program $OUTFILE
    rm $program-objdump.out
    rm $program-dwarf.out
