#include <stdio.h>

int add_int(int, int);
float add_float(float, float);
void print_str(char *ptr);

int add_int(int num1, int num2){
    return num1 + num2;
}

float add_float(float num1, float num2){
    return num1 + num2;
}

void print_str(char *name){
    printf("Hello %s\n", name);
}

const char * str_return() {
    static char s[] = "027f7757d71324a8e6d4c8d1a029ca84de6f0649fd1b122aa91f8bf0a9a9bdb625";
    return s;
}
