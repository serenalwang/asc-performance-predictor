#!/bin/bash 
# Make sure to run this from within the directory containing the asc binary.

# Build ASC
make mrproper
make

# Number of serena programs to benchmark with ASC
NPROGRAMS=4
for i in `seq 1 $NPROGRAMS`;
        do
                time ./asc -a 4001a2/16 $i.net $i
        done    
