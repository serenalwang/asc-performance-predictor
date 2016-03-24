#!/bin/bash

###
# Gets all hexdump features from all programs. 
# Make sure to run this from within the directory containing the serenaprogram binaries.
# Assumes that serenaprogram binaries are already built.
#
# USAGE: bash hexdump_1gram_features.sh 
###

NPROGRAMS=7
SERENAPROGRAMS=$(seq 1 ${NPROGRAMS})

OUTFILE=hexdump_1gram_features.csv

# clear outfile
rm -f $OUTFILE

for program in $SERENAPROGRAMS
do
    hexdump -C $program > $program-hexdump.out; python hexdump_1gram_features.py $program-hexdump.out $program $OUTFILE
    rm $program-hexdump.out
done 
