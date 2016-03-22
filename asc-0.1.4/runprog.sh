#!/bin/bash

###
# Runs one program with all IPs.
# Make sure to run this from within the directory containing the ASC binary.
# Must already be compiled: ASC, program binary
#
# USAGE: bash runprog.sh <program name> <number of inputs> <number of runs per input> 
###

PROGNAME=$1
NINPUTS=$2
NRUNS=$3
BPFILE=$PROGNAME-ips.csv

# Get all IPs from objdump
objdump -d $PROGNAME | python getallips.py $BPFILE

# Read all lines from BPFILE
echo Getting IPs for program $PROGNAME
while IFS='' read -r line || [[ -n "$line" ]];
do
    # Split line by commas
    IFS=',' read -r -a bp_data <<< "$line"
    # Read each breakpoint 
    for index in "${!bp_data[@]}";
    do
	IP="${bp_data[${index}]}"
	# Remove trailing character if there is one
	IP="${IP/$'\r'/}"
	echo Running breakpoint $IP
	bash runprogip.sh $PROGNAME $IP $NINPUTS $NRUNS
    done
done < $BPFILE

