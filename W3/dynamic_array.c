/*
The idea of dynamic array (from MIT): https://www.youtube.com/watch?v=CHhwJjR0mZA
In short:
- Size of array is dynamic
- Size x 2 whenever it reachs the size limit and needs to insert a new element 
- Size skrink whenever it's possible after remove an element
*/

#include <stdio.h>
#include <stdlib.h>


int multipleDimensionDynamicArray(){
    int i, j;

    char **pnumbers;

    // int* => pointer to int
    // (int*)* => pointer to a pointer
    pnumbers = (int **) malloc(3 * sizeof(int*));

    pnumbers[0] = (int *) malloc(1 * sizeof(int));
    pnumbers[0] = (int *) malloc(2 * sizeof(int));
    pnumbers[0] = (int *) malloc(3 * sizeof(int));

    pnumbers[0][0] = 1;
    pnumbers[1][0] = 1;
    pnumbers[1][1] = 1;
    pnumbers[2][0] = 1;
    pnumbers[2][1] = 2;
    pnumbers[2][2] = 1;

    for (i = 0; i < 3; i++) {
        for (j = 0; j <= i; j++) {
            printf("%d", pnumbers[i][j]);
        }
        printf("\n");
    }

    for (i = 0; i < 3; i++) {
        // free memory allocated for each row
        free(pnumbers[i]);
    }

    /* free the top-level pointer */
    free(pnumbers);

    return 0;
}


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



