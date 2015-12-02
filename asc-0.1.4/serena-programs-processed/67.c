/*
 * C Program to Count the Number of Trailing Zeroes in Integer
 */
#include <stdio.h>
 
void main()
{
    int j = 31, i, count = 0;
    unsigned int num;
    int b[32] = {0};
 
    printf("enter the number:");
    num = 123098417;
    while (num != 0)
    {
        if (num & 1 == 1)
        {
            break;
        }
        else
        {
            count++;
            num = num >> 1;
 
        }
    }
    printf("\n%d", count);
}
