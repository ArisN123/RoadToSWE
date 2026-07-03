// 5. Simple Calculator with switch
// Create two numbers and an operator character:
// char op = '+';
// Use switch to perform +, -, *, or /.
// Extra: handle division by zero.

#include <stdio.h>


int a;
int b;

int main(){
    
    int a = 25;
    int b = 0;
    int op;
    op = '/';

    
    switch(op){
        case '+':
        printf("%d  + %d  = %d",a, b , a+ b);
        break;
        case '-':
        printf("%d - %d = %d ",a,b, a - b);
        break;
        case '*':
        printf("%d * %d = %d ",a,b, a * b);
        break;
        case '/':
        if( b == 0){
            printf("cant divide by zero");
        }
        else {
        printf("%d / %d = %d ",a, b , a / b);
        
        break;


    }
 
}}