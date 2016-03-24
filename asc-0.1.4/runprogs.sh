#!/bin/bash

###
# Runs all programs with all IPs. 
# Make sure to run this from within the directory containing the ASC binary.
#
# USAGE: bash runprogs.sh <number of inputs> <number of runs> 
###

NINPUTS=$1
NRUNS=$2
NPROGRAMS=7
SERENAPROGRAMS=$(seq 1 ${NPROGRAMS})

# Build ASC
#make mrproper
#make

for program in $SERENAPROGRAMS
do
    echo running program $program
    bash runprog.sh $program $NINPUTS $NRUNS
done 
