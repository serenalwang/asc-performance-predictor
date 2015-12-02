#!/bin/bash 
# Make sure to run this from within the directory containing the asc binary.

# Build ASC
make mrproper
make

# Number of serena programs to benchmark with ASC
NPROGRAMS=150
# Max number of cores to run ASC with
NCORES=1
# Store results in output csv file
OUTFILE='asctimes.csv'

# Clear output file
echo "program_number,num_cores,asc_time,real_time" > $OUTFILE

exec 3>&1 4>&2
for ncores in `seq 1 $NCORES`;
do
    
for i in `seq 1 $NPROGRAMS`;
do
    echo RUNNING $i
    asc_time=$( { time ./asc -j $ncores $i 1>&3 2>&4; } 2>&1 | sed '/real */!d;s/real//g')
    real_time=$( { time ./$i 1>&3 2>&4; } 2>&1 | sed '/real */!d;s/real//g')
    out_line=$i,$ncores,$asc_time,$real_time
    echo $out_line >> $OUTFILE
done
done
exec 3>&- 4>&-
