#include <stdio.h>

// Regular variable can only be accessed within the scope it's defined
// Static var can be accessed anywhere in the file regarding the scope.

// For function, regular functions can be use globally
// Static function is narrowed to the file where it's defined.

int counter(){
    // int count = 0;
    static int count = 0; // comment this line and uncomment the line above
    count++;
    return count;
}

int main(void){
    printf("%d\n", counter()); // This should return 1
    printf("%d", counter()); // This should return 2
    return 0;
}
