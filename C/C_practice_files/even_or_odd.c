// 2. Even or Odd
// Create an int variable and use % to decide whether it is even or odd.
// Example output:
// 17 is odd
// Extra: test negative numbers too.

#include <stdio.h>


char *even_or_odd(int x){
    
    if((x % 2) == 0){
        return "even";
    }
    else{
        return "odd";
    }
}



int main(){
   printf(even_or_odd(-50));
}