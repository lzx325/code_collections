#include <iostream>
#include <cstdio>
#include <cstring>
#include <list>
#include "Blob_sep_file.h"


int main(){
    Blob<std::string> sb{"aaa","bbb"};
    Blob<std::string> sb_copy(sb);
    // Blob<int> ib {1,2}; // This is a link-time error because the template for int is not explicitly instantiated in Blob_sep_file.cpp
    sb_copy.pop_back();
    std::cout<<sb<<std::endl;
    return 0;
}
