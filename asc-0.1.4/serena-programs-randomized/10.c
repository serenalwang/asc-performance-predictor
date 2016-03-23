/* A simple loop kernel.  */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	/* Serena's seed  */
	int sseed;
    if (argc == 2) {
      sseed = atol(argv[1]);
    }
    srand(sseed);
		
    /* Default parameters.  */
    register long i, lo = 0, hi = 0;
	long lomax = 100000000000;
	long himax = 100000000000;
	
	lo = rand() % lomax;
	hi = lo + rand() % himax;

    for (i = lo; i < hi || hi < 0; i++) {
        /* An empty loop.  */
    }

    return 0;
}
