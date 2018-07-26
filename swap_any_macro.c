#include <stdio.h>
#include <string.h>

#define swap(x,y) do \ 
   { unsigned char swap_temp[sizeof(x) == sizeof(y) ? (signed)sizeof(x) : -1]; \
     memcpy(swap_temp,&y,sizeof(x)); \
     memcpy(&y,&x,       sizeof(x)); \
     memcpy(&x,swap_temp,sizeof(x)); \
    } while(0)

int main(int argc, char **argv){
    char a,b;
    int c,d;
    float e,f;

    a = 'a', b = 'b';
    c = 1, d = 2;
    e = 11.11, f = 12.12;

    printf("a[%c] b[%c], c[%d] d[%d], e[%f] f[%f]\n",a,b,c,d,e,f);
    swap(a,b);
    swap(c,d);
    swap(e,f);
    printf("a[%c] b[%c], c[%d] d[%d], e[%f] f[%f]\n",a,b,c,d,e,f);

    return 0;
}