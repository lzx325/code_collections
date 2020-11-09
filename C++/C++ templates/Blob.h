#include <vector>
#include <memory>
#include <iostream>
template<typename T> class Blob;
template<typename T> std::ostream& operator<<(std::ostream& os,const Blob<T>& sb);
template<typename T> class Pal1; // Since a specific instantiation of Pal1 is declared as friend to Blob, Pal1 should be forward declared. Please don't ask why.
template<typename T> class Pal2; // This forward declaration of Pal2 is not required, since all instantiation of Pal2 are declared as friend to Blob. Please don't ask why.
template<typename> class BlobPtr; // This is forward declaration of BlobPtr, the template parameters can be omitted.
template<typename T>
class Blob{
    public:
    typedef T value_type;
    typedef typename std::vector<T>::size_type size_type; // `typename` here is required. TODO: size_type is a member type of std::vector<T>, due to ambiguity explained in C++ Primer pp. 670, one need to use `typename` before `std::vector<T>::size_type` to show that `std::vector<T>::size_type` is a type member, not a static variable member
    Blob();
    Blob(std::initializer_list<T> il);
    template<typename It> Blob(It b, It e); // A constructor that itself is a template function
    size_type size() const {return data->size();}
    bool empty() const {return data->empty();}
    void push_back(const std::string &t) {data->push_back(t);}
    void pop_back();
    T& front();
    T& back();
    private:
    std::shared_ptr<std::vector<T>> data;
    void check(size_type i, const T& msg) const;
    friend std::ostream& operator<<  <> // This <> here makes operator<< to behave as a template function
    (std::ostream&,const Blob<T>&);
    friend class Pal1<T>; // befriend with a specific instantiation of Pal1
    template<typename X>
    friend class Pal2; // befriend with all instantiation of Pal2, note that it is not Pal2<X>
    friend class BlobPtr<T>;
    
};

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

template<typename T>
class Pal1{
    public:
    template<typename U>
    void print_blob_and_something_else(const Blob<U>& sb){
        std::cout<<"{ ";
        for(const U& item:*sb.data){
            std::cout<<item<<" ";
        }
        std::cout<<"}";
        std::cout<<"  Pal1 something_else: "<<something_else<<std::endl;
    }
    T something_else;
};

template<typename T>
class Pal2{
    public:
    template<typename U>
    void print_blob_and_something_else(const Blob<U>& sb){
        std::cout<<"{ ";
        for(const U& item:*sb.data){
            std::cout<<item<<" ";
        }
        std::cout<<"}";
        std::cout<<"  Pal2 something_else: "<<something_else<<std::endl;
    }
    T something_else;
};

template <typename T> class BlobPtr{
    public:
    BlobPtr(): curr(0) {}
    BlobPtr(Blob<T> &a,size_t sz=0):wptr(a.data),curr(sz) {}
    T& operator*() const{
        auto p=check(curr,"dereference past end");
        return (*p)[curr];
    }
    BlobPtr<T>& operator++();
    BlobPtr& operator--(); // refering to BlobPtr inside BlobPtr scope automatically means BlobPtr<T>
    private:
        std::shared_ptr<std::vector<T>> check(std::size_t,const std::string&) const;
        std::weak_ptr<std::vector<T>> wptr; // stores the pointer to the head of the blob
        std::size_t curr; // stores the current location that the BlobPtr points to
};
template <typename T> std::shared_ptr<std::vector<T>> BlobPtr<T>::check(std::size_t i, const std::string &msg) const{
    auto ret=wptr.lock();
    if(!ret){
        throw std::runtime_error("unbound BlobPtr");
    }
    if(i>=ret->size()){
        throw std::out_of_range(msg);
    }
    return ret;
}


template <typename T> BlobPtr<T>& BlobPtr<T>::operator++(){
    ++curr;
    return *this;
}

template <typename T> BlobPtr<T>& BlobPtr<T>::operator--(){
    --curr;
    return *this;
}