#include <stdio.h>
#include <stdlib.h>


int main(void){
    int n = 3;
    float *element;

    // castType* calloc(numberOfElement, size of type)
    // castType* malloc(numberOfElement, size of type)

    // malloc will randomly allocate memory
    // while calloc will give you a chain of memory 

    // if successfuly allocated, 
    // "element" will return the address of the first byte
    element = (float*)calloc(n, sizeof(float));

    if(element == NULL){
        printf("No memory is allocated");
        exit(0);
    }

    printf("%p", &element);
    printf("\n");
    printf("%f", *element);
    printf("\n");
    // Input the value
    scanf("%f", element);
    printf("\n");
    scanf("%f", element + 1);
    printf("\n");
    scanf("%f", element + 2);
    printf("\n");


    printf("%f", *element);
    printf("\n");
    printf("%f", *(element + 1));
    printf("\n");
    printf("%f", *(element + 2));

    free(element);
    
    return 0;
}
