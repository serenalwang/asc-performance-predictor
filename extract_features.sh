#!/bin/bash 
python program_text_features.py -c

search_dir = programs

for program in "$search_dir"/*
do
  python program_text_features.py $program
done