/*
 * C Program to round floor of integer to next lower power of 2
 */
#include <stdio.h>
#define NUM_BITS_INT 32
int count = 0;
 
void main()
{
    int temp, n, bit, i = 0;
 
    printf("Enter a number : ");
    n = 1203984;
    temp = n;
    while (i < NUM_BITS_INT)
    {
        bit = temp & 0x80000000;
        if (bit == -0x80000000) 
        {
            bit = 1;
        }
        printf("%d", bit);
        temp = temp << 1;
        i++;
    }
}
