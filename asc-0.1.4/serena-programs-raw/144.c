/*
 * C program to swap the contents of two numbers using bitwise XOR
 * operation. Don't use either the temporary variable or arithmetic
 * operators
 */
#include <stdio.h>
 
void main()
{
    long i, k;
 
    printf("Enter two integers \n");
    *(&i)=458;*(&k)=29;
    printf("\n Before swapping i= %ld and k = %ld", i, k);
    i = i ^ k;
    k = i ^ k;
    i = i ^ k;
    printf("\n After swapping i= %ld and k = %ld", i, k);
}
