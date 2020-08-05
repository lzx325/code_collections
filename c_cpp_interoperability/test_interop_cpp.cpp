#include "test_interop.h"
#include <iostream>
int fun2(int x){
    std::cout<<"This is fun2 implemented in c++"<<std::endl;
    return x+2;
}

int fun4(int x){
    std::cout<<("This is fun4 implemented in c++")<<std::endl;
    return x+4;
}

