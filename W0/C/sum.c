#include <stdio.h>

// Calculate sum and different of two int and float
int main(){
    int a, b;
    float c, d;

    scanf("%d %d", &a, &b);
    scanf("%f %f", &c, &d);

    printf("%d %d\n", a+b, a-b);
    printf("%.2f %.2f", c + d, c - d);
    return 0;
}