#!/bin/bash

# Clear program text features from previous runs
python program_text_features.py -c

# Directory containing the programs
SEARCHDIR= programs

# Extract features for each program
for program in "$SEARCHDIR"/*
do
  python program_text_features.py $program
done
