#!/bin/bash

###
# Runs one program with all IPs.
# Make sure to run this from within the directory containing the ASC binary.
# Must already be compiled: ASC, program binary
#
# USAGE: bash runprog.sh <program name> <number of runs> 
###

PROGNAME=$1
NRUNS=$2
BPFILE=$PROGNAME-ips.csv

# Get all IPs from objdump
objdump -d $PROGNAME | python getallips.py $BPFILE

# Read all lines from BPFILE
IFS='' read -r line < $BPFILE
# Split line by commas
IFS=',' read -r -a bp_data <<< "$line"
echo Found IPs for program $PROGNAME
# Read each breakpoint 
for index in "${!bp_data[@]}";
do
    IP="${bp_data[${index}]}"
    # Remove trailing character if there is one
    IP="${IP/$'\r'/}"
    echo Running breakpoint $IP
    bash runprogip.sh $PROGNAME $IP $NRUNS
done

