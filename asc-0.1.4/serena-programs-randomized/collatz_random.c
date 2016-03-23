/* Runs the original program collatz.c in kernels folder such that
 * it automatically randomizes input each time.
 */

/* Take any natural number i.  If i is even, divide it by 2 to get i / 2.
 * If i is odd, multiply it by 3 and add 1 to obtain 3i + 1.
 * Repeat the process indefinitely, halting if you reach 1 (a fixpoint).
 * The Collatz conjecture is that no matter what number i you start with,
 * you will always eventually reach 1.
 */

#include <stdio.h>
#include <stdlib.h>

static unsigned long step(unsigned long j)
{
    register unsigned long k = j;

    if ((k % 2) == 0)
        j = j / 2;
    else
        j = 3*j + 1;

    return j;
}

int main(int argc, char *argv[])
{
    register unsigned long i;
    register unsigned long j;
    int seed;
    if (argc == 2) {
      seed = atol(argv[1]);
    }
    srand(seed);

    int max = 10000000;
    unsigned long lo = rand() % max;
    unsigned long hi = (rand() % (max - lo)) + lo;
    printf("lo: %lu, hi: %lu \n", lo, hi);

    /* Search for a counterexample to the Collatz conjecture.  */
    for (i = lo; i < hi; i++) {
        for (j = i; j > 1; j = step(j)) {
            /* This may be an infinite loop.  */
#if 0
            printf("%7lu\t%7lu\n", i, j);
#endif
        }
    }

    return i;
}
