#include "pch.h"
#include "adder.h"
#include <stdio.h>

int add_int(int, int);
float add_float(float, float);
void print_str(char *);
void print_hello();

int add_int(int num1, int num2) {
    return num1 + num2;
}

float add_float(float num1, float num2) {
    return num1 + num2;
}

void print_str(char *name) {
    printf("Hello %s\n", name);
}

void print_hello() {
    printf("Hello from dll_function!\n");
}