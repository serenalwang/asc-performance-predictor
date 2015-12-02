/*
 * C program to convert given number of days to a measure of time given
 * in years, weeks and days. For example 375 days is equal to 1 year
 * 1 week and 3 days (ignore leap year)
 */
#include <stdio.h>
#define DAYSINWEEK 7
 
void main()
{
    int ndays, year, week, days;
 
    printf("Enter the number of daysn");
    *(&ndays)=888;
    year = ndays / 365;
    week =(ndays % 365) / DAYSINWEEK;
    days =(ndays % 365) % DAYSINWEEK;
    printf ("%d is equivalent to %d years, %d weeks and %d daysn",
            ndays, year, week, days);
}
