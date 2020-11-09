#include "Blob_sep_file.h"
template <typename T> Blob<T>::Blob(): data(std::make_shared<std::vector<T>>()) {}

template <typename T> Blob<T>::Blob(std::initializer_list<T> il): data(std::make_shared<std::vector<T>>(il)) {
    std::cout<<"Values in initializer_list: {";
    for(const std::string* p=il.begin();p<il.end();p++){ // This shows how to use an initializer_list
        std::cout<<" "<<*p<<" ";
    }
    std::cout<<"}"<<std::endl;
}

template <typename T> // The type parameter for class Blob
template <typename It> // The type parameter for the function itself
Blob<T>::Blob(It b, It c): data(std::make_shared<std::vector<T>>(b, c)) {}

template <typename T> void Blob<T>::check(size_type i, const T &msg) const{
    if( i>=data->size()){
        throw std::out_of_range(msg);
    }
}

template <typename T> T& Blob<T>::front(){
    check(0,"front on empty StrBlob");
    return data->front();
}

template <typename T> T& Blob<T>::back(){
    check(0,"back on empty StrBlob");
    return data->back();
}

template <typename T> void Blob<T>::pop_back(){
    check(0,"pop_back on empty StrBlob");
    data->pop_back();
}

template <typename T> inline
std::ostream& operator<<(std::ostream& os,const Blob<T>& sb){
    os<<"{ ";
    for(const T & item:*sb.data){
        os<<item<<" ";
    }
    os<<"}";
    return os;
}

template class Blob<std::string>;
template std::ostream& operator<< <std::string>(std::ostream& os,const Blob<std::string>& sb);
// template std::ostream& operator<< <>(std::ostream& os,const Blob<std::string>& sb); // This is also fine
// template std::ostream& operator<< (std::ostream& os,const Blob<std::string>& sb); // This is also fine