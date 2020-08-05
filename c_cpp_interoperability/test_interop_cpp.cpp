#include "test_interop.h"
#include <cstdio>
#include <iostream>
int fun2(int x){
    printf("This is fun2 implemented in c++\n");
    return x+2;
}

int fun4(int x){
    printf("This is fun4 implemented in c++\n");
    return x+4;
}

