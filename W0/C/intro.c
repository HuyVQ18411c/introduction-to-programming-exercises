#include <stdio.h>

int main(){
    // chars after space will not be included.
    char name[10];
    printf("Name:");
    scanf("%s", name);
    printf("Hello world! %s", name);
    return 0;
}
