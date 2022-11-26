#include <stdio.h>

int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);

    char *collections[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    for(int i = a; i <= b; i++){
        if(i <= 9 && i >= 1){
            printf("%s\n", collections[i-1]);
        }
        else if(i > 9){
            if(i % 2 == 0){
                printf("even\n");
            }
            else{
                printf("odd\n");
            }
        }
    }
    
    return 0;
}
