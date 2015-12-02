/*
 * fact.c
 *
 * This program prints the factorials of the numbers from 0 through 13
 */

#include <stdio.h>

/* This function computes the factorial of its parameter, returning it */
int factorial (int n) {
        int     i, 	/* loop counter */
		prod;	/* product accumulator */

	/* initially, prod = 1; this is the base case for 0! and 1! */

        prod = 1;

	/* multiply the numbers from 2 through n */

        for (i=2; i<=n; i++) 
		prod *= i;

	/* return the product */
        return prod;
}

/* main function */
int main () {
	int	i;	/* loop counter */

	/* as i goes from 0 through 13, print the factorial of i */

	for (i=0; i<=13; i++) printf ("%d\n", factorial (i));
	return 0;
}
