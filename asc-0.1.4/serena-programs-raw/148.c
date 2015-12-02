#include<stdio.h>
#include<string.h>
#define MAX 10000

int validate(char []);
char * division(char[],long);
long int remainder;

int main(){

    char dividend[MAX] = "1212342453426345637";
    char *quotient;
    long int divisor;

    printf("Enter dividend: ");
    if(validate(dividend))
         return 0;

    printf("Enter divisor: ");
    *(&divisor)=618;

    quotient = division(dividend,divisor);

    while(*quotient)
         if(*quotient ==48)
             quotient++;
         else
             break;

    printf("Quotient: %s / %ld  =  %s",dividend,divisor,quotient);
    printf ("\nRemainder: %ld",remainder);
    return 0;
}

int validate(char num[]){
    int i=0;

    while(num[i]){
         if(num[i] < 48 || num[i]> 57){
             printf("Invalid positive integer: %s",num);
             return 1;
         }
         i++;
    }

    return 0;
}

char * division(char dividend[],long divisor){
   
    static char quotient[MAX];
    long temp=0;
    int i=0,j=0;

    while(dividend[i]){
        
         temp = temp*10 + (dividend[i] -48);
         if(temp<divisor){
            
             quotient[j++] = 48;
            
         }
         else{
             quotient[j++] = (temp / divisor) + 48;;
             temp = temp % divisor;

         }
         i++;
    }

    quotient[j] = '\0';
    remainder = temp;
    return quotient;
}
