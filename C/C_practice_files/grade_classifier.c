// 3. %d is equivalent to grade Classifier

// Store ar[a] score from 0 to 100.

// Print:

// A: 90-100
// B: 80-89
// C: 70-79
// D: 60-69
// F: below 60

// Use if, else if, and else.

#include <stdio.h>


int main(){
    
    int a;
    
    int ar[7]= {95,85,75,65,55,105,-105};

    for (a = 0; a < 7; a++)
    {
       if(100 >= ar[a] && ar[a] >= 90){
        printf("%d is equivalent to grade A\n",ar[a]);
    }
    else if(89>= ar[a] && ar[a] > 80){
        printf("%d is equivalent to grade B\n",ar[a]);
    }
    else if(79>= ar[a] && ar[a] > 70){
        printf("%d is equivalent to grade C\n",ar[a]);
    }
    else if(69>= ar[a] && ar[a] > 60){
        printf("%d is equivalent to grade D\n",ar[a]);
    }
    else if(59>= ar[a] && ar[a] >= 0){
        printf("%d is equivalent to grade F\n",ar[a]);
    }
    else {
         printf("Error, invalid value\n");
    }

    }
    

    // if(100 >= ar[a] && ar[a] >= 90){
    //     printf("%d is equivalent to grade A\n",ar[a]);
    // }
    // else if(89>= ar[a] && ar[a] > 80){
    //     printf("%d is equivalent to grade B\n",ar[a]);
    // }
    // else if(79>= ar[a] && ar[a] > 70){
    //     printf("%d is equivalent to grade C\n",ar[a]);
    // }
    // else if(69>= ar[a] && ar[a] > 60){
    //     printf("%d is equivalent to grade D\n",ar[a]);
    // }
    // else if(59>= ar[a] && ar[a] >= 0){
    //     printf("%d is equivalent to grade F\n",ar[a]);
    // }
    // else {
    //      printf("Error, invalid value\n");
    // }

    

}