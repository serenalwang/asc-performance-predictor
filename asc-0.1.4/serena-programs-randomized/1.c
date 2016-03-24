/* Generates an array of random integers. The seed is given by 
 * the first argument, and the size of the array is given by the
 * second argument.
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int maxnrand = 1000;
  int seed;
  if (argc == 2) {
    seed = atol(argv[1]);
  }

  // Generate random seed.
  srand(seed);
  
  int nrand = rand() % maxnrand + 1;
  
  int randarray[nrand];
  for (int i = 0; i < nrand; i++) {
    randarray[i] = rand();
  }
  
  int randindex = rand() % nrand;

  printf("%d\n", randarray[randindex]);
  
  return randarray[randindex]; 
}
