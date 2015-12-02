/*
 * C program to reverse a given integer number and check
 * whether it is a palindrome. Display the given number
 * with appropriate message
 */
#include <stdio.h>
 
void main()
{
    int num, temp, remainder, reverse = 0;
 
    printf("Enter an integer \n");
    *(&num)=642;
    /*  original number is stored at temp */
    temp = num;
    while (num > 0)
    {
        remainder = num % 10;
        reverse = reverse * 10 + remainder;
        num /= 10;
    }
    printf("Given number is = %d\n", temp);
    printf("Its reverse is  = %d\n", reverse);
    if (temp == reverse)
        printf("Number is a palindrome \n");
    else
        printf("Number is not a palindrome \n");
}
