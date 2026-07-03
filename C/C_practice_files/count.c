// 4. Count Up and Down
// Use a for loop to print numbers from 1 to 10.
// Then use a while loop to print numbers from 10 down to 1.
#include <stdio.h>


int main(){
    int i;
    for(i = 0; i<=10; i++){
        printf("current number is %d \n",i);
    }

    int x = 10;
    while(x>0){
        printf("current number is %d \n",x);
        x--;
    }

}