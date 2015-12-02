#include <stdio.h>
#include <stdlib.h>
 
int main() {
  int c, n;
 
  printf("100 random numbers in [1,100]\n");
 
  for (c = 1; c <= 100; c++) {
    n = rand() % 100 + 1;
    printf("%d\n", n);
  }
 
  return 0;
}
