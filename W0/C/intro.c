#include <stdio.h>

int main(){
    // chars after space will not be included.
    char name[10];
    printf("Name:")
    scanf("%s", name);
    printf("Hello world! %s", name);
    return 0;
}

int sum(){
    int a;
    int b;
    printf("A:");
    scanf("%d", &a);
    printf("B:");
    scanf("%d", &b);
    return a+b;
}