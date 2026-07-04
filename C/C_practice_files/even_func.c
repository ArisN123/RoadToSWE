// 4. Is Even Function

// Write:

// bool is_even(int x);

// You will need:


#include <stdio.h>

int is_even(int x){
    return x%2 == 0;

}


int main(){

    int test_var = 0;

    int output = is_even(test_var);
    if(test_var != 0){
        if(output == 1){
            printf("%d is even\n",test_var);
    }else 
        printf("%d is odd\n",test_var);
    }else 
        printf("value is zero\n");


}