#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char str[1000];
    scanf("%s", str);
    for(int i = 0; i <=9; i++){
        int count = 0;
        char temp[10];
        int iAsciiVal = i + 48;
        for(int j = 0; j <= strlen(str); j ++){
            if((int) str[j] == iAsciiVal){
                ++count;
            }
        }
        printf("%d ", count);
        count = 0;
    }
       
    return 0;
}
