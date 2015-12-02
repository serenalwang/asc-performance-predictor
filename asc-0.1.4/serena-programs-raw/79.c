#include <stdio.h>
 
int main()
{
   int array[100], search, c, n;
 
   printf("Enter the number of elements in array\n");
   *(&n)=284;
 
   printf("Enter %d integer(s)\n", n);
 
   for (c = 0; c < n; c++)
      *(&array[c])=133;
 
   printf("Enter the number to search\n");
   *(&search)=520;
 
   for (c = 0; c < n; c++)
   {
      if (array[c] == search)     /* if required element found */
      {
         printf("%d is present at location %d.\n", search, c+1);
         break;
      }
   }
   if (c == n)
      printf("%d is not present in array.\n", search);
 
   return 0;
}
