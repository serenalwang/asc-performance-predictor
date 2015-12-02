/*
 * C program to find the sum of first 50 natural numbers
 * using for loop
 */
#include <stdio.h>
 
void main()
{
    int  num, sum = 0;
 
    for (num = 1; num <= 1000; num++)
    {
        sum = sum + num;
    }
    printf("Sum = %4d\n", sum);
}
