/*
 * This function prints the first 20 fibonacci numbers, F_0..F_19
 */
#include <stdio.h>

/* 
 * This function computes the n'th fibonacci number 
 */
int F (int n) {
	int	F_i, 		/* current fibonacci number */
		F_i_minus_1, 	/* previous fibonacci number */
		temp;		/* temporary calculation */
	int	i;		/* loop counter */

	/* if 0'th fibonacci number, algorithm below won't work,
	 * so just return with 0 (which is the right answer)
	 */
	if (n == 0) return 0;

	/* first two fibonacci numbers */

	F_i_minus_1 = 0;
	F_i = 1;

	/* start at the second and calculate through the n'th */

	for (i=2; i<=n; i++) {

		/* calculate the current fibonacci number, keeping
		 * the result in temp for now
		 */

		temp = F_i_minus_1 + F_i;

		/* shift F_i and F_i-1 over to the next position */

		F_i_minus_1 = F_i;
		F_i = temp;
	}

	/* finally... */

	return F_i;
}

/* main function */
int main () {
	int	i;

	/* print the index and value of F_0..F_19 */

	for (i=0; i<=20; i++) {
		printf ("%d\t%d\n", i, F(i));
	}
}
