#include "test_interop.h"
#include <cstdio>
void main1(){
    fun1(1); // will not cause error becuase gcc will not produce c++ symbols for fun3 and g++ expects c symbols for fun3 since it is enclosed in extern "C"
    // fun3(1); // will cause error becuase gcc will not produce c++ symbols for fun3 but g++ expects c++ symbols for fun3
}
int main(){
    main1();
    return 0;
}