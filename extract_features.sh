#!/bin/bash

###
# Extracts all features from programs in SERENAPROGRAMSDIR
###

SERENAPROGRAMSDIR=asc-0.1.4/serena-programs-processed
# Number of serena programs to benchmark with ASC
NPROGRAMS=5

# Clear program text features from previous runs
echo "program_number,num_lines,num_words,num_chars" > program_text_features.csv

# Extract features for each program
for i in `seq 1 $NPROGRAMS`;
do
  python program_text_features.py $SERENAPROGRAMSDIR/$i.c
done
