/* 
 * This program reads in a string, the prints the value of the first
 * integer it finds in the string.
 */

#include <stdio.h>

/* returns 0 through 9 if the parameter is a digit,
 * -1 if the parameter is the minus sign, 
 * and -2 otherwise.
 */
int digitval (char ch) {
	if (ch <= '9' && ch >= '0') 
		/* this line depends on the digits having
		 * consecutive representations in ASCII
		 */
		return (int) (ch - '0');
	else if (ch == '-') 
		return -1;
	else
		return -2;
}

/* convert a string to integer */

int string_to_int (char s[]) {
	int	i, value, digit, sign;

	value = 0;

	/* get rid of leading text */

	for (i=0; s[i] && digitval (s[i]) == -2; i++);

	/* if the current character is a '-', set sign to -1 else 1 */

	if (s[i] == '-') {
		sign = -1;
		i++;
	} else
		sign = 1;

	/* grab up digits until there are no more, shifting them
	 * into place in the integer
 	 */

	for (; s[i]; i++) {
		digit = digitval (s[i]);
		if (digit < 0) break;
		value = (value * 10) + digit;
	}

	/* multiply in the sign determined earlier */

	value = sign * value;
	return value;
}

int main () {
  char	s[100] = "132412542634564241";


	/* prompt, get a string, print the integer */

	printf ("enter a number\n");
	printf ("value is %d\n", string_to_int (s));
}
