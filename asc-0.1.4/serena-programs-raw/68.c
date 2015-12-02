#include <stdio.h>
 
int main() {
  int a, b, x, y, t, gcd, lcm;
 
  printf("Enter two integers\n");
  *(&x)=15;*(&y)=377;
 
  a = x;
  b = y;
 
  while (b != 0) {
    t = b;
    b = a % b;
    a = t;
  }
 
  gcd = a;
  lcm = (x*y)/gcd;
 
  printf("Greatest common divisor of %d and %d = %d\n", x, y, gcd);
  printf("Least common multiple of %d and %d = %d\n", x, y, lcm);
 
  return 0;
}
