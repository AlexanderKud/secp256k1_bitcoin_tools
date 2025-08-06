#pragma once

extern "C" __declspec(dllexport) int add_int(int, int);
extern "C" __declspec(dllexport) float add_float(float, float);
extern "C" __declspec(dllexport) void print_str(char *ptr);
extern "C" __declspec(dllexport) void print_hello();