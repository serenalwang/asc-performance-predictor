#!/bin/bash

###
# Extracts all asc features from current kernels
###

#make mrproper
#make

# Clear asc features file
OUTFILE=program_asc_features.csv
echo "program_name,breakpoint,round,hamming,mips,logloss" > $OUTFILE

# Collect breakpoints for all current kernels
declare -A kernel_arg_map
kernel_arg_map["collatz"]="100000"
kernel_arg_map["warshall"]="1 1500"
kernel_arg_map["factor"]="9000037038035596873"
kernel_arg_map["loop"]="9223372000000000000 100000000000"
kernel_arg_map["3sum"]="$RANDOM 5000 1750000000"

BPFILE=program_objdump_breakpoints.csv
# Read all lines from input file
while IFS='' read -r line || [[ -n "$line" ]];
do    
    # Split line by commas
    IFS=',' read -r -a bp_data <<< "$line"
    kernel="${bp_data[0]}"
    echo kernel $kernel
    args="${kernel_arg_map[${kernel}]}"
    echo args $args
    # Read each breakpoint 
    for index in "${!bp_data[@]}";
    do
	if [ $index -ne "0" ];
	then
	    breakpoint="${bp_data[${index}]}"
	    echo breakpoint $breakpoint
	    ./asc -a $breakpoint -n 1000 $kernel $args | python program_asc_features.py $kernel $breakpoint
	fi
    done
done < $BPFILE
