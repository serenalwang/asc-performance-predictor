/*
 * seach-sort.c
 *
 * This program performs timings of insertion sort, linear search,
 * binary search, and qsort.
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
 * Insertion sort
 */
void insertion_sort (int v[], int n) {
	int	i, j, k;
	int	a;

	/* for each element from 0 through n-2, swap it with the
	 * smallest element from i through n-2
	 */
	for (i=0; i<n-1; i++) {

		/* k is the index of the minimum element */

		k = i;	
		for (j=i+1; j<n; j++)
			if (v[j] < v[k]) k = j;

		/* swap v[i] with v[k] */

		a = v[i];
		v[i] = v[k];
		v[k] = a;
	}
}

/*
 * Linear search
 */
int linear_search (int v[], int n, int value) {
	int     i;

	for (i=0; i<n; i++) if (v[i] == value) return i;
	return -1;
}

/*
 * Binary search
 */
int binary_search (int v[], int n, int value) {
        /* assumes v[] is in ascending sorted order */
        int     bottom, middle, top;

	/* initially, we consider the whole array, from bottom to top */

        bottom = 0;
        top = n;
        while (top-1 > bottom) {

		/* find the middle element */

                middle = (bottom + top) / 2;

		if (v[middle] < value) 		/* value is in "upper" half */
			bottom = middle;
		else if (v[middle] > value)	/* value is in "lower" half */
			top = middle;
		else
	                return middle;		/* found it */
	}
	return -1;	/* no luck, return -1 */
}

/* Integer comparison function for qsort (defined in stdlib.h/libc) */
int intcmp (int *a, int *b) {
	return (*a < *b) ? -1 : (*a > *b) ? 1 : 0;
}

int main (void) {
	int	*v, n, i, j, c1, c2;
	float	secs;

	n = 123;
	v = (int *) malloc (n * sizeof (int));	

	/* fill array with random numbers */

	for (i=0; i<n; i++) v[i] = rand() % 10000;

	/* sort the array with insertion sort */

	c1 = clock ();
	insertion_sort (v, n);
	c2 = clock ();

	secs = (c2 - c1) / (float) CLOCKS_PER_SEC;
	printf ("%f seconds for insertion sort on %d elements\n", secs, n);

	/* fill array with random numbers again and do a qsort */

	for (i=0; i<n; i++) v[i] = rand() % 10000;
	c1 = clock ();
	qsort((void *) v, n, sizeof (int),
		(int (*) (const void *, const void *)) intcmp);
	c2 = clock ();
	secs = (c2 - c1) / (float) CLOCKS_PER_SEC;
	printf ("%f seconds for qsort on %d elements\n", secs, n);

	/* do n linear searches in the array */

	c1 = clock ();
	for (i=0; i<n; i++) {
		j = linear_search (v, n, v[i]);
	}
	c2 = clock ();
	secs = (c2 - c1) / (float) CLOCKS_PER_SEC;
	printf ("%0.2f seconds for %d linear searches ", secs, n);
	printf ("(%0.2lf microseconds / search)\n", (secs * 10e6) / n);


	/* do n binary searches in the array */

	c1 = clock ();
	for (i=0; i<n; i++) {
		j = binary_search (v, n, v[i]);
	}
	c2 = clock ();
	secs = (c2 - c1) / (float) CLOCKS_PER_SEC;
	printf ("%0.2f seconds for %d binary searches ", secs, n);
	printf ("(%0.2lf microseconds / search)\n", (secs * 10e6) / n);
	free (v);
}
