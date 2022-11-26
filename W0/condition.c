#include<stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    char *collections[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    if(n > 9){
        printf("Greater than 9");
    }
    else if(n >= 1 && n <= 9){
        printf("%s", collections[n-1]);
    }
    return 0;
}
