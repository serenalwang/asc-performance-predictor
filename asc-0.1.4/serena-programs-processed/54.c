/* 
 * C Program to use Bitwise Operations to Round(floor of) an Integer 
 * to next Lower Multiple of 2
 */
#include <stdio.h>
 
void main()
{
    int x = 1, i, n;
 
    printf("enter the number :");
    n = 1234115;
    /* for positive values */
    if (n > 0)
    {
        for (; x <= n >> 1;)
        {
            x = x << 1;
        }
        n = x;
    }
    /* for negative values */
    else
    {
        n = ~n;
        n = n + 1;
        for (; x <= n >> 1;)
        {
            x = x << 1;
        }
        x = x << 1;
        x = ~x;
        x = x + 1;
        n = x;
    }
    printf("%d", n);
}
