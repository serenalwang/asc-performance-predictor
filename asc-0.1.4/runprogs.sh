#!/bin/bash

###
# Runs all programs with all IPs. 
# Make sure to run this from within the directory containing the ASC binary.
# Assumes that all IPs are already written in BPFILE
#
# USAGE: bash runprogs.sh <number of runs> 
###

NRUNS=$1
SERENAPROGRAMS=(collatz_serena random)

# Build ASC
make mrproper
make

for program in $SERENAPROGRAMS
do
    bash runprog.sh $program $NRUNS
done 
