#!/bin/bash 

###
# Runs a single program and IP value with ASC and saves the output to a file.
# Make sure to run this from within the directory containing the ASC binary.
# Must already be compiled: ASC, program binary
# Saves output to ascfeatures/[progname]-[ip]-asc.csv
#
# USAGE: bash runprogram.sh <program binary> <IP value> <number of runs> 
###

# Number of serena programs to benchmark with ASC
PROGNAME=$1
IP=$2
NRUNS=$3
# Seed the bash random number generator with the current process id
RANDOM=$$
# Max number of rounds per run
MAXROUNDS="50"
OUTDIR=ascfeatures
# Store results in output csv file
OUTFILE=$PROGNAME-$IP-asc.csv

# Clear output file
mkdir -p $OUTDIR
echo "prog_name,IP,runsdone,round,hamming,mips,error" > $OUTDIR/$OUTFILE

echo RUNNING $PROGNAME
# Local variable - number of runs that have already been completed
RUNSDONE="0"
while [ $RUNSDONE -lt $NRUNS ];
do
    RUNSDONE=$[$RUNSDONE+1]
    echo starting run $RUNSDONE
    echo random seed $RANDOM
    ./asc -a $IP -n $MAXROUNDS $PROGNAME $RANDOM | python program_asc_features.py $PROGNAME $IP $RUNSDONE $OUTDIR/$OUTFILE
    echo $RUNSDONE runs completed
done 
