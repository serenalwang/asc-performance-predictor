/*
 * C Program to Add two Complex Numbers
 */
#include <stdio.h>
 
struct complex
{
   int realpart, imaginary;
};
 
main()
{
    struct complex a, b, c;
 
    printf("Enter value of a and b complex number a + ib.\n");
    printf("value of complex number a is = ");
    *(&a.realpart)=621;
    printf("value of complex number b is = ");
    *(&a.imaginary)=52;
    printf("Enter value of c and d complex number c + id.\n");
    printf("value of complex number c is = ");
    *(&b.realpart)=545;
    printf("value of complex number d is = ");
    *(&b.imaginary)=702;
    c.realpart = a.realpart + b.realpart;
    c.imaginary = a.imaginary + b.imaginary;
    if (c.imaginary >= 0)
        printf("complex numbers sum is = %d + %di\n", c.realpart, c.imaginary);
    else
        printf("complex numbers sum = %d %di\n", c.realpart, c.imaginary);
    return 0;
}
