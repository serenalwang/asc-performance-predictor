#!/bin/bash

###
# Extracts all features from programs in SERENAPROGRAMSDIR
###

#make mrproper
#make

# Clear breakpoints file
OUTFILE=program_objdump_breakpoints.csv
echo "program_name, kernels" > $OUTFILE

# Collect breakpoints for all current kernels
KERNELS=(loop collatz factor 3sum warshall)
for kernel in "${KERNELS[@]}";
do
    objdump -d $kernel | python program_objdump_breakpoints.py $kernel
done 
