#include<stdio.h>
#include<string.h>
#define MAX 10000

int validate(char []);
int modulerDivision(char[],unsigned long);


int main(int argc, char *argv[]){
	
	/* Serena's seed */
	int sseed;
    if (argc == 2) {
      sseed = atol(argv[1]);
    }
    srand(sseed);
	
	char dividend[size];
	int size = rand() % 30;	
	for(int i = 0; i < size; ++i) {
		dividend[i] = rand() % 10 + '0';
	}
    unsigned long int divisor,remainder;
    unsigned long int divisormax = 1 << size;	
	divisor = rand() % divisormax;
	
    if(validate(dividend))
         return 0;

    remainder = modulerDivision(dividend,divisor);

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

int modulerDivision(char dividend[],unsigned long divisor){
   
    unsigned long temp=0;
    int i=0;

    while(dividend[i]){
        
         temp = temp*10 + (dividend[i] -48);
         if(temp>=divisor){
             temp = temp % divisor;
         }
   
         i++;
    }

    return temp;
}
