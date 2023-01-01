#include <stdio.h>


int main(void){
    char string[5] = {'a', 'b', 'c', 'd', 'e'}; // string is an address.
    char *pstring = string;
    printf("%p\n", pstring); 
    printf("%p\n", string);
    printf("%c\t%c", *(pstring), *(string));
    return 0; 
}