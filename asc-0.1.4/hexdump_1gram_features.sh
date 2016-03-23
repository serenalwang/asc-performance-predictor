#!/bin/bash

###
# Gets all hexdump features from all programs. 
# Make sure to run this from within the directory containing the serenaprogram binaries.
# Assumes that serenaprogram binaries are already built.
#
# USAGE: bash hexdump_1gram_features.sh 
###

SERENAPROGRAMS=(collatz_serena random)

OUTFILE=hexdump_1gram_features.csv

# clear outfile
rm -f $OUTFILE

for program in $SERENAPROGRAMS
do
  hexdump -d $program | python hexdump_1gram_features.py program $OUTFILE 
done 
