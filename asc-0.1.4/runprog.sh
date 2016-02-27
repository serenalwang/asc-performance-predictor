#!/bin/bash

###
# Runs one program with all IPs.
# Make sure to run this from within the directory containing the ASC binary.
# Assumes that all IPs are already written in BPFILE
# Must already be compiled: ASC, program binary
#
# USAGE: bash runprog.sh <program name> <number of runs> 
###

PROGNAME=$1
NRUNS=$2
BPFILE=$PROGNAME-ips.csv
# Read all lines from input file
while IFS='' read -r line || [[ -n "$line" ]];
do    
    # Split line by commas
    IFS=',' read -r -a bp_data <<< "$line"
    echo Found IPs for program $PROGNAME
    # Read each breakpoint 
    for index in "${!bp_data[@]}";
    do
	IP="${bp_data[${index}]}"
        echo Running breakpoint $IP
        bash runprogip.sh $PROGNAME $IP $NRUNS
    done
done < $BPFILE
