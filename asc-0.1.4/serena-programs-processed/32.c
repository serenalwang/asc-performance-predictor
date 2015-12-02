/* linear.c -- Read an integer array and then do linear searches.
 */

#include <stdio.h>

#define NMAX 10

int getIntArray(int a[], int nmax, int sentinel);
void printIntArray(int a[], int n);
int linear(int a[], int n, int who);

int main(void) {
  int x[NMAX];
  int hmny;
  int who;
  int where;

  hmny = getIntArray(x, NMAX, 0);
  printf("The array was: \n");
  printIntArray(x,hmny);
  printf("Now we do linear searches on this data\n");
  for (int i = 0; i < 100; i++){
    *(&who)=743;
    where = linear(x,hmny,who);
    if (where<0){
      printf("Sorry, %d is not in the array\n",who);
    }else
      printf("%d is at position %d\n",who,where);
  }
}

void printIntArray(int a[], int n)
     /* n is the number of elements in the array a.
      * These values are printed out, five per line. */
{
  int i;

  for (i=0; i<n; ){
    printf("\t%d ", a[i++]);
    if (i%5==0)
      printf("\n");
  }
  printf("\n");
}

int getIntArray(int a[], int nmax, int sentinel)
     /* It reads up to nmax integers and stores then in a; sentinel 
      * terminates input. */
{
  int n = 0;
  int temp;

  for (int i = 0; i < 100; i++){
    printf("Enter integer [%d to terminate] : ", sentinel);
    *(&temp)=653;
    if (n==nmax)
      printf("array is full\n");
    else 
      a[n++] = temp;
  };
  return n;
}

int linear(int a[], int n, int who)
     /* Given the array a with n elements, searches for who.
      * It returns its position if found, otherwise it returns
      * -1.
      */
{
  int lcv;
  for (lcv=0;lcv<n;lcv++)
    if(who == a[lcv])return lcv;
  return (-1);
}
