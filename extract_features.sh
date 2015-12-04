#!/bin/bash

###
# Extracts all features from programs in SERENAPROGRAMSDIR
###

SERENAPROGRAMSDIR=asc-0.1.4/kernels

# Clear program text features from previous runs
echo "program_number,num_lines,num_words,num_chars" > program_text_features.csv
# Clear program gprof features from previous runs
echo "program_number,num_functions,num_function_calls,total_time,highest_percent_time,highest_percent_calls,var_function_times,var_function_calls,max_num_parents,max_num_children,num_recursive_calls" > program_gprof_features.csv

# Clear program callgrind features from previous runs
echo "program_number,Ir,Dr,I1mr,d1mr,D1mw,ILmr,DLmr,DLmw,I1missrate,D1missread,D1misswrite,LLmissrate" > program_callgrind_features.csv

# Extract features for each program
KERNELS=(collatz factor 3sum warshall)

declare -A kernel_arg_map
kernel_arg_map["collatz"]="100000"
kernel_arg_map["warshall"]="1 1500"
kernel_arg_map["factor"]="9000037038035596873"
kernel_arg_map["loop"]="9223372000000000000 100000000000"
kernel_arg_map["3sum"]="$RANDOM 5000 1750000000"

for kernel in "${KERNELS[@]}";
do
    echo extracting features for $kernel
    # Extract text features  
    python program_text_features.py $SERENAPROGRAMSDIR/$kernel.c

    echo extracting gprof features
    # Extract gprof features
    args="${kernel_arg_map[${kernel}]}"
    gcc -pg $SERENAPROGRAMSDIR/$kernel.c -o $kernel
    echo running $kernel $args
    ./$kernel $args
    gprof $kernel gmon.out -b | python program_gprof_features.py $kernel
    rm -f gmon.out

    echo extracting callgrind features
    # Extract callgrind features
    valgrind --tool=callgrind --simulate-cache=yes ./$kernel $args 3>&2 2>&1 1>&3 | python program_callgrind_features.py $kernel
    rm -f callgrind.out*
    
    # Clean up unnecessary files
    rm -f $kernel
    
done
