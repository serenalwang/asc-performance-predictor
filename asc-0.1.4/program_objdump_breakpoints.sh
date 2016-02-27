#!/bin/bash

###
# Extracts all IPs from objdump of a single program.
# Must already be compiled: program binary
#
# USAGE: getprogips.sh <program name>
###

PROGNAME=$1

# Clear breakpoints file
OUTFILE=$PROGNAME-ips.csv

objdump -d $PROGNAME | python program_objdump_breakpoints.py $PROGNAME $OUTFILE
