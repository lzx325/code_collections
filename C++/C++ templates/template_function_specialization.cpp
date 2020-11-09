#include <iostream>
#include <cstring>
template<typename T> // This is a template forward declaration
int compare(const T& v1, const T& v2);

template<unsigned long long N, unsigned long long M> // This is a template function overloading
int compare(const char (&p1)[N], const char (&p2)[M]) ;

template<> // This is a template specialization declaration
int compare(const char* const &p1, const char* const &p2);



template<typename T>
int compare(const T& v1, const T& v2){
    std::cout<<"general template"<<std::endl;
    if(v1<v2) return -1;
    else if (v1==v2) return 0;
    else return 1;
}

template<unsigned long long N, unsigned long long M>
int compare(const char (&p1)[N], const char (&p2)[M]){
    std::cout<<"overloading with array reference"<<std::endl;
    return strcmp(p1,p2);
}

template<>
int compare(const char* const &p1, const char* const &p2){
    std::cout<<"template specialization"<<std::endl;
    return strcmp(p1,p2);
}

template <typename T> void foo(T);
template <typename T> void foo(T*); // overload of foo(T)
template <>           void foo<int>(int*); // full specialisation of foo(T*)
// template <>           void foo(int*); // same as the previous one

int main(){
    compare("aaa","bb"); // This will match the array reference version. "aaa": const char [4], "bb": const char [3]. It will not match not general template
    // compare("aaa","bbb"); // This will result in compilation error. It will match both the general template and array reference template with same precedence. 
    foo(new int);
}

template <typename T> void foo(T){
    std::cout<<"call from template <typename T> void foo(T)"<<std::endl;
}

template <>           void foo(int*){
    std::cout<<"call from template <>           void foo<int>(int*)"<<std::endl;
}

template <typename T> void foo(T*){
    std::cout<<"template <typename T> void foo(T*)"<<std::endl;

}