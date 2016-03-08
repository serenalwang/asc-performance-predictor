#!/bin/bash 

###
# Runs a single program and IP value with ASC and saves the output to a file.
# Make sure to run this from within the directory containing the ASC binary.
# Must already be compiled: ASC, program binary
# Saves output to ascfeatures/[progname]-[ip]-asc.csv
#
# USAGE: bash runprogip.sh <program binary> <IP value> <number of inputs>
#        <number of runs per input> 
###

# Number of serena programs to benchmark with ASC
PROGNAME=$1
IP=$2
# Number of unique inputs to run
NINPUTS=$3
# Number of times to run with one input
NRUNS=$4
# Seed the bash random number generator with the current process id
RANDOM=$$
# Max number of rounds per run
MAXROUNDS="50"
OUTDIR=ascfeatures
# Store results in output csv file
OUTFILE=$PROGNAME-$IP-asc.csv

mkdir -p $OUTDIR
# Clear output file
rm -f $OUTDIR/$OUTFILE
# Clear previous .net file
rm -f $PROGNAME.net

echo RUNNING $PROGNAME FOR IP $IP
# Local variable - number of runs that have already been completed
INPUTSDONE="0"
while [ $INPUTSDONE -lt $NINPUTS ];
do
    INPUTSDONE=$[$INPUTSDONE+1]
    echo starting input $INPUTSDONE
    INPUT=$RANDOM
    echo random input $INPUT
    RUNSDONE="0"
    while [ $RUNSDONE -lt $NRUNS ];
    do
        RUNSDONE=$[$RUNSDONE+1]
	echo starting run $RUNSDONE for input $INPUT
	./asc -a $IP -n $MAXROUNDS $PROGNAME.net $PROGNAME $INPUT | python program_asc_features.py $PROGNAME $IP $INPUT $RUNSDONE $OUTDIR/$OUTFILE
    done
    echo $INPUTSDONE inputs completed
done 
