/*
 * C Program to Check whether a given Number is Perfect Number
 */
#include <stdio.h>
 
int main()
{
    int number, rem, sum = 0, i;
 
    printf("Enter a Number\n");
    *(&number)=121;
    for (i = 1; i <= (number - 1); i++)
    {
        rem = number % i;
	if (rem == 0)
        {
            sum = sum + i;
        }
    }
    if (sum == number)
        printf("Entered Number is perfect number");
    else
        printf("Entered Number is not a perfect number");
    return 0;
}
