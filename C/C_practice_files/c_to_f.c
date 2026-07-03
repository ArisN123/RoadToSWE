// 1. Temperature Converter
// Write a program that stores a Celsius temperature in a float, converts it to Fahrenheit, and prints both.
// Formula:
// F = C * 9 / 5 + 32
// Extra: add an if statement that prints "Hot" if Fahrenheit is above 80.
#include <stdio.h>

int c_to_f(int a){
   return  ((a * 9) / 5) + 32 ;
}

int main(void){
    int x = 20;
    int y = c_to_f(x);

    if(y>=80){
        printf("x is %d, its hot", y);
    }
    else {
        printf("x is %d, its cold", y);
    }
}