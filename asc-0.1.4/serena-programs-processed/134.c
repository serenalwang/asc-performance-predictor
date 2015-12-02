/*
 * C Program to Find the Sum of two Binary Numbers
 */
#include <stdio.h>
 
int main()
{
 
    long binary1, binary2;
    int i = 0, remainder = 0, sum[20];
 
    printf("Enter the first binary number: ");
    *(&binary1)=444;
    printf("Enter the second binary number: ");
    *(&binary2)=429;
    while (binary1 != 0 || binary2 != 0)
    {
        sum[i++] =(binary1 % 10 + binary2 % 10 + remainder) % 2;
        remainder =(binary1 % 10 + binary2 % 10 + remainder) / 2;
        binary1 = binary1 / 10;
        binary2 = binary2 / 10;
    }
    if (remainder != 0)
        sum[i++] = remainder;
    --i;
    printf("Sum of two binary numbers: ");
    while (i >= 0)
        printf("%d", sum[i--]);
    return 0;
}
