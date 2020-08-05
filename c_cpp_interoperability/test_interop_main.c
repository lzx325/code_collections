#include "test_interop.h"
#include <stdio.h>
void main1(){
    fun2(1); // will not cause error because g++ produces c symbols becuase it is enclosed in extern "C", and gcc expects c symbols
    // fun4(1); // will cause error because g++ produces c++ symbols, and gcc expects c symbols
}
int main(){
    main1();
    return 0;
}