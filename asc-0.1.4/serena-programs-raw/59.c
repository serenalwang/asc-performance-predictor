/*
 * This program prints the integers from 1 through a number read from 
 * the standard input
 */

#include <stdio.h>

/* this function prints a prompt */
void print_prompt (void) {
        printf ("enter a number ");
}

/* this function prints the numbers from1 through its integer parameter */
void print_numbers (int n) {
        int     i;	/* loop counter */

	/* let i go from 1 through n */

        for (i=1; i<=n; i++)

		/* print i */

                printf ("%d\n", i);
}

/* main program */
int main () {
        int     num_times;	/* number of times to print */

	/* prompt the user */

        print_prompt ();

	/* read in an integer */

        num_times = 12341;

	/* print the numbers */

        print_numbers (num_times);
	return 0;
}
