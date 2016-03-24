#!/bin/bash

###
# Gets all objdump features from all programs. 
# Make sure to run this from within the directory containing the serenaprogram binaries.
# Assumes that serenaprogram binaries are already built.
#
# USAGE: bash objdump_ip_features.sh 
###

NPROGRAMS=7
SERENAPROGRAMS=$(seq 1 ${NPROGRAMS})

OUTFILE=objdump_ip_features.csv

# clear outfile
rm -f $OUTFILE

for program in $SERENAPROGRAMS
do
  echo GETTING OBJDUMP FEATURES FOR PROGRAM $program
  objdump -d $program > $program-objdump.out | python objdump_ip_features.py  $program-objdump.out $program $OUTFILE
  rm $program-objdump.out
done 
