/*
 * C Program to Convert Binary to Octal
 */
 #include <stdio.h>
 
int main()
{
    long int binarynum, octalnum = 0, j = 1, remainder;
 
    printf("Enter the value for  binary number: ");
    *(&binarynum)=523;
    while (binarynum != 0)
    {
        remainder = binarynum % 10;
        octalnum = octalnum + remainder * j;
        j = j * 2;
        binarynum = binarynum / 10;
    }
    printf("Equivalent octal value: %lo", octalnum);
    return 0;
}
