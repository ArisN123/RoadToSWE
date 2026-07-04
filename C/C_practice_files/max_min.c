// 2. Maximum of Two Numbers

// Write:

// int max(int a, int b);

// Return the larger number.

// Extra: write min() too.


#include <stdio.h>


int max(int a, int b){

    if(a>=b){
        return a;
    }else return b;

}

int min(int a, int b){
    if (a>=b){
        return b;
    }  
    else 
        return a;
}


int main(){

    int test_1 = 50;
    int test_2 = 500;

    int output_max = max(test_1,test_2);
    int output_min = min(test_1, test_2);

    printf("max function gave output %d\n min function gave output %d \n", output_max,output_min);


}