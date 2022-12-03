#include <stdio.h>
#include <math.h>

/*
This is a really interesting operator. 
Although, if you follow web development career path (like me) 
or using high level programming language you will find it hard to see these operations.

I also question about this real-world-example. For now, I will only focus on what they can do, I don't have knowledge currently to answer this question directly.
Here is a thread of discussion about its application: https://www.sololearn.com/discuss/1847830/what-is-the-use-of-bitwise-operators-in-real-life

Example:
3 = 00000011 (In Binary)
5 = 00000101 (In Binary)

AND (&) will return 1 if every corresponding bits of two operands is 1, and return 0 otherwise.
OR (|) will return 1 if there is at least one corresponding bit of two operands is 1.
XOR (^) will return 1 if corresponding bits of two operands are opposite (1-0, 0-1)

AND operation        OR operation        XOR operation
  00000011             00000011            00000011
& 00000101           | 00000101          ^ 00000101
  ________             ________            ________
  00000001  = 1        00000111  = 7       00000110  = 6
*/

void calculate_the_maximum(int n, int k) {
  //Write your code here.
    int and_max = 0;
    int or_max = 0;
    int xor_max = 0;
    for(int a = 1; a < n; a++)
    {
        for (int b = a + 1; b <= n; b++)
        {
            int and = a&b;
            int or = a|b;
            int xor = a^b;
            if(and > and_max && and < k)
            {
                and_max = a&b;
            }
            if(or > or_max && or < k)
            {
                or_max = a|b;
            }
            if(xor > xor_max && xor < k)
            {
                xor_max = a^b;
            }
        }
    }
    printf("%d\n%d\n%d", and_max, or_max, xor_max);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
