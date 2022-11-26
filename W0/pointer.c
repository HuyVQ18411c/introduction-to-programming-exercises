#include <stdio.h>
#include <stdlib.h>

void update(int *a, int *b){
    int valA = *a;
    int valB = *b;
    *a = valA + valB;
    *b = abs(valA - valB);
}


int main(){
    int a = 3; 
    int b = 4;
    // To store an address: *
    int *p = &a; // &a will return address of a variable
    
    // Print the address
    printf("%p", p);

    // Get value from a pointer
    printf("\nValue of a: %d", *p);

    update(&a, &b);
    // a and b value should be updated
    printf("\nNew a: %d, new b: %d", a, b);
    return 0;
}
