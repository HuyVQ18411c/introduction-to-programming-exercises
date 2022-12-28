/*
In C we don't have any kind of "class"
"struct" is the way to go
*/
#include <stdio.h>

struct Animal{
    char *name;
    int numberOfLegs;
};

int main(void){
    struct Animal elephant;

    char elephantName[8] = {"elephant"};
    elephant.name = elephantName;
    elephant.numberOfLegs = 4;

    printf("Animal name: %s\n", elephant.name);
    printf("Number of legs: %d", elephant.numberOfLegs);
    
    return 0;
}