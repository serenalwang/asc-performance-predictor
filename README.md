To extract all ASC scaling results for c programs:
1. Place all c programs in serena-programs-raw.
   Make sure these programs are named i.c, where i is an integer, and i starts
   at 1, and goes up by 1 for every new program.
   Make sure that the number of programs in serena-programs-raw is the same as
   the variable NPROGRAMS in Makefile, runserenaprograms.sh,
   and process_programs.sh.
2. To process these programs for running with ASC, run
	$ bash process_programs.sh
3. To run ASC on all processed programs, in the asc-0.1.4 directory, run
      	$ bash runserenaprograms.sh

