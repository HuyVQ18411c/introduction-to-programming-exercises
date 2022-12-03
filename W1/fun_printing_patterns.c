/*
With the input n (int), print the following pattern

Ex: n = 4

4 4 4 4 4 4 4  
4 3 3 3 3 3 4   
4 3 2 2 2 3 4   
4 3 2 1 2 3 4   
4 3 2 2 2 3 4   
4 3 3 3 3 3 4   
4 4 4 4 4 4 4   

*/

#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int temp = n + 1;
    // Complete the code to print the pattern.
    int width, height;
    width = height = n * 2 - 1;
    for(int row = 1; row <= height; row++){
        for (int col = 1; col <= width; col++)
        {
            if (row == col && row <= (height/2) + 1)
            {
                temp = temp - 1;
            }
            // else if (row == col && row > (height/2) + 1)
            // {
            //     temp = temp + 1;
            // }
            if (col > width - row + 1 || col < )
            {
                temp = temp + 1;
            }

            if (row == 1 || row == height || col == 1 || col == width)
            {
                printf("%d ", n);
            }
            else
            {
                printf("%d ", temp);
            }

            if (col > width - row + 1)
            {
                temp = temp - 1;
            }

            if (col == width)
            {
                printf("\n");
            }
        }
    }
    return 0;
}
