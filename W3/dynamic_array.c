/*
The idea of dynamic array (from MIT): https://www.youtube.com/watch?v=CHhwJjR0mZA
In short:
- Size of array is dynamic
- Size x 2 whenever it reachs the size limit and needs to insert a new element 
- Size skrink whenever it's possible after remove an element
*/

#include <stdio.h>
#include <stdlib.h>


int main(void){
    // Assume that at first we need an array with 3 elements
    int n = 3;
    int *element;
    element = (int*) calloc(n, sizeof(int));

    if(element == NULL){
        exit(0);
    }

    // Let assign some values to the memory chunk
    for(int i = 0; i < n; i++){
        printf("%d", i);
        scanf("%d", element + i);
        printf("\n");
    }
    // To insert a new element, we re-allocate a new size for it
    element = (int*) realloc(element, n * 2  * sizeof(int));

    printf("%d", *(element + 1)); // Ensure the old values are preserve

    free(element);
    return 0;
}



