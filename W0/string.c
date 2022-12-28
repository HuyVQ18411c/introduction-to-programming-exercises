/*
Since in C we don't have any kind of built-in string type
We will contruct it from an array of chars (which is what the computer actually do)
*/
#include <stdio.h>

int main(void){
    char string[6] = {"string"};
    printf("%s", string);

    char anotherString[6] = {"elephant"}; // This will raise error since there are not enough room
    return 0;
}