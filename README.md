This repository contains code for extracting features from ASC
for performance prediction.  

In addition to asc-0.1.4, this repository contains the following directories and modifications added by Serena for feature extraction:

asc-0.1.4/serena-programs-randomized: This directory contains the programs that are "ready" to be run directly with ASC for feature extraction. Each program takes only a random seed as input, and the program's behavior varies randomly according to this random seed. 

asc-0.1.4/serena-programs-raw: This directory contains a set of C programs that were scraped from the recesses of the internet. I have verified that they all compile and work and aren't malware, and overall they're fairly simple. Running these over and over with the same input with ASC isn't really interesting because ASC can eventually learn the execution paths if they're identical for every run. I only chose a few of these to randomize for my thesis. 

To extract all ASC cross entropy loss values for C programs (target values):
1. Place all C programs in asc-0.1.4/serena-programs-randomized. Make sure the programs fit the specification that they only take one command line argument, and that command line argument is a random seed.
2. Compile ASC and the programs by running make in the asc-0.1.4 directory.
3. To run a single program with a single IP value with ASC and extract all cross entropy loss values (along with some other features):  
	$ bash runprogip.sh <program binary> <IP value> <number of inputs> <number of runs per input> 
4. To run a single program with all IP values of that program (the script takes care of extracting those IP values): 
	$ bash runprog.sh <program name> <number of inputs>  <number of runs per input> 
5. To run all programs with all IP values of each program: 
	$ bash runprogs.sh <number of inputs> <number of runs>
	
	edit
	

