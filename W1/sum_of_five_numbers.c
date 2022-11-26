#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    int sum = 0;
    int num = 0;
    for(int i = 4; i >= 0; i--){
        int divider = pow(10, i);
        if(n < divider){
            n = n + divider;
            num = 0;
            n = n - 1 * divider;
        }
        else{
            num = n / divider;
            n = n - num * divider;
        }
        sum += num;
        printf("%d\t%d\t%d\n", num, n, divider);
    }
    printf("%d", sum);
    return 0;
}