#include <stdio.h>


struct point{
    int width;
    int height;
};

typedef struct{
    int width;
    int height;
} point2;


int draw(struct point p){
    for(int h = 0; h < p.height; h++){
        for(int w = 0; w < p.width; w++){
            if(w == p.width - 1){
                printf("*\n");
            }
            else{
                printf("*");
            }
        }
    }
}

int draw2(point2 p){
    for(int h = 0; h < p.height; h++){
        for(int w = 0; w < p.width; w++){
            if(w == p.width - 1){
                printf("*\n");
            }
            else{
                printf("*");
            }
        }
    }
}

int main(void){
    struct point p;
    scanf("%d", &p.width);
    scanf("%d", &p.height);

    draw(p);

    printf("\n\n");

    point2 p2;
    p2.width = p.width;
    p2.height = p.height;

    draw2(p2);
    return 0;
}
