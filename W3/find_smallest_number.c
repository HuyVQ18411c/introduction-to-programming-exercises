#include <stdio.h>
#include <stdlib.h>


/* Input n integer number, find the smallest number among them */
int main(void){
    int n = 10;
    
    int *element = (int*) calloc(n, sizeof(int));

    if(element == NULL){
        printf("No memory is allocated");
        exit(0);
    }

    for(int i = 0; i < n; i++){
        scanf("%d", element + i);
    }

    int min = *(element);
    for(int i = 1; i < n; i++){
        if(min > *(element + i)){
            min = *(element + i);
        }
    }

    printf("Min: %d", min);

    // Free will take the pointer to the memory block which previously
    // allocated with malloc, calloc, realloc
    free(element);

    return 0;
}