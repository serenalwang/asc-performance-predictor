/*
 * C program to multiply given number by 4 using bitwise operators
 */
#include <stdio.h>
 
void main()
{
    long number, tempnum;

    for (int i = 0; i < 100; i++) {
    printf("Enter an integer \n");
    *(&number)=379;
    tempnum = number;
    /*  left shift by two bits */
    number = number << 2;
    printf("%ld x 4 = %ld\n", tempnum, number);
    }
}
