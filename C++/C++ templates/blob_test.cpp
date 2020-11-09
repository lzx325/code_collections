#include <iostream>
#include <cstdio>
#include <cstring>
#include <list>
#include "Blob.h"
#include "StrBlob.h"


template<int* P>
unsigned long long ptr_nontype_param(){
    return (unsigned long long)P;
}
int main1(){
    Blob<std::string> sb{"aaa","bbb"};
    Blob<std::string> sb_copy(sb);
    sb_copy.pop_back();
    std::cout<<sb<<std::endl;
    return 0;
}
int main2(){
    StrBlob sb{"ccc","ddd"};
    StrBlob sb_copy(sb);
    sb_copy.pop_back();
    std::cout<<sb<<std::endl;
    return 0;
}
int main3(){
    // Pal1<std::string> is friend of Blob<std::string>
    Blob<std::string> bs1{"aaa","bbb"};
    Pal1<std::string> bs1_p{"1"};
    bs1_p.print_blob_and_something_else(bs1);

    // Pal2<std::string> and Pal2<int> are both friend of Blob<std::string>
    Blob<std::string> bs2{"ccc","ddd"};
    Pal2<std::string> bs2_p{"2"};
    bs2_p.print_blob_and_something_else(bs2);
    Pal2<int> bs2_i{100};
    bs2_i.print_blob_and_something_else(bs2);
    return 0;
}

int main4(){
    // Pal1<std::string> is friend of Blob<std::string>
    Blob<std::string> bs1{"aaa","bbb"};
    BlobPtr<std::string> bs1_ptr(bs1);
    std::cout<<*bs1_ptr<<std::endl;
    ++bs1_ptr;
    std::cout<<*bs1_ptr<<std::endl;
    ++bs1_ptr;
    std::cout<<*(--bs1_ptr)<<std::endl;
    return 0;
}

int main5(){
    int ia[] = {0,1,2,3,4,5,6,7,8,9};
    std::vector<long> vi = {0,1,2,3,4,5,6,7,8,9};
    std::list<const char*> w = {"now", "is", "the", "time"};
    Blob<int> a1(std::begin(ia),std::end(ia));
    Blob<int> a2(vi.begin(),vi.end());
    Blob<std::string> a3(w.begin(),w.end());
    std::cout<<a1<<std::endl;
    std::cout<<a2<<std::endl;
    std::cout<<a3<<std::endl;

}
