#include <stdlib.h>
#include <stdio.h>

static void kernel_floyd_warshall(int n, double path[n][n])
{
    int i, j, k;

    for (k = 0; k < n; k++) {
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                path[i][j] = path[i][j] < path[i][k] + path[k][j] ?
                    path[i][j] : path[i][k] + path[k][j];
            }
        }
    }
}

static void print_array(int n, double path[n][n])
{
    int i, j;

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%0.2lf ", path[i][j]);
        }

        printf("\n");
    }

    printf("\n");
}

static void init_array(int n, double path[n][n])
{
    int i, j;

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            path[i][j] = ((double) (i + 1) * (j + 1)) / n;
}

#define MAX_PATH 4096

static double path[MAX_PATH][MAX_PATH];

int main(int argc, char *argv[])
{
	/* Serena's seed */
	int sseed;
    if (argc == 2) {
      sseed = atol(argv[1]);
    }
    srand(sseed);
	
    /* Default parameters.  */
    unsigned seed = rand();
    int nmax = 50;
    int n = rand() % nmax;
    srand(seed);
	
    if (n > MAX_PATH)
        n = MAX_PATH;

    init_array(n, path);

#if 0
    print_array(n, path);
#endif

    kernel_floyd_warshall(n, path);

#if 0
    print_array(n, path);
#endif

    return 0;
}
