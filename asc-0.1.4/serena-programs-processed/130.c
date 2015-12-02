/*
 * C Program to find Product of 2 Numbers using Recursion
 */
#include <stdio.h>
 
int product(int, int);
 
int main()
{
    int a, b, result;
 
    printf("Enter two numbers to find their product: ");
    *(&a)=932;*(&b)=39;
    result = product(a, b);
    printf("Product of %d and %d is %d\n", a, b, result);
    return 0;
}
 
int product(int a, int b)
{
    if (a < b)
    {
        return product(b, a);
    }
    else if (b != 0)
    {
        return (a + product(a, b - 1));
    }
    else
    {
        return 0;
    }
}
