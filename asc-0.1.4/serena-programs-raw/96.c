#include<stdio.h>
int main()
{
static char *s[3]={"math","phy","chem"};
//typedef char* ppp;
typedef char* (*ppp)[3];
static ppp p1=&s,p2=&s,p3=&s;
printf("p1=%p\n",*(*p1+1));
char *(*(*array[3]))[3]={&p1,&p2,&p3};
printf("p1=%p\n",*(*array[2])[1]);
char *(*(*(*ptr)[3]))[3]=&array;
p2=p2+1;
p3=p3+2;
printf("%s\n",(***ptr[0])[2]);
return 0;
}
