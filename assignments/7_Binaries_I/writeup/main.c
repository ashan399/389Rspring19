/*
 * Name: Ashan Panduwawala
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Ashan Panduwawala
 */

#include <stdio.h>
int main()
{
int x = 0xfeedface;
int y = 0x1ceb00da;
printf("%d\n" , x);
printf("%d\n", y);
x = x^y;
y = y^x;
x = x^y;
printf("%d\n", x);
printf("%d\n",y);
return 0;
}
