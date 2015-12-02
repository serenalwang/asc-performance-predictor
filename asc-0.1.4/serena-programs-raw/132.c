/*
 * C program to accept an integer and reverse it
 */
#include <stdio.h>
 
void main()
{
    long  num, reverse = 0, temp, remainder;
 
    printf("Enter the number\n");
    *(&num)=272;
    temp = num;
    while (num > 0)
    {
        remainder = num % 10;
        reverse = reverse * 10 + remainder;
        num /= 10;
    }
    printf("Given number = %ld\n", temp);
    printf("Its reverse is = %ld\n", reverse);
}
