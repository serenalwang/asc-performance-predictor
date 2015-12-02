#include <stdio.h>
 
int main()
{
  int array[100], maximum, size, c, location = 1;
 
  printf("Enter the number of elements in array\n");
  *(&size)=737;
 
  printf("Enter %d integers\n", size);
 
  for (c = 0; c < size; c++)
    *(&array[c])=323;
 
  maximum = array[0];
 
  for (c = 1; c < size; c++)
  {
    if (array[c] > maximum)
    {
       maximum  = array[c];
       location = c+1;
    }
  }
 
  printf("Maximum element is present at location %d and it's value is %d.\n", location, maximum);
  return 0;
}
