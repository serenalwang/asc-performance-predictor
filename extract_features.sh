#!/bin/bash

###
# Extracts all features from programs in SERENAPROGRAMSDIR
###

SERENAPROGRAMSDIR=asc-0.1.4/serena-programs-processed
# Number of serena programs to benchmark with ASC
NPROGRAMS=5

# Clear program text features from previous runs
echo "program_number,num_lines,num_words,num_chars" > program_text_features.csv
# Clear program gprof features from previous runs
echo "program_number,num_functions,num_function_calls,total_time,highest_percent_time,highest_percent_calls,var_function_times,var_function_calls,max_num_parents,max_num_children,num_recursive_calls" > program_gprof_features.csv

# Clear program callgrind features from previous runs
echo "program_number,Ir,Dr,I1mr,d1mr,D1mw,ILmr,DLmr,DLmw,I1missrate,D1missread,D1misswrite,LLmissrate" > program_callgrind_features.csv

# Extract features for each program
for i in `seq 1 $NPROGRAMS`;
do
    # Extract text features  
    python program_text_features.py $SERENAPROGRAMSDIR/$i.c
    
    # Extract gprof features
    gcc -pg $SERENAPROGRAMSDIR/$i.c -o $i
    ./$i
    gprof $i gmon.out -b | python program_gprof_features.py $i
    rm -f gmon.out
    
    # Extract callgrind features
    valgrind --tool=callgrind --simulate-cache=yes ./$i 3>&2 2>&1 1>&3 | python program_callgrind_features.py $i
    rm -f callgrind.out*
    
    # Clean up unnecessary files
    rm -f $i
    
done
