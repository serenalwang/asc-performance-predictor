#!/bin/bash

###
# Processes all programs in IN_DIRECTORY and places modified, asc-runnable
# programs in OUT_DIRECTORY
# Make sure script is in the same directory as asc-0.1.4.
###

IN_DIRECTORY=asc-0.1.4/serena-programs-raw
OUT_DIRECTORY=asc-0.1.4/serena-programs-processed

# Number of serena programs to benchmark with ASC
NPROGRAMS=150

# Process each program
for i in `seq 1 $NPROGRAMS`;
do
  python process_programs.py $IN_DIRECTORY/$i.c $OUT_DIRECTORY/$i.c
done
